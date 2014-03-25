import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from service_base.service import Manager

class Activity():
    def __init__(self, auth_member_id, auth_token, action, type=None, isbn=None, member_id=None, note=None, highlighted_text=None, current_char=None, start_char=None, end_char=None, reading_duration=None, rating=None, notation_id=None, in_reply_to=None, page_number=None, since=None, limit=None, offset=None, is_spoiler=None, share_with_followers=None, share_member_ids=None, share_emails=None):
        self.vals = { "auth_member_id": auth_member_id,
                      "auth_token": auth_token,
                      "isbn" : isbn,
                      "action": action }
        if action == "set":
            self.vals["type"] = type
            if type == "highlight" or "notation":
                self.vals["note"] = note
                self.vals["highlighted_text"] = highlighted_text
                self.vals["start_char"] = start_char
                self.vals["end_char"] = end_char
                self.vals["page_number"] = page_number
                self.vals["is_spoiler"] = is_spoiler
                self.vals["share_with_followers"] = share_with_followers
            elif type == "progress":
                self.vals["current_char"] = current_char
                self.vals["page_number"] = page_number
                self.vals["reading_duration"] = reading_duration
            elif type == "rating":
                self.vals["rating"] = rating
        elif action == "get":
            self.vals["type"]= type
            if type == "notation":
                print 'meow'
    def activate(self, api_url):
        print self.vals
        manager = Manager(self.vals)
        return manager.request(api_url, "social/activity")

class Activate():
    def __init__(self, api_url, member_id, auth_token):
        self.api_url = api_url
        self.member_id = member_id
        self.auth_token = auth_token
        
    def activityTest(self):
        a = Activity(self.member_id, self.auth_token, "set", "notation", "9781939126009", None, "meow", "woofy woofkins went dookie", None, "10000", "10020", None, None, None, "67", "47", 0, 25, 0, "yes", "yes", "yes")
        print self.dump(a.activate(self.api_url))
    
    def dump(self, s):
        if len(s) > 1: return json.dumps(s[1], indent=4, sort_keys=False)
        else: return s