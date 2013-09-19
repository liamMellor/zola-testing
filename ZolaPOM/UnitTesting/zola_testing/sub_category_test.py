
#import sys
#sys.path.append("page_objects")


import unittest #imports unit test/ability to run as pyunit test
from page_objects.webdriver_wrapper import webdriver_wrapper
from page_objects.sign_up import sign_up
from page_objects.homepage import homepage
from page_objects.add_card import add_card
from page_objects.category import category

class category_search(unittest.TestCase):
          
    def individual_category_test(self, page_home, webd_wrap, category):
        
        page_home.get_page()
        page_home.hover_over_category_dropdown()
        page_home.click_on_link(category)
        page_category.click_first_sub_category()

        page_category.page_title_should_be('Zola Books | ebook | ' + page_category)
        
        #webd_wrap.close_the_browser()
        
    
    def test_category(self): #running x as a unit test
        for browser in webdriver_wrapper._browsers:
            
            _driver = webdriver_wrapper(browser)
            #_driver.open_page('/')
            
            page_homepage = homepage(_driver)
            
            for category in page_homepage._categories:
                if ( category == 'Children' or category == 'Young Adult'):
                    self.individual_category_test(page_homepage, webdriver_wrapper, category)
            #webdriver_wrapper.close_the_browser()

    
print "Module Complete", __name__
if __name__ == "__main__":
    unittest.main()








# '''
# Created on Jun 18, 2013
# 
# @author: jsflax
# '''
# 
# #import sys
# #sys.path.append("page_objects")
# 
# import unittest #imports unit test/ability to run as pyunit test
# from page_objects.webdriver_wrapper import webdriver_wrapper
# from page_objects.sign_up import sign_up
# from page_objects.homepage import homepage
# from page_objects.add_card import add_card
# from page_objects.category import category
# 
# class category_search(unittest.TestCase):
#           
#     def individual_category_test(self, page_home, webd_wrap, category):
#         
#         #page_homepage = homepage(webd_wrap)
#         page_home.get_page()
#         page_home.hover_over_category_dropdown()
#         
#         page_category = category(webd_wrap)
#         page_category=page_home.click_on_link(category) 
#          
#         #page_category.page_title_should_be('Zola Books | ebook | ' + category)
#         
#        # page_category = category(webd_wrap)
#         page_category.click_first_sub_category()
#         
# 
#         
#     
#     def test_category(self): #running x as a unit test
#         for browser in webdriver_wrapper._browsers:
#             
#             page_homepage = homepage(webdriver_wrapper(browser))
#             
#             for category in page_homepage._categories:
#                 if ( category == 'Children' or category == 'Young Adult'):
#                     self.individual_category_test(page_homepage, webdriver_wrapper(browser), category)
#             webdriver_wrapper.close_the_browser()
# 
#     
# print "Module Complete", __name__
# if __name__ == "__main__":
#     unittest.main()
#   
#         
