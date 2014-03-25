import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class Manager():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self, value_dict):
        self.value_dict = value_dict
        
    def request(self, api_url, endpoint):
        url = api_url + endpoint
        data = urllib.urlencode(self.value_dict)
        print url + "?" + data
        req = urllib2.Request(url, data)
        response = None
        code = None
        try:
            response = urllib2.urlopen(req)
            s = [response.getcode(), json.load(response)]
            return Manager.OKGREEN + self.dump(s) + Manager.ENDC
        except urllib2.HTTPError as e:
            s = [e, e.read()]
            return Manager.FAIL + self.dump(s) + Manager.ENDC
        
    def dump(self, s):
        if len(s) > 1:
            return json.dumps(s[1], indent=4, sort_keys=False)
        else: 
            return s
