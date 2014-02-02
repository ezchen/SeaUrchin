#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
import os
import glob
import md5
import lf

#<-----------Everything is by Eric Chen---------------_>

print "Content-Type: text/html\n\n"

fieldData = lf.getFieldData()
user = lf.getUser('../data/loggedin.txt')

def sellingData(username = user):
	L = lf.organizeDataL('../data/allfile.txt')
	D = {}
	for line in L:
		if username in line and username == line[2]:
			D[line[0]] = [line[1],line[3],line[5],line[4]]
	return D

def buyingData(username = user):
	watching = lf.organizeData('../data/watch.txt')
	if user in watching:
		items = watching[user]
	else:
		items = {}
	L = lf.organizeDataL('../data/allfile.txt')
	D = {}
	for item in items:
		for line in L:
			if item in line and line[2] != user:
				D[line[1]] = [line[0],line[2],line[3],line[4],line[5]]
	return D

def stripEnding(image):
	index = image.find('.')
	return image[:index]

#removes every instance of itemnumber in the watch.txt file
def removeWatch(itemnumber, filedirectory='../data/watch.txt'):
	D = lf.organizeData(filedirectory)
	for user in D:
		if itemnumber in D[user]:
			D[user] = D[user].remove(itemnumber)
			if D[user] is None:
				D[user] = []

	out = ''
	for user in D:
		out+=user
		for itemnumber in D[user]:
			out += ',' + itemnumber
	f = open(filedirectory, 'w')
	f.write(out)
	f.close()


def deleteItem(itemnumber, user = user):
	removeWatch(itemnumber)
	D = lf.organizeData('../data/allfile.txt')
	if itemnumber in D:
		if D[itemnumber][1] == user:
			imageFiles = glob.glob('../data/images/*.png') + glob.glob('../data/images/*.jpg')
			del D[itemnumber]
			for image in imageFiles:
				imageid = stripEnding(os.path.basename(image))
				if itemnumber == imageid:
					lf.sold(itemnumber, image)
			out = ''
			for item in D:
				out += item
				for data in D[item]:
					out += ',' + data
				out += '\n'
			f = open('../data/allfile.txt', 'w')
			f.write(out)
			f.close()
		else:
			return 'This is not yours'
	else:
		return 'item does not exist'

def displaySold():
	items = sellingData()
	block = '''
	<table class="table">
	<caption><strong>You Are Selling</strong></caption>'''
	if len(items) < 1:
		block+='''<tr><th><h3>You Are Not Selling Anything</h3></th></tr>'''
	else:
		block +='''<tr>
			<th>ItemId</th>
			<th>ItemName</th>
			<th>category</th>
			<th>Bidder</th>
			<th>HighestBid</th>
			<th>Mark As Sold</th>
		</tr>
		'''
		for item in items:
			block += '<tr><td>' + item + '</td>'
			for data in items[item]:
				block += '<td>' + data + '</td>'
	
			form = 	'''<form method="get" action="profile.py">
			<input type="hidden" name="solditem" value="''' + item + '''"">
			<input type="submit" value="Mark As Sold">
			</form>
			'''
	
	
			block += '<td>' + form + '</td>'
			block += '</tr>'
	block += '</table>'
	return block

def displayBuying(username = lf.getUser()):
	items = buyingData()
	block = '''
	<table class="table">
	<caption><strong>You Are Bidding On</strong></caption>'''
	if len(items) < 1:
		block += '''<tr><th><h3>You Are Not Bidding On Anything</h3></th></tr>'''
	else:
		block += '''<tr>
			<th>Itemname</th>
			<th>Itemid</th>
			<th>owner</th>
			<th>category</th>
			<th>Bid</th>
		</tr>
	'''
		for item in items:
			if username not in items[item]:
				block += '<tr class="error"><td>' + item + '</td>'
				for data in items[item][:-1]:
					block += '<td>' + data + '</td>'
				block += '</tr>'
			else:
				block += '<tr><td>' + item + '</td>'
				for data in items[item][:-1]:
					block += '<td>' + data + '</td>'
				block += '</tr>'
		block += '</table>'
	return block

def makePage():
	page = '''<!DOCTYPE html>
	<html>
	<head>
		<title>profile</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
	</head>
	<body>
	<script src="js/bootstrap.min.js"></script>
	'''
	page += lf.makeNavBar()
	if 'solditem' in fieldData:
		page += '<div id="alert">You just sold' + fieldData['solditem'][0] + '</div>'
		deleteItem(fieldData['solditem'], lf.getUser())
	page += displaySold()
	page += displayBuying()
	return page


print makePage()

print '''
</body>
</html>'''

