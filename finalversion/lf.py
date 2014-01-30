import cgi, cgitb
cgitb.enable()
import md5
import os
import time
#<----------------------------------------------------------->
#<-------- Eric Chen's "Login Functions" Module-------------->
#<----------------------------------------------------------->
#<---------Everything is made by Eric Chen------------------->
#<----------------------------------------------------------->

#<------------Simple stuff------------------------->
#<--- Puts fieldData in the format {key: value}---->
field = cgi.FieldStorage()
def getFieldData():
	return {key: field[key].value for key in field}

fieldData = getFieldData()

#<--- Puts Data in the format [[line1element1,line1element2][line2element2,line2element2]]
def organizeDataL(filedirectory):
	f = open(filedirectory, 'r')
	L = f.read().split('\n')[:-1]
	return [L[n].split(',') for n in range(0, len(L))]

#<--- Puts Data in the format {firstitem: [list of items]}---->
def organizeData(filedirectory):
	f = open(filedirectory, 'r')
	L = f.read().split('\n')[:-1]
	L = [L[n].split(',') for n in range(0, len(L))]
	return {line[0]: line[1:] for line in L}

#<--- returns an encrypted password from the field due to user input---->
def e_pass_Field(D = fieldData):
	password=D['password']
	m=md5.new()
	m.update(password)
	return str(m.hexdigest())

#<----------------------------------------------------------------------->
#<-----------------Login Functions------------------------------>
#<----------------------------------------------------------------------->
#<----------------------Deletes the line from allfile.txt, deletes the pictures too--------->
def sold(itemid, pictureFile, filedirectory = '../data/allfile.txt'):
	D = organizeData(filedirectory)
	if itemid in D:
		del D[itemid]
		if os.path.isfile('../data/' + pictureFile):
			os.remove('../data/' + pictureFile)
		

#<--------------------Deletes the ip from the file------------------------>
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
#<--- Returns True or False if the ip address of the computer accessing is 
#																in the file--->
def isLoggedIn(filedirectory = '../data/loggedin.txt'):
    ip = str(cgi.escape(os.environ["REMOTE_ADDR"]))
    D = organizeData(filedirectory)
    if ip in D:
    	ts = time.time()
    	if D[ip][1] == 'true':
    		return True
    	elif ts - float(D[ip][1]) > 2000:
    		logout()
    		return False
    	else:
    		return True
    else:
    	return False


#<--- Returns the username --->
def getUser(filedirectory = '../data/loggedin.txt'):
	if isLoggedIn(filedirectory):
		D = organizeData(filedirectory)
		return D[str(cgi.escape(os.environ["REMOTE_ADDR"]))][0]
	else:
		return -1

#<--- Writes data to 'loggedin.txt' (enter the directory) in the format:
#ipaddress1, username1, timestamp--->
# Note: does not check if the ipaddress is already there yet
def writeToLoggedin(Loggedindirectory, username, timestamp):
	f = open(Loggedindirectory, 'r')
	text = f.read()
	f.close()

	Data = organizeData(Loggedindirectory)
	ip = str(cgi.escape(os.environ["REMOTE_ADDR"]))

	if ip in Data:
		del Data[ip]
	s = ip + ',' + username + ',' + timestamp + '\n'

	for key in Data:
		s += key + ',' + Data[key][0] + ',' + Data[key][1] + '\n'

	f = open(Loggedindirectory, 'w')
	f.write(s)
	f.close()

#<--- Writes Data to UsersDirectory (enter the directory) in the format:
#username, password, email
# Note: does not check if the username/email is there yet
def writeToUsers(UsersDirectory, username, encryptedpassword, email):
	f = open(UsersDirectory, 'a')
	f.write(username + ',' + encryptedpassword + ',' + email + '\n')
	f.close()

#<--- Checks if the username/email is already there, encrypts the password,
#and writes to the file 'users.txt'--->
def accountCreater(fieldData, UsersDirectory):
	userData = organizeData(UsersDirectory)
	usernames = userData.keys()
	emails = [userData[key][1] for key in userData]
	if fieldData['user'] in usernames:
		return 'username taken'
	elif fieldData['email'] in emails:
		return 'email taken'
	else:
		writeToUsers(UsersDirectory, fieldData['user'], e_pass_Field(fieldData),
						fieldData['email'])
		return 'account created'

#<--- Returns True or False based on whether or not the ipaddress is in the file--->
def loginChecker(fieldData, UsersDirectory):
	userData = organizeData(UsersDirectory)
	if fieldData['user'] in userData:
		return e_pass_Field(fieldData) == userData[fieldData['user']][0]

#<--- Returns a string with the navbar. This should be at the top of
#		Every file after the <body> --->
#filedirectory is loggedin.txt
def makeNavBar(filedirectory = '../data/loggedin.txt'):
	navbar = '''<div class="navbar">
	<div class="navbar-inner">
		<div class="container">
			<a class="brand" href="homepage.py">Sea-Urchin</a>
			<form class="navbar-form pull-left" name="input" action="search.py" method="get">
				<input type="text" name="search" placeholder="search">
				<select name="category">
					<option value="category">All</option>
					<option value="Home_and_Kitchen">Home and Kitchen</option>
					<option value="Education">Education</option>
					<option value="Electronics">Electronics</option>
				</select>
				<input type="submit" value="search">
			</form>'''
	if isLoggedIn(filedirectory):
		ipDictionary = organizeData(filedirectory)
		user = ipDictionary[str(cgi.escape(os.environ["REMOTE_ADDR"]))][0]
		navbar += '''<ul class="nav pull-right">
				<li>
					<a href="profile.py">ericchen10</a>
				</li>
				<li>
					<a href="sell.py">Sell</a>
				</li>
				<li>
					<a href="homepage.py?logout=true">Logout</a>
				</li>
			</ul>'''
	else:
		navbar += '''<a href="homepage.py">Login</a>'''
	navbar += '''</div>
	</div>
</div>'''
	return navbar


def redirectPage():
	out = '''<!DOCTYPE html>
	<html>
	<head>
	<meta http-equiv="refresh" content="0; url=homepage.py">
	</head>
	<body>
	If you are not automatically redirected,
	<a href="homepage.py">Click here to Login</a>
	</body>
	</html>'''
	return out





#list comprehensions/dict comprehensions learned at python tutorial site:
#	http://docs.python.org/2/tutorial/datastructures.html
