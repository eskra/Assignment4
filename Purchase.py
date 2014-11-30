#!/usr/bin/env python

#import requests
import re
import cgi
import cgitb
cgitb.enable()


#open the loggedIn.csv file and search through it to find a user

try:
	inf = open("loggedIn.csv", "r")
except IOError:
	print "oops"
else:
	lines = inf.readlines()

	for i in range(len(lines)):
		if not re.search("esther", lines[i]):
			#if username not present then
			print "Content-type: text/html\n\n"
			print """
			<html>
			<head>ERROR</head><br>
			<body>You are not logged in! Please login or create a user.<br>
			<a href=\"/~eugoli/catalogue.html\">Catalogue</a>
			</body>
			</html>
			"""
		else:
			#display the bill		

			print "Content-type: text/html\n\n"
			print """
			<html>
			<head>You purchased the following items</head><br>
			<body>
			You purchased the following items:
			<table>
			<th>Item Name</th>
			<th>Item Quantity</th>
			<th>Item (Total) Price</th>
			<td>
			"""
			form = cgi.FieldStorage() 
#			checkedboxes1 = requests.get('item1')
#			print checkedboxes
			basket = form.getvalue('item1')

#			if checkedboxes1:
			print "%s" %(basket[0])
			print "</td><td>%s" %(basket[1])
			#HERE TAKE QUANTITY AND MAKE MULTIPLY BY PRICE
			#PRINT PRICE
			
#			checkedboxes2 = requests.get('item2')
			basket = form.getvalue('item2')

#			if checkedboxes2:
			print "<p>%s %s</p>" %(basket[0], basket[1])

#			checkedboxes3 = requests.get('item3')
			basket = form.getvalue('item3')
#
#			if checkedboxes3:
			print "<p>%s %s</p>" %(basket[0], basket[1])
		#	while basket != None:
			#	print "<p>%s %s</p>" %(basket[0], basket[1])
					
			print """
			</body>
			</html>
			"""
