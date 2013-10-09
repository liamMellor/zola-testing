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
from UnitTesting.page_objects.bestsellers import bestsellers

class test_rating_notsignedin(unittest.TestCase):
          
    def rating_notsignedin_list_test(self, webd_wrap):
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()
         
        page_sign_up = sign_up(webd_wrap)
        email = page_sign_up.submit_new_member_info()
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends. click_skip_this()
        
        page_homepage.click_sign_out()
        page_homepage.click_bestsellers()
        
        page_bestsellers = bestsellers(webd_wrap)
        book_title = page_bestsellers.get_first_book_title()
        page_bestsellers.rate_first_book()
        page_bestsellers.sign_in_modal.sign_in(email, 'password')
        
        page_bestsellers.click_my_zola()
        
        page_my_zola = my_zola(webd_wrap)
        page_my_zola.first_activity_should_be_rated_book(book_title)
    
        webd_wrap.close_the_browser()
    
    def test_rating_notsignedin_list(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.rating_notsignedin_list_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()