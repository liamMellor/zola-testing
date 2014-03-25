import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class Manager():
     def __init__(self, value_dict):
        self.value_dict = value_dict
        
     def request(self, api_url, endpoint):
        url = api_url + endpoint
        data = urllib.urlencode(self.value_dict)
        req = urllib2.Request(url, data)
        response = None
        code = None
        try:
            response = urllib2.urlopen(req)
            return [response.getcode(), json.load(response)]
        except urllib2.HTTPError as e:
            print e
            return {"status" : "Nope!"}
