import urllib
import urllib2
import json
import random
import string
import re
import time
import os

#api_url = 'https://api.api-v4.divergence.zolaqc.com/v4/'


class V4_login():
    def __init__(self,username,password,device_name,email):
        global api_url
        self.username = username
        self.password = password
        self.device_name = device_name
        self.email = email

    def login(self, api_url):
        loginUrl = api_url + 'session/login'
        loginValues = {'username' : self.username,
                       'password' : self.password,
                       'device_name' : self.device_name,
                       'email' : self.email}
        loginData = urllib.urlencode(loginValues)
        loginReq = urllib2.Request(loginUrl,loginData)
        loginResponse = urllib2.urlopen(loginReq)
        loginJSON = json.load(loginResponse)
        loginContainer = {}
        for x,y in loginJSON["data"].iteritems():
            loginContainer[x] = y
        return loginContainer
