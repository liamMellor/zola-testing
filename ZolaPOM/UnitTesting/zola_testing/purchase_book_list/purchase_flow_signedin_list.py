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
from UnitTesting.page_objects.bestsellers import bestsellers
from UnitTesting.page_objects.find_friends import find_friends

class test_purchase_signedin(unittest.TestCase):
          
    def purchase_signedin_list_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
        
        page_homepage.click_sign_out()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        
        page_homepage.click_bestsellers()
        
        page_bestsellers = bestsellers(webd_wrap)
        book_title = page_bestsellers.get_eighth_book_title()
        page_bestsellers.click_buy_eighth_book()

        page_add_card = add_card(webd_wrap)
        page_add_card.submit_new_cc_info()
        
        page_bestsellers.purchase_confirm_modal.click_receive_emails()
        page_bestsellers.purchase_confirm_modal.click_buy()
        page_bestsellers.purchase_confirm_modal.click_done()
        
        page_bestsellers.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_purchased_book(book_title)
    
        webd_wrap.close_the_browser()
    
    def test_purchase_signedin_list(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.purchase_signedin_list_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()