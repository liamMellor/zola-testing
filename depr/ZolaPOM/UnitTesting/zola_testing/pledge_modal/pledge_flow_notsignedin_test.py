'''
Created on Jul 10, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.find_friends import find_friends
from UnitTesting.page_objects.booksellers import booksellers

#from page_objects.modals.recommend_modal import recommend_modal

class test_pledge_flow_notsignedin_modal(unittest.TestCase):
          
    def pledge_flow_notsignedin_modal_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
         
        page_homepage.click_sign_out()
        page_homepage.hover_over_connect_dropdown()
        page_homepage.click_on_link("Booksellers")
        
        page_booksellers = booksellers(webd_wrap)
        page_booksellers.click_first_bookseller()
        
        page_booksellers.pledge_modal.initial_pledge()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        page_booksellers.pledge_modal.pledge_confirm()
        page_booksellers.confirm_bookseller_page()
        page_booksellers.click_first_bookseller()
        page_booksellers.pledge_modal.initial_unpledge()
        page_booksellers.pledge_modal.unpledge_confirm()
        
        webd_wrap.close_the_browser()
    
    def test_pledge_notsignedin_modal(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.pledge_flow_notsignedin_modal_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()
