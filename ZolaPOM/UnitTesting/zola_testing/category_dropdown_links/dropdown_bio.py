'''
Created on Jul 29, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.homepage import homepage
from page_objects.category import category

class dropdown_bio(unittest.TestCase):
          
    def dropdown_bio_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.hover_over_category_dropdown()
        page_homepage.click_on_link("Biography & Memoir")
        
        page_category = category(webd_wrap)
        page_category.page_title_should_be("Zola Books | ebook | Biography & Memoir")
        
        
        webd_wrap.close_the_browser()
        
        
    
    def test_dropdown_bio(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.dropdown_bio_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()