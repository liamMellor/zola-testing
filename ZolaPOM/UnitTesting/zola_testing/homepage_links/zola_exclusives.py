'''
Created on Aug 6, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.find_friends import find_friends

class zola_exclusives(unittest.TestCase):
          
    def zola_exclusives_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_zola_exclusives()
        
        webd_wrap.check_url('https://zolabooks.com/profile/zolabooks')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_zola_exclusives(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.zola_exclusives_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()