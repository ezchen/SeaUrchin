#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, lf, glob, os
cgitb.enable()
field=cgi.FieldStorage()
#<--------------Everything is by Muhamed Rahman---------------->
page='''<html>
<head>
    <title>Search Results</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
</head>

<body>
    <script src="js/bootstrap.min.js"></script>'''

page += lf.makeNavBar()
rowStart ='''<div class="row-fluid">
	<ul class="thumbnails">'''
rowEnd ='''    </ul>
</div>'''

#<---Returns a table of all the matching results--->
itemidIndex=0
itemNameIndex=1
userIndex=2
categoryIndex=3
bidIndex=4
conditionIndex=6

#takes input of where each info is located in the allfile.txt
def searchresults(itemid=itemidIndex, itemName=itemNameIndex, user=userIndex, bid=bidIndex,
		category=categoryIndex, condition=conditionIndex, rowStart=rowStart, rowEnd=rowEnd):

    field=cgi.FieldStorage()
    ans=''
    categories=['Electronics', 'Home_and_Kitchen', 'Education', 'category']
    if 'search' in field.keys() and field['search'].value != '':
		if 'category' in field.keys():
			for i in categories:
				if field['category'].value==i:
					f=open('../data/allfile.txt', 'r')
					items=f.read().split('\n')
					x=0
					thumbNails=[]
					otherMatches=[]
					while x < len(items):
						result=items[x].split(',')
						if field['search'].value in result:
							thumbNail = makeThumbNail(result[itemid],
									getImageName(result[itemid]),
									result[itemName],
									result[bid],
									result[user],
									result[category],
									result[condition])
							if field['category'].value == i:
								thumbNails.append(thumbNail)
							else:
								otherMatches.append(thumbNail)
						x+=1

					if thumbNails.__len__() == 0 and otherMatches.__len__() == 0:
						ans = '<h3>No Results for "%s"</h3>\n<div class="container"> %s' % (
								field['search'].value, displayAll(itemid,
									itemName,user,bid,category,condition,rowStart,rowEnd) + '</div>')
					else:
						#group elements into correct number of columns
						si = iter(thumbNails)
						thumbNails = [c+next(si, '')+next(si, '') for c in si]
						si = iter(otherMatches)
						otherMatches = [c+next(si, '')+next(si, '') for c in si]

						#join the rows together by adding <ul> tags
						ans = '''<h3>%s</h3>
						<div class="container">''' % (field['search'].value)
						ans+= rowStart+(rowEnd+rowStart).join(thumbNails)+rowEnd+'</div>'
						ans+= rowStart+(rowEnd+rowStart).join(otherMatches)+rowEnd+'</div>'

					
					
					
		else:
			ans = '<div class="container">\n<h3>No Results</h3> %s' % (displayAll(itemid,itemName,user,bid,
					category,condition,rowStart,rowEnd) + '</div>')
    else:
        ans = '<h3>No Search Entered</h3>\n<div class="container"> %s' % (displayAll(itemid,itemName,user,bid,
				category,condition,rowStart,rowEnd) + '</div>')
    return ans

def displayAll(itemid, itemName, user, bid,
		category, condition, rowStart, rowEnd):

	f=open('../data/allfile.txt')
	items=f.read().split('\n')
	f.close()

	thumbNails=[]
	for item in items:
		if item != '':
			result = item.split(',')
			thumbNails.append(makeThumbNail(result[itemid],
										getImageName(result[itemid]),
										result[itemName],
										result[bid],
										result[user],
										result[category],
										result[condition]))
	si = iter(thumbNails)
	thumbNails = [c+next(si, '')+next(si, '') for c in si]
	ans = rowStart+(rowEnd+rowStart).join(thumbNails)+rowEnd
	return ans





def makeThumbNail(itemid, imageName, itemName, bid, user, category, condition):
	s='''<li class="span4">
		<a href="displayItem.py?itemid=%s" class="thumbnail">
			<img src="../data/images/%s" style="width: 300px; height: 200px;">
				<ul class="inline">
					<li><h3 class="text-info">%s</h3></li>
					<li><h3 class="text-success">%s$</h3></li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Owner</strong></li>
					<li class="muted">%s</li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Category</strong></li>
					<li class="muted">%s</li>
				</ul>
				<ul class="inline">
					<li class="muted"><strong>Condition</strong></li>
					<li class="muted">%s</li>
				</ul>
		</a>
	</li>
	''' % (itemid, imageName, itemName, bid, user, category, condition)
	return s


def getImageName(itemNumber, filedirectory = '../data/images'):
	imageFiles = glob.glob('../data/images/*.png') + glob.glob('../data/images/*.jpg') + glob.glob('../data/images/*.gif')

	itemname = 'nopicture.jpg'

	if itemNumber == 'nopicture':
		itemname = 'nopicture.jpg'
	else:
		D = lf.organizeData('../data/allfile.txt')
		if itemNumber in D:
			itemname = D[itemNumber][0]

			for image in imageFiles:
				itemid = stripEnding(os.path.basename(image))
				if itemNumber == itemid:
					return os.path.basename(image)
				else:
					itemname = 'nopicture.jpg'
	return itemname

def stripEnding(string):
	index = string.find('.')
	return string[:index]


page+=searchresults()
page+='''</table>
</body>
</html>'''

print page
        
