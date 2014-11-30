import re

#open the loggedIn.csv file and search through it to find a user

filename = loggedIn.csv
inf = open(filname, 'r')
lines = inf.readlines()

for i in range(len(lines)):
	if not re.search(thisistheusername, lines[i]):
		#if username not present then
		print "<html>"
		print "<head>ERROR</head><br>"
		print "<body>You are not logged in! Please login or create a user.<br>"
		print "<a href=\"/~eugoli/catalogue.html\"></a>"
		print "</body>"
		print "</html>"
	else:
		#display the bill	
		print "<html>"
		print "<head>Your Purchase</head><br>"
		print "<body>"
		print "You purchased the following items:"
		print "item1"
		print "            quantity1                 price1<br>"
		print "item2"
		print "            quantity2                 price2<br>"
		print "item3"
		print "            quantity3                 price3<br>"
		print "Total: totalquantity"
		print "Hello word"
		print "</body>"
		print "</html>"
