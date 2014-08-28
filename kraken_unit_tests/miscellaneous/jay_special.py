import urllib
import urllib2
import json
import random
import string
import re
import time
import os

api_url = 'https://api.zolabooks.com/v2/'                                                                                                                                                   


class V4_login():
    def __init__(self,username,password,device_name):
        global api_url
        self.username = username
        self.password = password
        self.device_name = device_name
        
    def login(self, api_url):
        loginUrl = api_url + 'device/login'
        loginValues = {'username' : self.username,
                       'password' : self.password,
                       'device_name' : self.device_name}
        loginData = urllib.urlencode(loginValues)
        loginReq = urllib2.Request(loginUrl,loginData)
        loginResponse = urllib2.urlopen(loginReq)
        loginJSON = json.load(loginResponse)
        loginContainer = {}
        for x,y in loginJSON["data"].iteritems():
            loginContainer[x] = y
        return loginContainer

class V2_get_followers():
    def __init__(self,member_id,auth_member_id,auth_token):
        global api_url
        self.member_id = member_id
        self.auth_member_id = auth_member_id
        self.auth_token = auth_token

    def get_followers(self, api_url):
        gfUrl = api_url + 'follow/get_followers'
        gfValues = {'member_id' : self.member_id,
                    'auth_member_id' : self.auth_member_id,
                    'auth_token' : self.auth_token}
        gfData = urllib.urlencode(gfValues)
        gfReq = urllib2.Request(gfUrl+"?"+gfData)
        gfResponse = urllib2.urlopen(gfReq)
        gfJSON = json.load(gfResponse)
        return gfJSON["data"]
        gfContainer = {}
        for x,y in gfJSON["data"].iteritems():
            gfContainer[x] = y
            return gfContainer
                             
class V2_set_unfollow():
    def __init__(self,member_id,auth_member_id,auth_token):
        global api_url
        self.member_id = member_id
        self.auth_member_id = auth_member_id
        self.auth_token = auth_token

    def set_unfollow(self, api_url):
        gfUrl = api_url + 'follow/set_unfollow'
        gfValues = {'follower' : self.member_id,
                    'followee' : '87277',
                    'auth_member_id' : self.auth_member_id,
                    'auth_token' : self.auth_token}
        gfData = urllib.urlencode(gfValues)
        gfReq = urllib2.Request(gfUrl,gfData)
        gfResponse = urllib2.urlopen(gfReq)
        gfJSON = json.load(gfResponse)
        return gfJSON["data"]
        

init_login = V4_login("jason-flax-2","kingkong","swagcity")
init_creds = init_login.login(api_url)

init_get_followers = V2_get_followers("87277", init_creds["member_id"], init_creds["auth_token"])
init_players = init_get_followers.get_followers(api_url)
player_container = []
for dat in init_players:
    sn = dat["screen_name"]
    un = dat["username"]
    mi = dat["member_id"]
    if sn == "Lin Robinson":
        player_container.append(str(un))

for player in player_container:
    player_login = V4_login(player, "password", "spacecats")
    player_creds = player_login.login(api_url)
    player_unfollow = V2_set_unfollow(player_creds["member_id"], player_creds["member_id"], player_creds["auth_token"])
    print player_unfollow.set_unfollow(api_url)
