'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.user_profile import user_profile

class user_in_feed(unittest.TestCase):
          
    def user_in_feed_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_first_user_in_feed()
        
        page_user_profile = user_profile(webd_wrap)
        page_user_profile.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_user_in_feed(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.user_in_feed_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()