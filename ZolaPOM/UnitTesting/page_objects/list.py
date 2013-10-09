'''
Created on Jul 25, 2013

@author: emma
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from UnitTesting.page_objects.base_page_object import base_page_object

import time

class list(base_page_object):  

    def __init__(self, webd_wrap):
            base_page_object.__init__(self, webd_wrap)


    def confirm_page(self, _list_name=None):
        ''' raises AssertionError if page is incorrect. takes the type of acp as arg1 '''
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        if _list_name is None:
            _title = 'Zola Books | ebook | Booklist'
            if not _actual_url.startswith(self._webd_wrap._baseURL + '/list') or not _actual_title.startswith(_title):
                raise AssertionError("Not on an List page")
        else:
            _title = 'Zola Books | ebook | ' + _list_name
            if not _actual_url.startswith(self._webd_wrap._baseURL + '/list') or not _actual_title.startswith(_title):
                raise AssertionError("Not on a List page")

    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
        
    
    def confirm_daily_deals(self):
        ''' confirms the page is the Zola Deals page '''

        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-1')))        
        
        _list_title = self._webd_wrap._driver.find_element_by_class_name('header-1').text
        
        if 'ZOLA DEALS!' not in _list_title:
                raise AssertionError("Not on Daily Deals page")