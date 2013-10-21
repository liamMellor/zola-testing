'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.new_releases import new_releases

class see_all_nonfiction_new_releases(unittest.TestCase):
          
    def see_all_nonfiction_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_see_all_non_fiction()
        
        page_new_releases = new_releases(webd_wrap)
        page_new_releases.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_see_all_nonfiction(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.see_all_nonfiction_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()