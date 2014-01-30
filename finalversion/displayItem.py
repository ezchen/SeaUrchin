#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
import lf
import glob

print 'Content-Type: text/html\n\n'

#<--------------Muhamed Rahman---------------->
#<----------Gets Index of item using itemid-------->
def getIndex(itemID):
    f=open('../data/allfile.txt','r')
    items=f.read().split('\n')
    f.close()
    for i in items:
        if i.split(',')[0]==itemID:
            index=items.index(i)
    return index

def bid():
    user=lf.getUser()
    field=cgi.FieldStorage()
    ans=''
    if user != -1:
        if 'bid' in field.keys():
            index=getIndex(field['itemid'].value)
            f=open('../data/allfile.txt','r')
            items=f.read().split('\n')
            f.close()
            bid=items[index].split(',')[4]
            if float(field['bid'].value)>float(bid):
                items[index]=items[index].replace(items[index].split(',')[4], field['bid'].value)
                items[index]=items[index].replace(items[index].split(',')[5], lf.getUser())
                watch(field['itemid'].value)
                ans+='''Bid Successful!'''
                items='\n'.join(items)
                f=open('../data/allfile.txt', 'w')
                f.write(items)
            else:
                ans+='''Need higher bid!'''
        else:
            ans+='please bid'
    else:
        ans+='''<meta HTTP-EQUIV="REFRESH" content="0; url=homepage.py">
        <a href="homepage.py">Login</a>'''
    return ans
#<-----------------End of Functions by Muhamed-------------->
#<------------------Eric Chen -------------------->
def watch(itemid, filedirectory = '../data/watch.txt', user = lf.getUser()):
	D = lf.organizeData(filedirectory)
	if user in D:
		if itemid not in D[user]:
			D[user] += [itemid]
	else:
		D[user] = itemid
	out = ''
	for user in D:
		out += user
		for item in D[user]:
			out += ',' + itemid
		out += '\n'
	f = open(filedirectory, 'w')
	f.write(out)
	f.close()

def stripEnding(string):
	index = string.find('.')
	return string[:index]

def getItemNumber():
	if 'itemid' in fieldData:
		itemnumber = fieldData['itemid']
	else:
		itemnumber = 'nopicture'
	return itemnumber

def getEmail(username):
	users = lf.organizeData('../data/users.txt')
	if username in users:
		email = users[username][1]
	else:
		email = 'noemail'
	return email


fieldData = lf.getFieldData()

imageFiles = glob.glob('../data/*.png') + glob.glob('../data/*.jpg')

def itemName(filedirectory = '../data/'):
	imageFiles = glob.glob('../data/*.png') + glob.glob('../data/*.jpg')
	itemnumber = getItemNumber()

	if itemnumber == 'nopicture':
		itemname = 'nopicture.jpg'
	else:
		D = lf.organizeData('../data/allfile.txt')
		if itemnumber in D:
			itemname = D[itemnumber][0]
			user = lf.getUser()
			name = user + itemname

			for image in imageFiles:
				itemid = stripEnding(image)
				if name == itemid:
					itemname = image
				else:
					itemname = 'nopicture.jpg'
	return itemname

def makeForm():
	itemnumber = getItemNumber()
	D = lf.organizeData('../data/allfile.txt')
	if itemnumber in D:
		itemname = D[itemnumber][0]
		description = D[itemnumber][-1]
		condition = D[itemnumber][-2]
		bid = D[itemnumber][-4]
		username = D[itemnumber][1]
	else:
		itemname=description=condition=bid=username = "We're sorry, this item doesn't exist"
	#itemname
	html = '\n<div class="span4">' + '\n<h3>Current Bid</h3>'
	html += '\n' + bid + '$' + '''<form class="form-inline" method="get" action="displayItem.py">
	<div class="field">
		<input type="text" class="input" name="bid" placeholder="bid">
	<input type="hidden" name="itemid" value="''' + fieldData['itemid'] + '''">
	<input type="submit" class="button" value="bid">
	</form>''' + '\n</div></div>\n'
	html += '\n<div class="span4">' + '\n<h3>ItemName</h3>'
	html += '\n' + itemname + '\n</div>'
	#condition
	html += '\n<div class="span4">' + '\n<h3>Condition</h3>'
	html += '\n' + condition + '\n</div>'
	#description
	html += '\n<div class="span4">' + '\n<h3>Description</h3>'
	html += '\n' + description + '\n</div>'
	html += '''</div>'''

	#Owner and info
	html += '\n<div class="span12">'
	html += '\n' + '<strong>Owner</strong>: ' + username + '<br>' + '<strong>Email</strong>: ' + getEmail(username) + '</div>'
	html += '\n</div>'

	return html





if lf.isLoggedIn():
	print '''<!DOCTYPE html>
	<html>
	<head>
		<title>View</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
	</head>
	<body>
	<script src="js/bootstrap.min.js"></script>'''
	page = lf.makeNavBar()
	page += '<div class="container">'
	page += '<div class="row">'
	page += '<div class="span8"><img src="../data/' + itemName() + '" alt="Item" class="img-rounded"></div>'
	if 'bid' in fieldData:
		page+='<div class="span4"><div class="alert alert-error">' + bid() + '</div></div>'
	page += makeForm()
	print page + '</div></div>'
	
	
	print '''</body>
	</html>'''
else:
	print lf.redirectPage()
