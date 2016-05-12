


import sys
import requests
from requests.auth import HTTPDigestAuth
import json
import export 

fileName = ""
apiKey = ""
pubKey = ""
startDate = ""
endDate = ""

while fileName == "":
	fileName = raw_input("Name your output File: ")	
while apiKey == "":
	apiKey = raw_input("\nEnter the Access Token: ")
while pubKey == "":
	pubKey = raw_input("\nEnter the Publisher Key: ")
while startDate == "":
	startDate = raw_input("\nEnter the start date: (YYYY-MM-DD)")
while endDate == "":
	endDate = raw_input("\nEnter the end date: (YYYY-MM-DD)")
	


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

