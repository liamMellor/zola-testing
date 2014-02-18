import urllib
import urllib2
import json
import random
import string
import re
import time
import os

class V4_token():
	def __init__(self, member_id, auth_token, action):
		self.member_id = member_id
		self.auth_token = auth_token
		self.action = action

	def token(self, api_url):
		tokenUrl = api_url + 'session/token'
		tokenValues = {'auth_member_id' : self.member_id,
			       'auth_token' : self.auth_token,
			       'action' : self.action}
		
		tokenData = urllib.urlencode(tokenValues)
		tokenReq = urllib2.Request(tokenUrl, tokenData)
		tokenResponse = urllib2.urlopen(tokenReq)
		tokenJSON = json.load(tokenResponse)

		tokenContainer = tokenJSON["data"]
                return tokenContainer
