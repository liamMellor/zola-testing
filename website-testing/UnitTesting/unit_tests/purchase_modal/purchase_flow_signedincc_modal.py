'''
Created on Aug 5, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.add_card import add_card
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.bestsellers import bestsellers
from UnitTesting.page_objects.billing_info import billing_info
from UnitTesting.page_objects.find_friends import find_friends

class test_purchase_signedincc(unittest.TestCase):
          
    def purchase_signedincc_modal_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
        
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.click_billing_info()
        
        page_billing_info = billing_info(webd_wrap)
        page_billing_info.click_add_card()
        
        page_add_card = add_card(webd_wrap)
        page_add_card.submit_new_cc_info()
        
        page_billing_info.click_back_to_profile()
        
        page_my_zola.click_sign_out()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        
        page_homepage.click_first_bestseller()
        book_title = page_homepage.book_modal.get_book_title()
        page_homepage.book_modal.click_buy()
        
        page_homepage.purchase_confirm_modal.click_receive_emails()
        page_homepage.purchase_confirm_modal.click_buy()
        page_homepage.purchase_confirm_modal.click_done()
        
        page_homepage.click_my_zola()
        page_my_zola.first_activity_should_be_purchased_book(book_title)
    
        webd_wrap.close_the_browser()
    
    def test_purchase_signedincc_modal(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.purchase_signedincc_modal_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()