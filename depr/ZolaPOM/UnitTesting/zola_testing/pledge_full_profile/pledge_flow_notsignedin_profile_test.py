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
from UnitTesting.page_objects.bookseller_profile import bookseller_profile



class test_pledge_flow_notsignedin_profile(unittest.TestCase):
          
    def pledge_flow_notsignedin_profile_test(self, webd_wrap):
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
        page_booksellers.bookseller_modal.click_full_profile()
        
        page_bookseller_profile = bookseller_profile(webd_wrap)
        page_bookseller_profile.click_pledge()
        
        page_bookseller_profile.sign_in_modal.sign_in(email, 'password')
        page_bookseller_profile.pledge_modal.pledge_confirm()
        page_bookseller_profile.click_unpledge()
        page_bookseller_profile.pledge_modal.unpledge_confirm()
        
        webd_wrap.close_the_browser()
    
    def test_pledge_notsignedin_profile(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.pledge_flow_notsignedin_profile_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()