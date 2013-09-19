'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.find_friends import find_friends


class connect_friends_notsignedin(unittest.TestCase):
          
    def friends_notsignedin_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.hover_over_connect_dropdown()
        page_homepage.click_on_link('Friends')
        page_homepage.sign_in_modal.sign_in()
        #page_homepage.hover_over_connect_dropdown()
        #page_homepage.click_on_link('Friends')
        
        page_find_friends = find_friends(webd_wrap)
        page_find_friends.confirm_page('David Tennant')
        
        webd_wrap.close_the_browser()
        
        
    
    def test_friends_notsignedin(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.friends_notsignedin_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()