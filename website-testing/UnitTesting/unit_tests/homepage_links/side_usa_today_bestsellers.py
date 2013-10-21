'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage

class side_usa_today_bestsellers(unittest.TestCase):
          
    def usa_today_bestsellers_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_usa_today_bestsellers()
        webd_wrap.check_url('http://www.usatoday.com/life/books/best-selling/')
        
        
        webd_wrap.close_the_browser()
        
        
    
    def test_usa_today_bestsellers(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.usa_today_bestsellers_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()