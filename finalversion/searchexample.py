#!/usr/bin/python
print 'Content-Type: text/html\n\n'
#<----------------Muhamed Rahman-------------------->

page='''<!DOCTYPE html>
<html>
<body>
<form action="search.py" method="get">
<select name="category">
<option value="category">All</option>
<option value="Home_and_Kitchen">Home and Kitchen</option>
<option value="Education">Education</option>
<option value="Electronics">Electronics</option>
</select>
<br>
<br>
<input type="text" name="search" placeholder="What would you like to search for?">
<input type="submit" value="search">
</form>
<br>'''
page+='''
<form action="bid.py" method="get">
<input type="text" placeholder="bid">
<input type="hidden" name="itemid" value="item1id">
<input type="hidden" name="username" value="'''+'''
">
<input type="submit" name="bid" value="bid">
</form>
</body>
</html>'''

print page
