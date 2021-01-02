import webbrowser
import requests

print("Let's find an old Website.")
site=input("Type a website URL: ")
era=input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = get(url)
data=response.json()
try:
 old_site =date["archived_snapshot"]["closest"]["url"]
 print("Found this copy: ", old_site)
 print("It should appear in your browser now.")
 webbrowser.open(old_site)
except:
  print("sorry, no luck finding", site)