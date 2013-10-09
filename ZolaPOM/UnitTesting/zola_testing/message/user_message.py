'''
Created on Jul 15, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.find_friends import find_friends
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.user_profile import user_profile


class user_message(unittest.TestCase):
          
    def message_test(self, webd_wrap):
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
        page_homepage.click_my_zola()

        webd_wrap.open_page('/profile/david-tennant/')
        page_user_profile= user_profile(webd_wrap)
        page_user_profile.click_follow()
        page_user_profile.click_sign_out()
        
        page_homepage = homepage(webd_wrap)
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in()
        page_homepage.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.click_my_followers()
        page_my_zola.click_follow_first_user()
        page_my_zola.click_first_user()
        page_my_zola.user_modal.click_send_message()
        page_my_zola.message_modal.enter_message()
        page_my_zola.message_modal.submit_message()
        page_my_zola.message_modal.close_modal()
        page_my_zola.click_sign_out()
        
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.sign_in(email, 'password')
        page_homepage.click_my_zola()
        
        page_my_zola.click_messages()
        page_my_zola.first_message_should_be_from('David')
    
        webd_wrap.close_the_browser()
    
    def test_message(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.message_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()