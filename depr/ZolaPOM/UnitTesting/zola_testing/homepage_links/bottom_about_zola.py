'''
Created on Jul 16, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage

class bottom_about_zola(unittest.TestCase):
          
    def bottom_about_zola_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_bottom_about_zola()
        webd_wrap.check_url('http://news.zolabooks.com/welcome-to-zola-the-future-of-ebooks/#more-188')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_bottom_about_zola(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.bottom_about_zola_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()