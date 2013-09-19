'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.bestsellers import bestsellers

class navigation_bestsellers(unittest.TestCase):
          
    def bestsellers_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_bestsellers()
        
        page_bestsellers = bestsellers(webd_wrap)
        page_bestsellers.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_bestsellers(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.bestsellers_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()