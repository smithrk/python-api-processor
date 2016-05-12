


import sys
import requests
from requests.auth import HTTPDigestAuth
import json
import export 

fileName = raw_input("Name your output File: ")
if fileName == "":
	sys.exit("you didn't enter a file name")
apiKey = raw_input("\nEnter the Access Token: ")
if apiKey == "":
	sys.exit("you didn't enter an API Key")
pubKey = raw_input("\nEnter the Publisher Key: ")
if pubKey == "":
	sys.exit("you didn't enter an publisher key")
startDate = raw_input("\nEnter the start date: (YYYY-MM-DD)")
if startDate == "":
	sys.exit("you didn't enter a date")
endDate = raw_input("\nEnter the end date: (YYYY-MM-DD)")
if endDate == "":
	sys.exit("you didn't enter a date")
	


# Replace with the correct URL
urlDaily = "http://api.po.st/analytics/v1/daily.json?access-token="+accessToken+"&pubkey="+pubKey+"&period-from="+startDate+"&period-to="+endDate
urlServices = "http://api.po.st/analytics/v1/services.json?access-token="+accessToken+"&pubkey="+pubKey+"&period-from="+startDate+"&period-to="+endDate
# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(urlDaily, verify=True)
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)

dailyJSON = json.loads(myResponse.content)

export.exportDailyStats(dailyJSON['rows'],fileName)

myResponse = requests.get(urlServices, verify=True)

