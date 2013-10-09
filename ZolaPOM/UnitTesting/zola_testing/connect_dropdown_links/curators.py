'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.acp_list import acp_list

class connect_curators(unittest.TestCase):
          
    def connect_curators_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.hover_over_connect_dropdown()
        page_homepage.click_on_link("Curators")
        
        page_acp_list = acp_list(webd_wrap)
        page_acp_list.confirm_page("curators")
        webd_wrap.close_the_browser()
        
        
    
    def test_connect_curators(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.connect_curators_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()