'''
Created on Jul 29, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.category import category

class homepage_humor(unittest.TestCase):
          
    def homepage_humor_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_category("Humor & Entertainment")
        
        page_category = category(webd_wrap)
        page_category.page_title_should_be("Zola Books | ebook | Humor & Entertainment")
        page_category.click_first_book()
        page_category.book_modal.close_modal()
        
        
        webd_wrap.close_the_browser()
        
        
    
    def test_homepage_humor(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.homepage_humor_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()