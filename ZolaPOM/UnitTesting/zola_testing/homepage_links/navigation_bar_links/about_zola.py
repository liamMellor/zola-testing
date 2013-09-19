'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage

class navigation_about_zola(unittest.TestCase):
          
    def about_zola_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_about_zola()
        webd_wrap.check_url('http://news.zolabooks.com/tag/new-publisher')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_about_zola(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.about_zola_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()