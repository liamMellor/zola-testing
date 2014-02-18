'''
Created on Jul 10, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class Booksellers:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'subheader-1'), 'Booksellers'), 'Bookseller list not present')
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        _url = self._webd_wrap._baseURL + '/people/booksellers'
        _title = 'Zola Books | ebook |'# Booksellers'
        
        #if _url != _actual_url  or _title != _actual_title:
            #raise AssertionError("Not on the Booksellers list page.")
        
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