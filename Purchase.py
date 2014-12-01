#!/usr/bin/env python

import os
import re
import cgi
import cgitb
import fileinput
cgitb.enable()

def mult(a, b):
	return a*b

#open the loggedIn.csv file and search through it to find a user
try:
	inven = open("inventory.csv", "r")
except IOError:
	print "Cannot open inventory"
#else:
#	invenline = inven.readline()

try:
	inf = open("loggedIn.csv", "r")
except IOError:
	print "Cannot open user list"
else:
	lines = inf.readlines()

	form = cgi.FieldStorage()
	basket = form.getvalue('username')

	#split string on last occurrence of ","
	#this is used to find the last logged in user
	lastuser = lines.rpartition(",")

#	for i in range(len(lines)):
#		if not re.search(basket[0], lines[i]):
		if line[2] != basket[0]:
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
			for index in range(1):
					
				sumtot = 0

				inventoryline = inven.next()
				numitem1 = inventoryline.split(",")
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
#				form = cgi.FieldStorage() 
#				checkedboxes1 = requests.get('item1')
#				print checkedboxes
				basket = form.getvalue('item1')
				purch_item1 = int(basket[1])
				new_item1_inv = 0
#			if checkedboxes1:

				if eval('int(numitem1[1]) - int(basket[1])') < 0:
					print "<p>ERROR: PURCHASE NOT PERMITTED.</p>"
					#PUT SOME KIND OF GODDAMN QUIT SHIT HERE OR W/E
				else:
					print "<td>%s</td>" %(basket[0])
					print "<td>%s</td>" %(basket[1])
					cost1 = mult(purch_item1, 1)
					new_item1_tempinv = eval('int(numitem1[1]) - int(basket[1])')
					new_item1_inv = new_item1_tempinv
					print "<td>%d$</td><tr>" %(cost1)
					sumtot += cost1
			
				item1_for_csv = [basket[0], new_item1_inv, 1]
				inventoryline = inven.next()
				numitem2 = inventoryline.split(",")			
#				checkedboxes2 = requests.get('item2')
				basket = form.getvalue('item2')
				purch_item2 = int(basket[1])
				new_item2_inv = 0
							
				if eval('int(numitem2[1]) - int(basket[1])') < 0:
					print "<p>ERROR: PURCHASE NOT PERMITTED.</p>"
#			if checkedboxes2:
				else:
					print "<td>%s</td>" %(basket[0])
					print "<td>%s</td>" %(basket[1])
					cost2 = mult(purch_item2, 2)
					#COMPUTE FINAL INVENTORY OF ITEM
					new_item2_tempinv = eval('int(numitem2[1]) - int(basket[1])')
					new_item2_inv = new_item2_tempinv
					#PRINT AND UPDATE SUM
					print "<td>%d$</td><tr>" %(cost2)
					sumtot += cost2
#			checkedboxes3 = requests.get('item3')
		
				item2_for_csv = [basket[0], new_item2_inv, 2]
				#TAKE NEXT LINE IN INVENTORY
				inventoryline = inven.next()
				#SPLIT STRING BY COMMA
				numitem3 = inventoryline.split(",")
				#GET NEW BASKET
				basket = form.getvalue('item3')
				#STORE NUMBER OF PURCHASED ITEMS IN VAR
				purch_item3 = int(basket[1])
				#INITIALIZE FINAL ITEM INVENTORY
				new_item3_inv = 0

				if eval('int(numitem3[1]) - int(basket[1])') < 0:
					#IF TRYING TO PURCHASE TOO MANY ITEMS, DO NOT ALLOW
					print "<p>ERROR: PURCHASE NOT PERMITTED.</p>"
				else:
#			if checkedboxes3:
					print "<td>%s</td>" %(basket[0])
					print "<td>%s</td>" %(basket[1])
					#COMPUTE THE COST
					cost3 = mult(purch_item3, 3)
					#COMPUTE THE FINAL INVENTORY
					#NOTICE THAT WE MADE TWO INV VARS BECAUSE WE NEED THEM TO BE IN SCOPE LATER
					new_item3_tempinv = eval('int(numitem3[1]) - int(basket[1])')
					new_item3_inv = new_item3_tempinv
					#PRINT THE COST
					print "<td>%d$</td><tr>" %(cost3)
					#CHANGE THE SUM
					sumtot += cost3

				item3_for_csv = [basket[0], new_item3_inv, 3]

				#CLOSE THE FILE	
				inven.close()

				first_line = item1_for_csv[0] +','+ str(item1_for_csv[1]) +','+ str(item1_for_csv[2])
                                second_line = item2_for_csv[0] +','+ str(item2_for_csv[1]) +','+ str(item2_for_csv[2])
                                third_line = item3_for_csv[0] +','+ str(item3_for_csv[1]) +','+ str(item3_for_csv[2])
				

				try:
					rewriteinv = open("inventory.csv", "r+")
				except IOError:
					print "Cannot open inventory"
				else:	
					rewriteinv.write(first_line)
					rewriteinv.write("\n")
					rewriteinv.write(second_line)
					rewriteinv.write("\n")
					rewriteinv.write(third_line)
				
					rewriteinv.close()
				print "</tr><td></td><td></td><td>"
				print "%s$</td>" %(sumtot)
				print "</tr></table>"
				
				print """
				<a href=\"/~eugoli/catalogue.html\">Catalogue</a>
				</body>
				</html>
				"""
