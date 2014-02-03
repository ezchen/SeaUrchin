#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
import os
import md5
import lf
import time

print "Content-Type: text/html\n\n"

fieldData = lf.getFieldData()
user = lf.getUser()
#<-----------------Everything is by Eric Chen-------------->
def loginForm():
	return '''<html>
<head>
	<link href="css/style.css" rel="stylesheet" type="text/css">
</head>
<body background="../data/boat.jpg">
	<div id="topright">
		<a href="create.html">Click Here to Register</a>
	</div>
	<div id="title">
		<h1>Sea-Urchin</h1>
	</div>
	<form id="loginForm" class="round" method="get" action="homepage.py">
	<div class="field">
		<input type="text" class="input" name="user" id="user" placeholder="Username">
	</div>
	<div class="field">
		<input type="password" class="input" name="password" id="password"
		placeholder="password">
	</div>
	<div class="field">
		<input type="checkbox" name="checkbox" id="checkbox">
		<label for="checkbox">Remember me</label>
	</div>
	<input type="submit" name="login" class="button" value="Login">
</div>
</body>
</html>'''

def makeFailCreatePage():
	return '''
		<!DOCTYPE html>
	<html>
	<head>
		<link href="css/createstyle.css" rel="stylesheet" type="text/css">
		<title>create</title>
	</head>
	<body background="../data/boat.jpg">
		<div id="topright">
			<a href="homepage.py">Click Here to Login</a>
		</div>

		<div id="title">
			<h1>Sea-Urchin</h1>
		</div>

		<form id="createAccountForm" class="round" method="get" action="homepage.py">
		<div id="failure">
			REPLACE
		</div>
		<div class="field">
			<input type="text" class="input" name="user" id="user" placeholder="Username">
		</div>
		<div class="field">
			<input type="password" class="input" name="password" id="password" placeholder="password">
		</div>
		<div class="field">
			<input type="text" class="input" name="email" id="email" placeholder="email">
		</div>
		<input type="submit" name="create" class="button" value="Create Account">
		</div>
		</form>
	</body>
	</html>
	'''

def accountCreater(fieldData, UsersDirectory = '../data/users.txt'):
	userData = lf.organizeData(UsersDirectory)
	usernames = userData.keys()
	emails = [userData[key][1] for key in userData]
	if 'user' in fieldData and 'password' in fieldData and 'email' in fieldData:
		if fieldData['user'] in usernames:
			return makeFailCreatePage().replace('REPLACE', 'Username Taken')
		elif fieldData['email'] in emails:
			return makeFailCreatePage().replace('REPLACE', 'Email Taken')
		elif '@' not in fieldData['email']:
			return makeFailCreatePage().replace('REPLACE', 'Invalid Email')
		else:
			f = open(UsersDirectory, 'a')
			f.write(fieldData['user'] + ',' + lf.e_pass_Field(fieldData) + ',' + fieldData['email'] + '\n')
			f.close()
			return loginForm()
	else:
		return makeFailCreatePage().replace('REPLACE', 'Please fill in all the information')


def makeFailLoginPage():
	return '''<html>
	<head>
		<link href="css/createstyle.css" rel="stylesheet" type="text/css">
	</head>
	<body background="../data/boat.jpg">
	<div id="topright">
		<a href="homepage.py?create=on">Click Here to Register</a>
	</div>
	<div id="title">
		<h1>Sea-Urchin</h1>
	</div>
	<form id="loginForm" class="round" method="get" action="homepage.py">
		<div id="failure">
			Invalid Login
		</div>
		<div class="field">
			<input type="text" class="input" name="user" id="user" placeholder="Username">
		</div>
		<div class="field">
			<input type="password" class="input" name="password" id="password"
			placeholder="password">
		</div>
		<div class="field">
			<input type="checkbox" name="checkbox" id="checkbox">
			<label for="checkbox">Remember me</label>
		</div>

		<input type="submit" name="login" class="button" value="Login">
	</form>'''

def alreadyLoggedIn():
	return '''<html>
	<head>
		<meta http-equiv="refresh" content="0; url=search.py">
		<link href="css/style.css" rel="stylesheet" type="text/css">
	</head>
	<body background="../data/boat.jpg">
	<div id="title">
		<h1>Sea-Urchin</h1>
	</div>
	<div id="block">
		<div class="top">
			REPLACE
		</div>
		<div class="middle">
			<a href="profile.py">Continue To Website</a>
		</div>
		<div class="bottom">
			<a href="homepage.py?logout=true">Logout</a>
		</div>
	</div>
	</body>
	</html>'''

def login(fieldData, UsersDirectory, loggedinDirectory):
	if lf.loginChecker(fieldData, UsersDirectory):
		if 'checkbox' in fieldData:
			lf.writeToLoggedin(loggedinDirectory, fieldData['user'], 'true')
			user = lf.getUser()
			return alreadyLoggedIn().replace('REPLACE', 'Welcome ' + user)
		else:
			lf.writeToLoggedin(loggedinDirectory, fieldData['user'], str(time.time()))
			user = lf.getUser()
			return alreadyLoggedIn().replace('REPLACE', 'Welcome ' + user)
	else:
		return makeFailLoginPage()

def logout():
	if lf.isLoggedIn('../data/loggedin.txt'):
		loggindata = lf.organizeData('../data/loggedin.txt')
		del loggindata[str(cgi.escape(os.environ["REMOTE_ADDR"]))]
		out = ''
		for key in loggindata:
			out += key + ','
			for data in loggindata[key][:-1]:
				out += data + ','
			out += loggindata[key][-1] + '\n'
		f = open('../data/loggedin.txt', 'w')
		f.write(out)
		f.close()

def makePage():
	if 'create' in fieldData:
		return accountCreater(fieldData, '../data/users.txt')
	elif 'logout' in fieldData:
		logout()
		return loginForm()
	elif lf.isLoggedIn('../data/loggedin.txt'):
		return alreadyLoggedIn().replace('REPLACE', 'Welcome ' + user)
	elif 'login' in fieldData:
		return login(fieldData, '../data/users.txt', '../data/loggedin.txt')
	else:
		return loginForm()

print makePage()
