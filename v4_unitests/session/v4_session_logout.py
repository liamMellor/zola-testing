import urllib
import urllib2
import json
import random
import string
import re
import time 
import os

class V4_logout():
     def __init__(self, member_id, auth_token, kAll):
	self.member_id = member_id
	self.auth_token = auth_token
	self.kAll = kAll

     def logout(self, api_url):
	logoutUrl  = api_url + 'session/logout'
	logoutValues = {"auth_member_id" : self.member_id,
			"auth_token" : self.auth_token,
                        "all" : self.kAll}

	logoutData = urllib.urlencode(logoutValues)
	logoutReq = urllib2.Request(logoutUrl, logoutData)
	logoutResponse = urllib2.urlopen(logoutReq)
	
        return logoutResponse.getcode()

        


