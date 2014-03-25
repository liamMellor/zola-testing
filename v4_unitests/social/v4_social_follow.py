import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from service_base.service import Manager

class Follow():
    def __init__(self, auth_member_id, auth_token, action, member_id = None):
        self.vals = { "auth_member_id": auth_member_id,
                      "auth_token": auth_token,
                      "action": action }
        if action == "start-following" or "unfollow":
            self.vals["member_id"] = member_id
        
    def follow(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "social/follow")
