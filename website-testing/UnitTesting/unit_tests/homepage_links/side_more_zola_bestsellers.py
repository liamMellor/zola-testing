'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.bestsellers import bestsellers

class side_more_zola_bestsellers(unittest.TestCase):
          
    def more_zola_bestsellers_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_more_zola_bestsellers()
        
        page_bestsellers = bestsellers(webd_wrap)
        page_bestsellers.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_more_zola_bestsellers(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.more_zola_bestsellers_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()