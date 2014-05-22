# My first test scipt at Zola books
# Made by Michael Galanin Test Engineer

import urllib 
import urllib2
import json
from service_base.service import Manager

marker = "#################################################################\n######################### COLLECTIONS ################################\n#############################################################"
class v4coll():
	
	def __init__(self, auth_member_id, auth_token, action ):
		global api_url
		self.auth_member_id = auth_member_id
		self.auth_token = auth_token
		self.action = action
		
	def list(self, api_url):
		self.vals = {'auth_member_id' : self.auth_member_id, 
						 'auth_token' : self.auth_token,
						 'action' : self.action }
		manager = Manager(self.vals)
		return manager.request(api_url, "collection/lists")
		
class CollectionTest():
    def __init__(self, api_url, member_id, action, auth_token):
        self.api_url = api_url
        self.auth_member_id = member_id
        self.action = action
        self.auth_token = auth_token

    def list(self):
        a = v4coll(self.auth_member_id, self.auth_token, "get-purchased" )
        print Manager.OKBLUE + marker + Manager.ENDC
	return a.list(self.api_url)
	        		
		


