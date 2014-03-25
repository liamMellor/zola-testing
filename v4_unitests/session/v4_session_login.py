import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class V4_login():
    def __init__(self,username,password,device_name,email):
        global api_url
        self.username = username
        self.password = password
        self.device_name = device_name
        self.email = email

    def login(self, api_url):
        loginUrl = api_url + 'session/login'
        loginValues = {'password' : self.password,
                       'device_name' : self.device_name,
                       'email' : self.email}
        loginData = urllib.urlencode(loginValues)
        loginReq = urllib2.Request(loginUrl,loginData)
        loginResponse = urllib2.urlopen(loginReq)
        loginJSON = json.load(loginResponse)
        loginContainer = {}
        return loginJSON["data"]
