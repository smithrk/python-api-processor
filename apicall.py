

import getopt
import sys
import requests
import json
import export 
import helpers
import urllib
from BeautifulSoup import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv as csv
import time
import cPickle as pickle


fileName = ""
accessToken = ""
pubKey = ""
startDate = ""
endDate = ""

while fileName == "":
	fileName = raw_input("File name: ")	
	if fileName == "Exit" or fileName == "exit":
		sys.exit("Stopping")
while accessToken == "":
	accessToken = raw_input("\nEnter the Access Token: ")
	if accessToken == "Exit" or accessToken == "exit":
		sys.exit("Stopping")
while pubKey == "":
	pubKey = raw_input("\nEnter the Publisher Key: ")
	if pubKey == "Exit" or pubKey == "exit":
		sys.exit("Stopping")
while startDate == "" or len(startDate) < 10 or len(startDate) > 10:
	startDate = raw_input("\nEnter the start date: (YYYY-MM-DD)")
	if startDate == "Exit" or startDate == "exit":
		sys.exit("Stopping")
	if not helpers.dateCheck(startDate):
		print("You entered an invalid date format")

while endDate == "" or len(startDate) < 10 or len(startDate) > 10:
	endDate = raw_input("\nEnter the end date: (YYYY-MM-DD)")
	if endDate == "Exit" or endDate == "exit":
		sys.exit("Stopping")
	if not helpers.dateCheck(startDate):
		print("You entered an invalid date format")


# Replace with the correct URL
urlDaily = "http://api.po.st/analytics/v1/daily.json?access-token="+accessToken+"&pubkey="+pubKey+"&period-from="+startDate+"&period-to="+endDate
urlServices = "http://api.po.st/analytics/v1/services.json?access-token="+accessToken+"&pubkey="+pubKey+"&period-from="+startDate+"&period-to="+endDate
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponseDaily = requests.get(urlDaily, verify=True)
dailyJSON = json.loads(myResponseDaily.content)

myResponseServices = requests.get(urlServices, verify=True)
servicesJSON = json.loads(myResponseServices.content)



mydict = {}
# list of domain names in a text file
fname = 'domains_list_v2.txt'
fhand = open(fname)
mydomains = list()
for line in fhand:
    pieces = line.split()
    domain = pieces[0]
    mydomains.append(domain)
    
import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


for i in mydomains:
    url = 'http://www.' + i
    print(url)
    time.sleep(10)
    try:
        html = opener.open(url).read()
        soup = BeautifulSoup(html)
        print url
        try:
            title = soup.title.string
        except:
            title = ''
        mydict[url] = title + keywords + description
    except:
        mydict[url] = ''


export.exportDailyStats(dailyJSON['rows'], servicesJSON['rows'],fileName)




