import urllib
import urllib2
import json

def func1():
     url = "https://zolabooks.com/api/v4/session/login"
     vals = {"device_name" : "device","email" : "jsflax@gmail.com","password" : "kingkong"}
     data = urllib.urlencode(vals)
     req = urllib2.Request(url,data)
     try:
          resp = urllib2.urlopen(req)
          try:
               mjson = json.load(resp)
               print json.dumps(mjson,indent=4,sort_keys=False)
          except ValueError as e:
               print resp.read()
     except urllib2.URLError as e:
          print e
          print e.code
          print e.read()

func1()
