import urllib
import urllib2
import json
import random
import string
import re
import time
import os

api_url = 'https://zolaqc.com/api/v4/'


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

class V4_details():
    def __init__(self,member_id,auth_token, isbn):
        self.member_id = member_id
        self.auth_token = auth_token
        self.isbn = isbn
    def details(self, api_url):
        detailsUrl = api_url + 'book/details'
        detailsValues = {'auth_member_id' : self.member_id,
                         'auth_token' : self.auth_token,
                         'action' : 'get-min',
                         'isbn' : self.isbn}
        detailsData = urllib.urlencode(detailsValues)
        detailsReq = urllib2.Request(detailsUrl,detailsData)
        detailsResponse = urllib2.urlopen(detailsReq)
        detailsJSON = json.load(detailsResponse)
        detailsContainer = {}
        print detailsJSON
        for x,y in detailsJSON["data"].iteritems():
            detailsContainer[x] = y
            return detailsContainer

class V4_avatar():
    def __init__(self,member_id,auth_token):
        self.member_id = member_id
        self.auth_token = auth_token

    def avatar(self, api_url):
        avUrl = api_url + 'session/avatar'
        avValues = {'auth_member_id' : self.member_id,
                    'auth_token' : self.auth_token,
                    'action' : 'set'}
        avData = urllib.urlencode(avValues)
        avReq = urllib2.Request(avUrl,avData)
        avResponse = urllib2.urlopen(avReq)
        avJSON = json.load(avResponse)
        print avJSON

login = V4_login('jason-flax-2','kingkong','python','jay.flax@zolabooks.com')
creds = login.login(api_url)
mem_id = creds["member_id"]

auth_token = creds["auth_token"]
details = V4_details(str(mem_id),auth_token,"2965334482104")
print details.details(api_url)
