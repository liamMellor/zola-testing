'''
Created on Jul 10, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.add_card import add_card
from page_objects.acp_list import acp_list
from page_objects.bookseller_profile import bookseller_profile

#from page_objects.modals.recommend_modal import recommend_modal

class test_pledge_flow_signedin_modal(unittest.TestCase):
          
    def pledge_flow_signedin_modal_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
         
        page_homepage.click_sign_out()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        page_homepage.hover_over_connect_dropdown()
        page_homepage.click_on_link("Booksellers")
        
        page_acp_list = acp_list(webd_wrap)
        page_acp_list.click_first_acp()
        page_acp_list.bookseller_modal.click_full_profile()
        
        page_bookseller_profile = bookseller_profile(webd_wrap)
        page_bookseller_profile.click_pledge()
        
        page_bookseller_profile.pledge_modal.pledge_confirm()
        page_bookseller_profile.click_unpledge()
        page_bookseller_profile.pledge_modal.unpledge_confirm()
        
        webd_wrap.close_the_browser()
    
    def test_pledge_signedin_modal(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.pledge_flow_signedin_modal_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()