import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from service_base.service import Manager

marker = "#################################################################\n######################### DETAILS ###############################\n#################################################################"
class Details():
    def __init__(self,member_id,auth_token, isbn):
        self.vals = {"auth_member_id" :  member_id,
                     "auth_token" : auth_token,
                     "isbn" : isbn,
                     "action" : "get"}
    def details(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "book/details")

class DetailsTest():
    def __init__(self, api_url, member_id, auth_token):
        self.api_url = api_url
        self.member_id = member_id
        self.auth_token = auth_token

    def detailsTest(self):
        a = Details(self.member_id, self.auth_token, "9781939126009")
        print Manager.OKBLUE + marker + Manager.ENDC
        return a.details(self.api_url)


