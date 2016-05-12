



import requests
from requests.auth import HTTPDigestAuth
import json
import export 

fileName = raw_input("Name your output File: ")
if fileName == "":
	print("you didn't enter a file name")
	break
apiKey = raw_input("\nEnter the Access Token: ")
if apiKey == "":
	print("you didn't enter an API Key")
	break
pubKey = raw_input("\nEnter the Publisher Key: ")
if pubKey == "":
	print("you didn't enter a publisher key")
	break
startDate = raw_input("\nEnter the start date: (YYYY-MM-DD)")
if startDate == "":
	print("you didn't enter a date")
	break
endDate = raw_input("\nEnter the end date: (YYYY-MM-DD)")
if endDate == "":
	print("you didn't enter a date")
	break


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

