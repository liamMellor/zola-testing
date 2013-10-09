'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.list import list

class navigation_deals(unittest.TestCase):
          
    def deals_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_deals()
        
        page_list = list(webd_wrap)
        page_list.confirm_daily_deals()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_deals(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.deals_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()