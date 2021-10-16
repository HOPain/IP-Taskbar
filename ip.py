import urllib.request
import json
ip = "8.8.8.8"
response = urllib.request.urlopen("http://ipwhois.app/json/")
ip = json.load(response)
print (ip["ip"],("|"),(ip["country"]))
