#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, os, lf
cgitb.enable()

#<---------------Everything by Muhamed Rahman------------->
field=cgi.FieldStorage()

form='''<form class="form-horizontal action="sell.py" method="get" enctype="multipart/form-data">
What would you like to sell?
<div class="control-group">
	<input type="text" name='item' placeholder="item name">
	<select name="0">
		<option value="All">All</option>
		<option value="Home_and_Kitchen">Home and Kitchen</option>
		<option value="Education">Education</option>
		<option value="Electronics">Electronics</option>
	</select>
</div>
	<textarea name="description" cols="25" rows="5">description</textarea>
<div class="control-group">
<select name="1">
<option value="condition">condition</option>
<option value="10">10</option>
<option value="9">9</option>
<option value="8">8</option>
<option value="7">7</option>
<option value="6">6</option>
<option value="5">5</option>
<option value="4">4 or lower</option>
</select>
</div>
<input type="text" name="sb" placeholder="Starting Bid">
<input type="submit" name="next" value="next"></form>
'''

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

def sell():
    ans=''
    user=lf.getUser()
    f=open('../data/allfile.txt', 'r')
    items=f.read().split('\n')
    f.close()
    itemid=items[-2].split(',')[0]
    f=open('../data/allfile.txt', 'a')
    if user!=-1:
        if 'submit' in field.keys():
            f.write(str(int(itemid)+1)+','+field['item'].value+','+lf.getUser()+','+field['0'].value+','+field['sb'].value+','+'bidder'+','+field['1'].value+','+field['description'].value+'\n')#user+','+
            f.close()
            fileitem = field['filename']
            if fileitem.filename:
                # strip leading path from file name to avoid 
                # directory traversal attacks
                fn = os.path.basename(fileitem.filename)
                newname=str(int(itemid)+1)+'.'+fn.split('.')[1]
                open('data/' + fn, 'wb').write(fileitem.file.read())
                ans += 'The file "' + fn + '" was uploaded successfully'
            else:
                ans += 'No file was uploaded'
    else:
        ans+='''<meta HTTP-EQUIV="REFRESH" content="0; url=homepage.py">
        <a href="homepage.py">Login</a>'''
    return ans


if len(field)<1:
    page+=form
if 'next' in field.keys():
    page+='''<form enctype="multipart/form-data" action="save_file.py" method="post" >
<p>Image Files ONLY: <input type="file" name="file"></p>
<input type="hidden" name="item" value="'''+ str(field.getvalue('item'))+'''">
<input type="hidden" name="0" value="'''
    page+=str(field.getvalue('0'))+'''">
<input type="hidden" name="description" value="'''
    page += str(field.getvalue('description'))+'''">
<input type="hidden" name="sb" value="'''
    page += str(field.getvalue('sb'))+'''">
<input type="hidden" name="1" value="'''
    page+=str(field.getvalue('1'))+'''">
<input type="submit" value="Upload">
</form>'''

print page + '</body></html>' 
