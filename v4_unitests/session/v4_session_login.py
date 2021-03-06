import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from service_base.service import Manager

marker = "#################################################################\n######################### SESSION ##############################\n#################################################################"
sets = "######################### LOGIN ##############################"

class v4_login():
    def __init__(self, username, password, device):
        self.vals = {"username":username,"password":password,"device_name":device}
        
    def login(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url,"session/login")

class LoginTest():
    def __init__(self, api_url):
        self.api_url = api_url
        
    def activate(self):
        print Manager.OKBLUE + marker + Manager.ENDC
        
        print Manager.WARNING + sets + Manager.ENDC

        a = v4_login("jason-flax-2","kingkong","awesomefuckingbot")
        return a.login(self.api_url)