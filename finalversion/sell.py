#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, os, lf
cgitb.enable()

#<---------------Everything by Muhamed Rahman------------->
from lf import field

form='''<div class="container">
			<form class="form-horizontal" action="save_file.py" method="post" enctype="multipart/form-data">
				<div class="control-group">
					<label class="control-label" for="itemName"><b>Item Name</b></label>
					<div class="controls">
					<input class="input-large" type="text" name="item" id="itemName" placeholder="item name">
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="category"><b>Category</b></label>
					<div class="controls">
					<select id="category" name="0" class="input-large">
						<option value="All">All</option>
						<option value="Home_and_Kitchen">Home and Kitchen</option>
						<option value="Education">Education</option>
						<option value="Electronics">Electronics</option>
					</select>
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="description"><b>Description</b></label>
					<div class="controls">
					<textarea class="input-large" name="description" id="description" cols="25" rows="5"></textarea>
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="condition"><b>Condition</b></label>
					<div class="controls">
					<select name="1" id="condition">
					<option value="10">10</option>
					<option value="9">9</option>
					<option value="8">8</option>
					<option value="7">7</option>
					<option value="6">6</option>
					<option value="5">5</option>
					<option value="4">4 or lower</option>
					</select>
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="bid"><b>Starting Bid</b></label>
					<div class="controls">
					<input type="text" name="sb" placeholder="Enter Bid">
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="fileinput"><b>Upload an Image</b></label>
					<div class="controls">
					<input type="file" id="fileinput" name="file">
					</div>
				</div>
				<div class="controls">
					<button type="submit" class="btn btn-default" name="next" value="next">Submit</button>
				</div>
			</form>
</div>'''

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

print page + '</body></html>' 
