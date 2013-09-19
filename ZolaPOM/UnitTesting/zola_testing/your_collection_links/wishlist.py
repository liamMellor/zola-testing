'''
Created on Jul 22, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.my_ebooks import my_ebooks
from page_objects.your_collection import your_collection

class wishlist(unittest.TestCase):
          
    def wishlist_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_ebooks()
        
        page_my_ebooks = my_ebooks(webd_wrap)
        page_my_ebooks.click_all_books_see_all()
        
        webd_wrap.check_url('https://zolaqc.com/collection/list/all_results/') 
        
        page_your_collection = your_collection(webd_wrap)
        page_your_collection.click_wishlist()
        
        webd_wrap.check_url('https://zolaqc.com/collection/list/wishlist/')
        webd_wrap.close_the_browser()
        
        
    
    def test_wishlist(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.wishlist_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()