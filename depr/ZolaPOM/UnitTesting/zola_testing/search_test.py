'''
Created on Jun 18, 2013

@author: jsflax
'''

import sys
sys.path.append("page_objects")

import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.add_card import add_card

class test_search(unittest.TestCase):
          
    def individual_search_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.perform_search("john irving")
    
        webd_wrap.close_the_browser()
    
    def test_search(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.individual_search_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()
  
        
