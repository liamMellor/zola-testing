import urllib
import urllib2
import json
def func1():
     url = "https://zolabooks.com/api/v4/book/details"
     vals = {'isbn' : '9781939126009','action' : 'get'}
     data = urllib.urlencode(vals)
     req = urllib2.Request(url,data)
     try:
          resp = urllib2.urlopen(req)
          try:
               mjson = json.load(resp)
               return json.dumps(mjson, indent=4, sort_keys=False)
          except ValueError as e:
               return resp.read()
     except urllib2.URLError as e:
          print e
          print e.code
          print e.read()
print func1()
