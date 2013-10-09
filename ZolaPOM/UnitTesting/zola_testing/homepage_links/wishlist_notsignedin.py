'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.your_collection import your_collection

class wishlist_notsignedin(unittest.TestCase):
          
    def wishlist_notsignedin_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()

        page_homepage.click_wishlist()
        page_homepage.sign_in_modal.sign_in()
        
        page_your_collection = your_collection(webd_wrap)
        page_your_collection.confirm_filter_selected('wishlist')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_wishlist_notsignedin(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.wishlist_notsignedin_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()