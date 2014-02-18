'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.find_friends import find_friends

class side_feed_signup(unittest.TestCase):
          
    def feed_signup_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_the_feed()
        page_homepage.sign_in_modal.click_sign_up()
        
        page_sign_up = sign_up(webd_wrap)
        page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
        
        page_homepage.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_feed_signup(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.feed_signup_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()