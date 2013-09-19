'''
Created on Jul 16, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage

class bottom_news(unittest.TestCase):
          
    def bottom_news_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_news()
        webd_wrap.check_url('http://news.zolabooks.com/')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_bottom_news(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.bottom_news_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()
