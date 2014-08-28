import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class V4_account():
        def __init__(self, action, email, password):
                self.action = action
                self.email = email
                self.password = password

        def account(self, api_url):
                accountUrl = api_url + 'session/account'
                accountValues = {'action' : self.action,
                                 'email' : self.email,
                                 'password' : self.password }
                accountData = urllib.urlencode(accountValues)
                accountReq = urllib2.Request(accountUrl, accountData)
                print accountUrl + "?" + accountData
                accountResponse = urllib2.urlopen(accountReq)
                accountJSON =  json.load(accountResponse)

                accountContainer = {}
                print accountJSON

va = V4_account( "exists", "jay.flax@zolabooks.com", "kingkong")
va.account( "https://api.zolabooks.com/v4/" )
