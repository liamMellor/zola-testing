import urllib
import urllib2
import json
from service_base.service import Manager

sets = "######################### RSS ###############################"

class v4rss():

    def __init__(self):
        global api_url
    
    def rss(self, api_url):
        self.vals = {}
        manager = Manager(self.vals)
        return manager.request(api_url, "content/rss")

class rssTest():

    def __init__(self, api_url):
        self.api_url = api_url
    

    def rss(self):
        testFeed = v4rss()
        print Manager.WARNING + sets + Manager.ENDC
        return testFeed.rss(self.api_url)