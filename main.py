import json
import requests

host = "yourThingworxHostName"
port = 8080         # your port number
appkey = "yourApplicationKey"
thingName = "yourThingName"

header = {"appKey": appkey, "Content-Type": "application/json"}

strData = {"humid": 25}     # your data

url = host + ':' + str(port) + "/Thingworx/Things/" + \
    thingName + "/Properties/*"

print(url)

jsonData = json.dumps(strData)

print(jsonData)

response = requests.put(url, data=jsonData, headers=header)
print(response)