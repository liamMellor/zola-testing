from service_base.service import Manager
import urllib
import urllib2
import json
import random
import string
import re
import time
import os
import datetime
import time
import hashlib


sets = "############################# Logout ##################################"

class v4logout():
    
    def __init__(self, member_id, auth_token, all):
        self.member_id  = member_id
        self.auth_token = auth_token
        self.all        = all


    def logout(self, api_url):
        self.sig  = hashlib.md5('8gwb5ozh7cy6tyturnbtyipe' + 'we6jgopi6axv' + str(int(time.time()))).hexdigest()
        self.vals = { 'auth_member_id' : self.member_id,
                      'auth_token'     : self.auth_token,
                      'all'            : self.all,
                      'key'            : '8gwb5ozh7cy6tyturnbtyipe',
                      'signature'      : self.sig
                    }
        url  = api_url + "session/logout"
        data = urllib.urlencode(self.vals)
        req  = urllib2.Request(url, data)
        response = None
        response = urllib2.urlopen(req)
        m        = response.getcode()
        #print m
        if m == 204:
            print Manager.OKGREEN + 'success' + Manager.ENDC + "          " + "session/logout"
        else:
            print Manager.FAIL + 'fail ' + "HTTPError() " + str(m) + Manager.ENDC

class logoutTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url    = api_url
        self.member_id  = member_id
        self.auth_token = auth_token

    def logout(self):
        print Manager.WARNING + sets + Manager.ENDC
        a = v4logout(self.member_id, self.auth_token, "true")
        a.logout(self.api_url)




