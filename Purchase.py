#!/usr/bin/env python

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
			<head>Your Purchase</head><br>
			<body>
			You purchased the following items:<br>
			"""
	
			form = cgi.FieldStorage()
			basket = form.getvalue('item')

			print "<p>%s %s</p>" %(basket[0], basket[1])

			while basket != None:
				print "<p>%s %s</p>" %(basket[0], basket[1])
					
			print """
			</body>
			</html>
			"""
