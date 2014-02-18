'''
Created on Jul 25, 2013

@author: emma
'''
import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.recommendations import recommendations

class navigation_find_great_ebooks(unittest.TestCase):
          
    def find_great_ebooks_test(self, webd_wrap):
        
        page_homepage = homepage(webd_wrap)
        page_homepage.get_page()
        page_homepage.click_find_great_ebooks()
        
        page_recommendations = recommendations(webd_wrap)
        page_recommendations.confirm_page()
        
        webd_wrap.close_the_browser()
        
        
    
    def test_find_great_ebooks(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            self.find_great_ebooks_test(webdriver_wrapper(browser))

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()