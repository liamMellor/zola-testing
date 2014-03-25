# My first test scipt at Zola books
# Made by Michael Galanin Test Engineer

import urllib 
import urllib2
import json

class v4coll():
	
	def __init__(self, auth_member_id, auth_token, action, type):
		global api_url
		self.auth_member_id = auth_member_id
		self.auth_token = auth_token
		self.action = action
		self.type = type 

	def list(self, api_url):
		encoded_vars = urllib.urlencode({'auth_member_id' : self.auth_member_id, 
						 'auth_token' : self.auth_token,
						 'action' : self.action ,
						 'type' :self.type })

		listUrl = api_url + "collection/lists"
		
		listReq = urllib2.Request(listUrl, encoded_vars)
		resp = urllib2.urlopen(listReq)
		jsonResp = json.load(resp)
		
		return jsonResp["data"]


