SeaUrchin
=========

buying and selling python cgi website


This site is meant to replace craigslist. Craigslist's function as a trading website is great,
but the website itself is unaesthetic. The links do not display images and is not completely
discriptive of the item. We hope that our site will offer a better user experience.

Features

LF.PY
-A lot of basic functions
-navigationbar
	-A lot of useful links
		-homepage
		-your profile(displays it as your username)
		-sell
		-logout(lets you logout...)
	-If you're not logged in...
		-dropdown menu - login.
HOMEPAGE.PY
-ability to create an account and login
-ability to "stay logged in", which will keep you logged in on the computer u logged in
	with forever
		-created by writing the file 'data/loggin.txt' which keeps track of the ipaddress and
			username
-After a certain amount of time, your login will expire(for those who dont check the "remember
	me check box")
-ability to logout

PROFILE.PY
-Displays what you are selling
	-ability to "mark as sold" which deletes the item
	-We expect the users to communicate with each other via email

-Displays what you are bidding on
	-When you are outbid, the items will be red to alert the user that they
		are no longer winning the item
	-If you are not outbid, it is a normal color

SEARCH.PY
-Searches for an item based on what you enter in the search form on the navigation bar
-You can search based on categories too
-If you like an item, you can click on it and bid. This will take you to displayItem.py

DISPLAYITEM.PY
-Shows the information about the item
-Images supported, if the owner did not upload an image than it defaults to our special
	sea-urchin image that we made
-allows you to place a bid
	-if the bid is lower than the previous bid, then an alert will tell you you did
		not successfully bid
	-otherwise it bids
-disables the bidding option if you are not logged in or you own the item
