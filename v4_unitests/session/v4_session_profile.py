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

class V4_profile():
    def __init__(self, auth_member_id ,auth_token, setter=True, email="",member_public_email="",member_first_name="",member_last_name="",bday_d="",bday_m="",bday_y="",member_gender="",member_zip_code="",member_location="",member_phone="",member_url="",member_facebook_url="",member_facebook_username="",member_facebook_id="",member_twitter_url="",member_twitter_username="",member_gplus_url="",member_gplus_username="",receive_newsletter="",receive_email_if_followed="",receive_email_if_messaged="" ):
        global api_url
        
        self.auth_member_id = auth_member_id
        self.auth_token = auth_token
        
        self.setter = setter
        if setter is True:
             self.email = email
             self.member_public_email = member_public_email
             self.member_first_name = member_first_name
             self.member_last_name = member_last_name
             self.bday_d = bday_d
             self.bday_m = bday_m
             self.bday_y = bday_y
             self.member_gender = member_gender
             self.member_zip_code = member_zip_code
             self.member_location = member_location
             self.member_phone = member_phone
             self.member_url = member_url
             self.member_facebook_url = member_facebook_url
             self.member_facebook_username = member_facebook_username
             self.member_facebook_id = member_facebook_id
             self.member_twitter_url = member_twitter_url
             self.member_twitter_username = member_twitter_username
             self.member_gplus_url = member_gplus_url
             self.member_gplus_username = member_gplus_username
             self.receive_newsletter = receive_newsletter
             self.receive_email_if_followed = receive_email_if_followed
             self.receive_email_if_messaged = receive_email_if_messaged
    
    def profile(self, api_url):
        profileUrl = api_url + 'session/profile'
        if self.setter is True:
            profileValues = {'auth_member_id' : self.auth_member_id,
                             'auth_token' : self.auth_token,
                             'action' : 'set',
                             'email' : self.email,
                             'member_public_email' : self.member_public_email,
                             'member_first_name' : self.member_first_name,
                             'member_last_name' : self.member_last_name,
                             'bday_d' : self.bday_d,
                             'bday_m' : self.bday_m,
                             'bday_y' : self.bday_y,
                             'member_gender' : self.member_gender,
                             'member_zip_code' : self.member_zip_code,
                             'member_location' : self.member_location,
                             'member_phone' : self.member_phone,
                             'member_url' : self.member_url,
                             'member_facebook_url': self.member_facebook_url,
                             'member_facebook_username': self.member_facebook_username,
                             'member_facebook_id' : self.member_facebook_id,
                             'member_twitter_url': self.member_twitter_url,
                             'member_twitter_username' : self.member_twitter_username,
                             'member_gplus_url' : self.member_gplus_url,
                             'member_gplus_username':  self.member_gplus_username,
                             'receive_newsletter' :self.receive_newsletter,
                             'receive_email_if_followed' : self.receive_email_if_followed,
                             'receive_email_if_messaged' : self.receive_email_if_messaged}
        else:
            
            profileValues = {'auth_member_id' : self.auth_member_id,
                             'auth_token' : self.auth_token,
                             'action' : 'get'}
        profileData = urllib.urlencode(profileValues)
        profileReq = urllib2.Request(profileUrl,profileData)
        profileResponse = urllib2.urlopen(profileReq)
        profileJSON = json.load(profileResponse)
        return profileJSON["data"]

login = V4_login('jason-flax-2','kingkong','python','jay.flax@zolabooks.com')
creds = login.login(api_url)
mem_id =  creds["member_id"]

pGet = V4_profile( str(mem_id), creds["auth_token"], False)

print pGet.profile(api_url)

pSet = V4_profile( str(mem_id), creds["auth_token"], True, 'jay.flax@zolabooks.com','publicbobo@email.com','mrbobo','jangles','11','11','1982','female','11201','kentucky','631-506-8330','MemberUrl','fbMemberurl','facebookUsername','boboFacebookId','newTwitterUrl','twitterUsername','gPlusUrl','gplusUsername','True','True','False')

print pSet.profile(api_url)

print pGet.profile(api_url)
