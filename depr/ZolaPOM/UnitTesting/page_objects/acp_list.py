'''
Created on Jul 10, 2013

@author: emma
'''
from selenium.webdriver.common.by import By
from UnitTesting.page_objects.base_page_object import base_page_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time

class acp_list(base_page_object):  

    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self, _acp_type=None):
        ''' raises AssertionError if page is incorrect. takes the type of acp as arg1 '''
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'author')), 'ACP list not present')
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        if _acp_type is None:
            _url = self._webd_wrap._baseURL + '/people/'
        else:
            _url = self._webd_wrap._baseURL + '/people/' + _acp_type
            _title = 'Zola Books | ebook | ' + _acp_type.capitalize()
        
        
        if _acp_type is None:
            if not _actual_url.startswith(_url):
                raise AssertionError("Not on an ACP page")
        else:
            if _url != _actual_url  or _title != _actual_title:
                raise AssertionError("Not on the appropriate ACP list page.")  
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
        
    def click_first_acp(self):
        ''' clicks the first acp in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()
        
    def click_follow_first_acp(self):
        ''' clicks follow on the first acp in the main list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[2]/a').click()
        
    ########################################################################
    ########################################################################
        
    def confirm_bookseller_page(self):
#         self.confirm_page()
        
        bookstore_button = self._webd_wrap._driver.find_element_by_class_name("author").find_element_by_xpath("a/div/img")
        if bookstore_button is None: raise Exception('bookstore button not found')
        
        hover = ActionChains(self._webd_wrap._driver).move_to_element(bookstore_button)
        hover.perform()
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', bookstore_button)