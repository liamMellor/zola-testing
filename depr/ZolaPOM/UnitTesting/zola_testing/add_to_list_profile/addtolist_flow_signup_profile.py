'''
Created on Jul 15, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.add_card import add_card
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.book import book

class addtolist_flow_signup_test(unittest.TestCase):
          
    def add_to_list_signup_modal_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()

        page_homepage.click_first_bestseller()
        title = page_homepage.book_modal.get_book_title()
        page_homepage.book_modal.click_full_profile()
        
        page_book = book(webd_wrap)
        page_book.click_add_to_list()
        page_book.sign_in_modal.click_sign_up()  
        
        page_sign_up = sign_up(webd_wrap)
        page_sign_up.submit_new_member_info()
        
        page_book.choose_wishlist()
        page_book.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_added_book(title)
    
        webd_wrap.close_the_browser()
    
    def test_addtolist_signup_modal(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.add_to_list_signup_modal_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()