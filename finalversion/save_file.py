#!/usr/bin/env python
print 'Content-Type: text/html\n\n'
import cgi, os, lf
import cgitb; 
cgitb.enable()

page='''
<!DOCTYPE html>
<head>
	<title>sell</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
<html>
<body>
'''
page += lf.makeNavBar()
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

from lf import field
# A nested FieldStorage instance holds the file
fileitem = field['file']

out=''
user=lf.getUser()

f=open('../data/allfile.txt', 'r')
items=f.read().split('\n')
f.close()

f=open('../data/itemNumber.txt', 'r')
itemid=f.readline()
f.close()

f=open('../data/allfile.txt', 'a')

if user!=-1:
		f.write(str(int(itemid)+1)+','+field['item'].value+','+lf.getUser()+','+field['0'].value+','+field['sb'].value+','+'bidder'+','+field['1'].value+','+field['description'].value+'\n')#user+','+
		f.close()
		f=open('../data/itemNumber.txt', 'w')
		f.write(str(int(itemid)+1))
		f.close()
		fileitem = field['file']
		if fileitem.filename:
			# strip leading path from file name to avoid 
			# directory traversal attacks
			fn = os.path.basename(fileitem.filename)
			newname=str(int(itemid)+1)+'.'+fn.split('.')[1]
			open('../data/images/' + newname, 'wb').write(fileitem.file.read())
			out += '''<meta HTTP-EQUIV="REFRESH" content="0; url=displayItem.py?itemid=%s">''' % (str(int(itemid)+1))
			out += 'The file "' + fn + '" was uploaded successfully as' + newname
		else:
			out += 'No file was uploaded'
else:
	out+='''<meta HTTP-EQUIV="REFRESH" content="0; url=homepage.py"><a href="homepage.py">Login</a>'''	

print page + out + '</body></html>'
