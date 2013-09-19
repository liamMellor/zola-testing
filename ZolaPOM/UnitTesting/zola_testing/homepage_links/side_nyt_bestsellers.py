'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage

class side_nyt_bestsellers(unittest.TestCase):
          
    def nyt_bestsellers_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_nyt_bestsellers()
        webd_wrap.check_url('http://www.nytimes.com/best-sellers-books/overview.html')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_nyt_bestsellers(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.nyt_bestsellers_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()