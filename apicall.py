


import sys
import requests
from requests.auth import HTTPDigestAuth
import json
import export 
import helpers


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

myResponseServices = requests.get(urlServices, verify=True)
# For successful API call, response code will be 200 (OK)

dailyJSON = json.loads(myResponseDaily.content)



servicesJSON = json.loads(myResponseServices.content)

print(servicesJSON['rows'])
export.exportDailyStats(dailyJSON['rows'], servicesJSON['rows'],fileName)




