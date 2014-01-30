#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, os, lf
cgitb.enable()

from lf import field

page='''
<!DOCTYPE html>
<head>
    <title>sell</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
<html>
<body>
<script src="js/bootstrap.min.js"></script>
'''
page += lf.makeNavBar()

def saveFile():
	out=''
	user=lf.getUser()
	f=open('../data/allfile.txt', 'r')
	items=f.read().split('\n')
	f.close()
	itemid=items[-2].split(',')[0]
	f=open('../data/allfile.txt', 'a')
	if user!=-1:
		f.write(str(int(itemid)+1)+','+field['item'].value+','+
				lf.getUser()+','+field['0'].value+','+field['sb'].value+','+'bidder'+','+
				field['1'].value+','+field['description'].value+'\n')#user+','+
		f.close()
		fileitem = field['filename']
		if fileitem.filename:
			# strip leading path from file name to avoid 
			# directory traversal attacks
			fn = os.path.basename(fileitem.filename)
			newname=str(int(itemid)+1)+'.'+fn.split('.')[1]
			open('data/' + fn, 'wb').write(fileitem.file.read())
			out += 'The file "' + fn + '" was uploaded successfully'
		else:
			out += 'No file was uploaded'
	else:
        out+='''<meta HTTP-EQUIV="REFRESH" content="0; url=homepage.py">
        <a href="homepage.py">Login</a>'''
    return out
