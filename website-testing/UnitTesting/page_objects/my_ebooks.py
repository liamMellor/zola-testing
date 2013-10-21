'''
Created on Jul 17, 2013

@author: emma
'''
from UnitTesting.page_objects.base_page_object import base_page_object

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

class my_ebooks(base_page_object):

    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        _header = self._webd_wrap._driver.find_element_by_class_name('title-1').text.lower()
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        if not _url.startswith(self._webd_wrap._baseURL + '/collection') or _title != 'Zola Books | Your Collection' or 'your collection' not in _header:
            raise AssertionError("Not on the My eBooks page.")
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
    
    ################################################################################################################
    #################################LINKS##########################################################################
    ################################################################################################################
    
    def click_all_books_see_all(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/section[2]/header[4]/a").click()
  
    def click_purchased_see_all(self):  
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/section[2]/header[3]/a').click()
    
    def check_purchased_see_all(self):
        ''' raises AssertionError if page is incorrect '''
        _actual_url = self._webd_wrap._driver.current_url
        if not _actual_url.startswith(self._webd_wrap._baseURL + '/collection/list/purchased/'):
            raise AssertionError("Not on purchased see all page.")
        
    def click_wishlist_see_all(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/section[2]/header[2]/a').click()    
     
    def check_wishlist_see_all(self):
        ''' raises AssertionError if page is incorrect '''
        _actual_url = self._webd_wrap._driver.current_url
        if not _actual_url.startswith(self._webd_wrap._baseURL + '/collection/list/wishlist/'):
            raise AssertionError("Not on wishlist see all page.") 
    ################################################################################################################
    #####################################TOP MENU LINKS#############################################################
    ################################################################################################################
     
    def click_want_to_read(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-bucket-header').find_element_by_xpath('li/a').click()
         
    def click_rated(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-bucket-header').find_element_by_xpath('li[2]/a').click()
           
    def click_purchased(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-bucket-header').find_element_by_xpath('li[3]/a').click()
                
    def click_preordered(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-bucket-header').find_element_by_xpath('li[4]/a').click()

      
    def click_lists(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-bucket-header').find_element_by_xpath('li[5]/a').click()
