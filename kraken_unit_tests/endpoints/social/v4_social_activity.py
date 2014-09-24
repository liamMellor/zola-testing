import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from service_base.service import Manager
import arg_manager


marker = "######################################################################\n############################# SOCIAL #################################\n######################################################################"
sets = "######################### ACTIVITY/SETS ##############################"
gets = "######################### ACTIVITY/GETS ##############################"
rems = "######################### ACTIVITY/REMOVE ############################"
mess = "###################### ACTIVITY/SEND_MESSAGE #########################"

class Activity():

    def __init__(self, auth_member_id, auth_token, action, type=None, isbn=None, member_id=None, note=None, highlighted_text=None, current_char=None, start_char=None, end_char=None, reading_duration=None, rating=None, notation_id=None, in_reply_to=None, page_number=None, since=None, limit=None, offset=None, is_spoiler=None, share_with_followers=None, share_member_ids=None, share_emails=None):
    
        self.vals = { "auth_member_id": auth_member_id,
                      "auth_token": auth_token,
                      "isbn" : isbn,
                      "action": action }
        if action == "set":
            self.vals["type"] = type
            if type is "highlight" or type is "notation":
                self.vals["note"] = note
                self.vals["highlighted_text"] = highlighted_text
                self.vals["current_char"] = start_char
                self.vals["end_char"] = end_char
                self.vals["page_number"] = page_number
                self.vals["is_spoiler"] = is_spoiler
                self.vals["share_with_followers"] = share_with_followers
            elif type is "progress":
                self.vals["current_char"] = current_char
                self.vals["page_number"] = page_number
                self.vals["reading_duration"] = reading_duration
            elif type is "reply":
                self.vals["note"] = note
                self.vals["in_reply_to"] = in_reply_to
            elif type is "rating":
                self.vals["rating"] = rating
            elif type is "bookmark":
            	self.vals["page_number"] = page_number
            elif type is "notation":
            	self.vals["notation_id"] = notation_id
            elif type is "note":
            	self.vals["note"] = note

        elif action == "get":
            self.vals["type"]= type
            if type is "notation" or type is "reply":
                self.vals["notation_id"] = notation_id
                
        elif action == "remove":
            self.vals["type"] = type
            self.vals["notation_id"] = notation_id
        	
        elif action == "send-message":
            self.vals["member_id"] = member_id
            self.vals["note"] = note


    def activate(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "social/activity")

class ActivityTest():
    def __init__(self, api_url, member_id, auth_token):
        self.api_url = api_url
        self.member_id = member_id
        self.auth_token = auth_token
        
    def activityTest(self):
        print Manager.OKBLUE + marker + Manager.ENDC

		
        ########## BEGIN SETS ###########
        print Manager.WARNING + sets + Manager.ENDC

        a = Activity(self.member_id, self.auth_token, "set", "highlight", "9780525478812", None, "meow", "woofy woofkins went dookie", None, "10000", "10020", None, None, None, "67", "47", 0, 25, 0, "yes", "yes", "yes")
        value = a.activate(self.api_url)
        data  = value[1]['data']
        id1   = data['notation_id']

        b = Activity(self.member_id, self.auth_token, "set", "progress", "9781101569184",current_char="10", page_number="7", reading_duration="100")
        b.activate(self.api_url)
    
        c = Activity(self.member_id, self.auth_token, "set", "rating", "9780525478812",rating="4")
        c.activate(self.api_url)

        d     = Activity(self.member_id, self.auth_token, "set", "reply", "9780525478812", note="boo", in_reply_to="7226")
        value = d.activate(self.api_url)
        data  = value[1]['data']
        id2   = data['notation_id']
        
        e     = Activity(self.member_id, self.auth_token, "set", "bookmark", "9780525478812", page_number="2")
        value = e.activate(self.api_url)
        data  = value[1]['data']
        id3   = data['notation_id']
        
        f     = Activity(self.member_id, self.auth_token, "set", "note", "9780525478812", note="Liam is cool")
        value = f.activate(self.api_url)
        data  = value[1]['data']
        id4   = data['notation_id']
        
        h     = Activity(self.member_id, self.auth_token, "set", "note", "9780525478812", note="Liam is cool yup")
        value = h.activate(self.api_url)
        data  = value[1]['data']
        id5   = data['notation_id']
        
        i = Activity(self.member_id, self.auth_token, "set", "abandonded", "9780525478812")
        i.activate(self.api_url)
        
        
        ########## BEGIN GETS ###########
        print Manager.WARNING + gets + Manager.ENDC

        a      = Activity(self.member_id, self.auth_token, "get", "notation", "9780525478812")
        printA = a.activate(self.api_url)[0]
        if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR NOTATION ACTIVITY:"
            print "\n"
            print printA
        
        b      = Activity(self.member_id, self.auth_token, "get", "rating", "9780525478812")
        printB = b.activate(self.api_url)
        if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR RATING ACTIVITY:"
            print "\n"
            print printB
        
        c      = Activity(self.member_id, self.auth_token, "get", "progress", "9781101569184")
        printC = c.activate(self.api_url)
        if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR PROGRESS ACTIVITY:"
            print "\n"
            print printC

        d      = Activity(self.member_id, self.auth_token, "get", "reply", "9780525478812")
        printD = d.activate(self.api_url)
        if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR REPLY ACTIVITY:"
            print "\n"
            print printD

        e      = Activity(self.member_id, self.auth_token, "get", "notation", "9780525478812")
        printE = e.activate(self.api_url)
        if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR NOTATION ACTIVITY:"
            print "\n"
            print printE
            
    	f      = Activity(self.member_id, self.auth_token, "get", "bookmark", "9780525478812")
    	printF = f.activate(self.api_url)
    	if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR bookmark ACTIVITY:"
            print "\n"
            print printF
            
        g      = Activity(self.member_id, self.auth_token, "get", "highlight", "9780525478812")
        printG = g.activate(self.api_url)
    	if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR highlight ACTIVITY:"
            print "\n"
            print printG
            
        h      = Activity(self.member_id, self.auth_token, "get", "note", "9780525478812")
        printH = h.activate(self.api_url)
    	if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR highlight ACTIVITY:"
            print "\n"
            print printH  
            
    	i      =  Activity(self.member_id, self.auth_token, "get", "abandonded", "9780525478812")
        printI = i.activate(self.api_url)
    	if arg_manager.verboseHigh == True:
            print "\n"
            print "BELOW IS JSON RETURNED GET FOR abandonded ACTIVITY:"
            print "\n"
            print printI    
        
        
        ########## BEGIN Removes ###########
    	print Manager.WARNING + rems + Manager.ENDC
    	
    	a = Activity(self.member_id, self.auth_token, "remove", "bookmark", "9781939126009", notation_id=id3)
    	a.activate(self.api_url)
    	
    	b = Activity(self.member_id, self.auth_token, "remove", "highlight", "9781939126009", notation_id=id1)
    	b.activate(self.api_url)
    	
    	c = Activity(self.member_id, self.auth_token, "remove", "note", "9781939126009", notation_id=id4)
    	c.activate(self.api_url)
    	
    	d = Activity(self.member_id, self.auth_token, "remove", "reply", "9781939126009", notation_id=id2)
    	d.activate(self.api_url)
    	
    	e = Activity(self.member_id, self.auth_token, "remove", "notation", "9781939126009", notation_id=id5)
    	e.activate(self.api_url)
    	
    	
    	########## Begin Send Message #####
    	print Manager.WARNING + mess + Manager.ENDC
    	
    	a = Activity(self.member_id, self.auth_token, "send-message", member_id="12", note="Yeah whoop")
    	a.activate(self.api_url) 

    	
    	
    	
    	
    	
    	
    	
    	
    	
