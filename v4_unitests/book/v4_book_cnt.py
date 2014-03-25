import urllib
import urllib2
import json
import random
import string
import re
import time
import os

#api_url = 'https://api.api-v4.divergence.zolaqc.com/v4/'                                                                                                                                        


class V4_books_cnt():
    def __init__(self,member_id,auth_token,action,isbn):
        global api_url
        self.member_id = member_id
        self.auth_token = auth_token
        self.action = action
        self.isbn = isbn

    def count(self, api_url):
        loginUrl = api_url + 'book/cnt'
        loginValues = {'auth_member_id' : self.member_id,
                       'auth_token' : self.auth_token,
                       'action' : self.action,
                       'isbn' : self.isbn}
        loginData = urllib.urlencode(loginValues)
        loginReq = urllib2.Request(loginUrl,loginData)
        loginResponse = urllib2.urlopen(loginReq)
        loginJSON = json.load(loginResponse)
        loginContainer = {}
        print loginJSON
