import urllib
import urllib2
import json
import random
import string
import re
import time
import os
import datetime
import time
import hashlib
import arg_manager

class Manager():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    TIMEPURP = '\033[35m'
    TIMEBLOCK = "### TIME ###\n"
    
    def __init__(self, value_dict):
        self.value_dict = value_dict
        sig = hashlib.md5('8gwb5ozh7cy6tyturnbtyipe' + 'we6jgopi6axv' + str(int(time.time()))).hexdigest()
        self.value_dict['key'] = '8gwb5ozh7cy6tyturnbtyipe'
        self.value_dict['signature'] = sig
    
    
    def request(self, api_url, endpoint):
        url = api_url + endpoint
        data = urllib.urlencode(self.value_dict)
        if arg_manager.verboseLow == True or arg_manager.verboseHigh == True:
            print "The url request = " + url + "?" + data
        req = urllib2.Request(url, data)
        response = None
        code = None
        clock1 = datetime.datetime.now()
        clock2 = datetime.datetime.now()
        try:
            
            clock1 = datetime.datetime.now()
            response = urllib2.urlopen(req)
            clock2 = datetime.datetime.now()
            s = [response.getcode(), json.load(response)]
            
            # Slice out "action" from endpoint to use in information print out
            word  = "action="
            text  = data
            match = re.search(word, text)
            start = 0
            valueError = False
            if match == None:
                valueError = True
            else:
                start = match.start()
            
            # If JSONdump flag is enabled
            if arg_manager.JSONdump == True:
                print self.dump(s)
            
            # If there's a system error print out in RED
            if s[1]["status"] == "system_error":
                if valueError == True:
                    print Manager.FAIL + s[1]["status"] + Manager.ENDC + "          " + endpoint
                    return Manager.FAIL + self.dump(s) + Manager.ENDC
                else:
                    print Manager.FAIL + s[1]["status"] + Manager.ENDC + "          " + endpoint + " " + data[start:]
                    return Manager.FAIL + self.dump(s) + Manager.ENDC

            # Else we were successful
            if valueError == True:
                print Manager.OKGREEN + s[1]["status"] + Manager.ENDC + "          " + endpoint
                return [Manager.OKGREEN + self.dump(s) + Manager.ENDC, s[1]]
            else:
                print Manager.OKGREEN + s[1]["status"] + Manager.ENDC + "          " + endpoint + " " + data[start:]
                return [Manager.OKGREEN + self.dump(s) + Manager.ENDC, s[1]]
          
        # Catch HTTP exceptions
        except urllib2.HTTPError as e:
            s = [e, e.read()]
            print  Manager.FAIL + "fail " + "            " + str(s) + Manager.ENDC
            return Manager.FAIL + self.dump(s) + Manager.ENDC
        finally:
            timeattack = clock2 - clock1
            if arg_manager.verboseHigh == True:
                print Manager.TIMEPURP + Manager.TIMEBLOCK + str(timeattack) + Manager.ENDC


    def dump(self, s):
        if len(s) > 1:
            return json.dumps(s[1], indent=4, sort_keys=False)
        else: 
            return s

    # ****** Function for purposeful failure calls ***********************************************
    def requestFail(self, api_url, endpoint, message):
        url = api_url + endpoint
        data = urllib.urlencode(self.value_dict)
        if arg_manager.verboseLow == True or arg_manager.verboseHigh == True:
            print "The url request = " + url + "?" + data
        req = urllib2.Request(url, data)
        response = None
        code = None
        clock1 = datetime.datetime.now()
        clock2 = datetime.datetime.now()
        try:
        
            clock1 = datetime.datetime.now()
            response = urllib2.urlopen(req)
            clock2 = datetime.datetime.now()
            s = [response.getcode(), json.load(response)]
        
            # Slice out "action" from endpoint to use in information print out
            word  = "action="
            text  = data
            match = re.search(word, text)
            start = 0
            valueError = False
            if match == None:
                valueError = True
            else:
                start = match.start()
        
            # If JSONdump flag is enabled
            if arg_manager.JSONdump == True:
                print self.dump(s)
        
            # If there's a system error print out in RED
            if s[1]["status"] == "system_error":
                if valueError == True:
                    print Manager.FAIL + s[1]["status"] + " System Error on back-end." + Manager.ENDC + "          " + endpoint
                    return Manager.FAIL + self.dump(s) + Manager.ENDC
                else:
                    print Manager.FAIL + s[1]["status"] + " System Error on back-end." + Manager.ENDC + "          " + endpoint + " " + data[start:]
                    return Manager.FAIL + self.dump(s) + Manager.ENDC
        
            # This function handles purposeful incorrect calls so "success" status is a failure in this case
            if valueError == True:
                print Manager.FAIL + s[1]["status"] + " ***Should have failed here." + Manager.ENDC + "          " + endpoint
                return [Manager.FAIL + self.dump(s) + Manager.ENDC, s[1]]
            else:
                print Manager.FAIL + s[1]["status"] + " ***Should have failed here." + Manager.ENDC + "          " + endpoint + " " + data[start:]
                return [Manager.FAIL + self.dump(s) + Manager.ENDC, s[1]]
    
        # Catch HTTP exceptions.  Return 'success' because we are purposefully making errors.
        except urllib2.HTTPError as e:
            s = e.read()
            word   = "data"
            word2  = "}"
            match  = re.search(word, s)
            match2 = re.search(word2, s)
            start  = match.start()
            start  = start + 6
            end    = match2.start()
            print  Manager.OKGREEN + "success " + Manager.ENDC + Manager.WARNING + "(catch)  " + Manager.ENDC + endpoint + " " + message + " " + str(s[start:end])
        finally:
            timeattack = clock2 - clock1
            if arg_manager.verboseHigh == True:
                print Manager.TIMEPURP + Manager.TIMEBLOCK + str(timeattack) + Manager.ENDC
