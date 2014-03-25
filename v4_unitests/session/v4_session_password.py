import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class V4_password():
    def __init__(self,member_id,auth_token,action,username,current_password,kPassword,email):
        self.member_id = member_id
        self.auth_token = auth_token
        self.action = action
        self.username = username
        self.current_password = current_password
        self.kPassword = kPassword
        self.email = email

    def password(self, api_url):
        passwordUrl = api_url + "session/password"
        passwordValues = {"auth_member_id" : self.member_id,
                          "auth_token" : self.auth_token,
                          "action" : self.action,
                          "username" : self.username,
                          "current_password" : self.current_password,
                          "password" : self.kPassword,
                          "email" : self.email
                      }
        passwordData = urllib.urlencode(passwordValues)
        passwordReq = urllib2.Request(passwordUrl,passwordData)
        passwordResponse = urllib2.urlopen(passwordReq)
        passwordJSON = json.load(passwordResponse)
        passwordContainer = passwordJSON["data"]
        return passwordContainer

