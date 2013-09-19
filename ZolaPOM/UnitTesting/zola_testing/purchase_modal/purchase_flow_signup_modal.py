'''
Created on Jul 15, 2013

@author: emma
'''

import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.add_card import add_card
from page_objects.my_zola import my_zola

class test_purchase_signup(unittest.TestCase):
          
    def purchase_signup_modal_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_first_bestseller()
        book_title = page_homepage.book_modal.get_book_title()
        page_homepage.book_modal.click_buy()
        page_homepage.sign_in_modal.click_sign_up()

        page_sign_up = sign_up(webd_wrap)
        page_sign_up.submit_new_member_info()

        page_add_card = add_card(webd_wrap)
        page_add_card.submit_new_cc_info()
        
        page_homepage.purchase_confirm_modal.click_receive_emails()
        page_homepage.purchase_confirm_modal.click_buy()
        page_homepage.purchase_confirm_modal.click_done()
        
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_purchased_book(book_title)
    
        webd_wrap.close_the_browser()
    
    def test_purchase_signup_modal(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.purchase_signup_modal_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()