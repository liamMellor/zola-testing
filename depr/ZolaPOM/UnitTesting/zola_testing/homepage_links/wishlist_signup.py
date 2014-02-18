'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.your_collection import your_collection

import time 

class wishlist_signup(unittest.TestCase):
          
    def wishlist_signup_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()

        page_homepage.click_wishlist()
        page_homepage.sign_in_modal.click_sign_up()
        
        page_sign_up = sign_up(webd_wrap)
        page_sign_up.submit_new_member_info()
        
        time.sleep(3)
        page_your_collection = your_collection(webd_wrap)
        page_your_collection.confirm_filter_selected('wishlist')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_wishlist_signup(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.wishlist_signup_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()