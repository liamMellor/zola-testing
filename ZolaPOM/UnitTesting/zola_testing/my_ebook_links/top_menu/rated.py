'''
Created on Jul 22, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.my_ebooks import my_ebooks

class top_rated(unittest.TestCase):
          
    def top_rated_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_ebooks()
        
        page_my_ebooks = my_ebooks(webd_wrap)
        page_my_ebooks.click_rated()
        
        webd_wrap.check_url('https://zolaqc.com/collection/list/all_rated/')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_top_rated(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.top_rated_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()