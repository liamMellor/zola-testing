'''
Created on Jul 15, 2013

@author: emma
'''

import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.find_friends import find_friends
from page_objects.my_zola import my_zola
from page_objects.book import book


import time

#from page_objects.modals.recommend_modal import recommend_modal

class addtolist_flow_notsignedin_test(unittest.TestCase):
          
    def add_to_list_notsignedin_profile_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
         
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.click_skip_this()
        page_homepage.click_sign_out()
        page_homepage.click_first_bestseller()
        title = page_homepage.book_modal.get_book_title()
        page_homepage.book_modal.click_full_profile()
        
        page_book = book(webd_wrap)
        page_book.click_add_to_list_nsi()
        page_book.sign_in_modal.sign_in(email, 'password')
        page_book.choose_wishlist()
        page_book.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_added_book(title)
    
        webd_wrap.close_the_browser()
    
    def test_addtolist_notsignedin_profile(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.add_to_list_notsignedin_profile_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()