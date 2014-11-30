#!/usr/bin/env python

#TO DO: MAKE IT SO THAT THE INVENTORY DECREASES AS YOU BUY STUFF. 
#TO DO: MAKE IT SO THAT YOU CANNOT BUY STUFF IF THERE ISN'T ENOUGH IN THE INVENTORY
#import requests
import re
import cgi
import cgitb
cgitb.enable()

def mult(a, b):
	return a*b

#open the loggedIn.csv file and search through it to find a user
try:
	inven = open("inventory.csv", "r+")
except IOError:
	print "oh my god"
else:
	invenline = inven.readlines()

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
		for l in range(len(invenline)):
			numitem1 = invenline.split(",")
	#			for i in range(len(invenline)):
				print "Content-type: text/html\n\n"
				print """
				<html>
				<head>You purchased the following items</head><br>
				<body>
				<table border=\"1\" style=\"text-align:center;\">
				<tr>
				<th>Item Name</th>
				<th>Item Quantity</th>
				<th>Item (Total) Price</th>
				</tr>
				<tr>
				"""
				form = cgi.FieldStorage() 
#			checkedboxes1 = requests.get('item1')
#			print checkedboxes
				basket = form.getvalue('item1')

#			if checkedboxes1:
				
				if eval('int(numitem1[1]) - int(basket[0])') < 0:
					print "<p>ERROR: PURCHASE NOT PERMITTED.</P>"
	
				print "<td>%s</td>" %(basket[0])
				print "<td>%s</td>" %(basket[1])
				cost1 = mult(int(basket[1]), 1)
				print "<td>%d</td><tr>" %(cost1)
			
#			checkedboxes2 = requests.get('item2')
				basket = form.getvalue('item2')

#			if checkedboxes2:
				print "<td>%s</td>" %(basket[0])
				print "<td>%s</td>" %(basket[1])
				cost2 = mult(int(basket[1]), 2)
				print "<td>%d</td><tr>" %(cost2)

#			checkedboxes3 = requests.get('item3')
				basket = form.getvalue('item3')
#
#			if checkedboxes3:
				print "<td>%s</td>" %(basket[0])
				print "<td>%s</td>" %(basket[1])
				cost3 = mult(int(basket[1]), 3)
				print "<td>%d</td><tr>" %(cost3)
			
				print "</tr><td></td><td></td><td>"
				sum = eval('cost1 + cost2 + cost3')
				print "%d</td>" %(sum)
				print "</tr></table>"
		#	while basket != None:
			#	print "<p>%s %s</p>" %(basket[0], basket[1])
					
				print """
				</body>
				</html>
				"""
