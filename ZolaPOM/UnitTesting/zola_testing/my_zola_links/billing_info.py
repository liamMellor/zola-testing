'''
Created on Jul 17, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.my_zola import my_zola

class my_zola_billing_info(unittest.TestCase):
          
    def billing_info_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.click_billing_info()
        
        webd_wrap.check_url('https://zolaqc.com/profile/billing')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_billing_info(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.billing_info_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()