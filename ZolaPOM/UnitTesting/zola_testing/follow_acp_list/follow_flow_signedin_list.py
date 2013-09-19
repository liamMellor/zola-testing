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
from page_objects.acp_list import acp_list


class follow_flow_signedin_test(unittest.TestCase):
          
    def follow_signedin_list_test(self, webd_wrap):
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
        page_homepage.click_on_link('Authors')
        
        page_acp_list = acp_list(webd_wrap)
        page_acp_list.click_follow_first_acp()
        page_acp_list.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_follow()
    
        webd_wrap.close_the_browser()
    
    def test_follow_signedin_list(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.follow_signedin_list_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()