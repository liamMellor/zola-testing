import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from subprocess import Popen, PIPE
import subprocess

api_url = 'https://utest-api-correction.divergence.zolaqc.com/api/v2/'
#base_url = 'https://zolaqc.com/'                                                                                                                                                                           
base_url = 'http://localhost/'
auth_url = re.sub(r'(https?://)(.*)', r'\1zola_stage:zola123@\2', base_url)

def deviceLogin():
    loginUrl = api_url + 'device/login'

    loginValues = {'username' : 'jason-flax-2',
                   'password' : 'kingkong',
                   'device_name' : 'swagger' }

    loginData = urllib.urlencode(loginValues)
    loginReq = urllib2.Request(loginUrl, loginData)
    loginResponse = urllib2.urlopen(loginReq)
    auth_creds = json.load(loginResponse)
    print 'DEVICE LOGIN : ' , auth_creds
    return(auth_creds)

def deviceForgotPassword(auth_creds):
    fpUrl = api_url + 'device/forgot_password'

    fpValues = {'email' : 'jsflax@gmail.com',
                   'auth_member_id' :  auth_creds["data"]["member_id"],
                   'auth_token' : auth_creds["data"]["auth_token"] }

    fpData = urllib.urlencode(fpValues)
    fpReq = urllib2.Request(fpUrl, fpData)
    fpResponse = urllib2.urlopen(fpReq)
    fpOutput = json.load(fpResponse)
    print 'FORGOT PASSWORD : ' , fpOutput
    return(fpOutput)

login = deviceLogin()
deviceForgotPassword(login)

