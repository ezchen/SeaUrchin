#! /usr/bin/python
print 'Content-Type: text/html\n\n'
import cgi, cgitb, os, lf
cgitb.enable()

#<---------------Everything by Muhamed Rahman------------->
from lf import field

form='''
			<form class="form-horizontal" action="save_file.py" method="post" enctype="multipart/form-data">
				<div class="control-group">
					<label class="control-label" for="itemName"><b>Item Name</b></label>
					<div class="controls">
					<input class="input-xxlarge" type="text" name="item" id="itemName" placeholder="item name">
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="category"><b>Category</b></label>
					<div class="controls">
					<select id="category" name="0" class="input-xxlarge">
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
					<textarea class="input-xxlarge" name="description" id="description" cols="25" rows="5"></textarea>
					</div>
				</div>
				<div class="control-group">
					<label class="control-label" for="condition"><b>Condition</b></label>
					<div class="controls">
					<select name="1" id="condition" class="input-xxlarge">
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
					<input type="text" name="sb" placeholder="Enter Bid" class="input-xxlarge">
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

if len(field)<1:
    page+=form

print page + '</body></html>' 
