'''
Created on Jul 10, 2013

@author: emma
'''

from page_objects.base_page_object import base_page_object
from selenium.webdriver.common.action_chains import ActionChains

import time 
class booksellers(base_page_object):  

    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def get_page(self, category):
        return self

    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        _url = 'https://zolaqc.com/people/booksellers'
        _title = 'Zola Books | ebook |'# Booksellers'
        
        if _url != _actual_url  or _title != _actual_title:
            raise AssertionError("Not on the Booksellers list page.")
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()    
        
    ########################################################################
    ######################################################################## 
    
    def click_first_bookseller(self):
        ''' clicks the first acp in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()