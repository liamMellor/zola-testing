'''
Created on Jul 15, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.modals.book_modal import book_modal
from UnitTesting.page_objects.modals.sign_in_modal import sign_in_modal
from UnitTesting.page_objects.modals.purchase_confirm_modal import purchase_confirm_modal
from UnitTesting.page_objects.bestsellers import bestsellers
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.add_card import add_card
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.book import book
from UnitTesting.page_objects.find_friends import find_friends

class test_purchase_notsignedin(unittest.TestCase):
          
    def purchase_notsignedin_profile_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_bestsellers = bestsellers(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
        
        page_homepage.click_sign_out()
        page_homepage.click_bestsellers()
        page_bestsellers.click_first_book()
        
        book = book_modal(webd_wrap)
        sign_in = sign_in_modal(webd_wrap)
        book.click_buy()
        sign_in.sign_in(email, 'password')
        
        page_add_card = add_card(webd_wrap)
        page_add_card.submit_new_cc_info()
        
        purchase_confirm = purchase_confirm_modal(webd_wrap)
        purchase_confirm.click_receive_emails()
        purchase_confirm.click_buy()
        purchase_confirm.click_done()
        
    
        webd_wrap.close_the_browser()
    
    def test_purchase_notsignedin_profile(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.purchase_notsignedin_profile_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()