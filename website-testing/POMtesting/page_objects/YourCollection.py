'''
Created on Jul 23, 2013

@author: emma
'''

import selenium.common.exceptions as Exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class YourCollection:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'title-1'), 'Your Collection'), 'not on Your Collection page.')

        
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        if not _url.startswith(self._webd_wrap._baseURL + '/collection/list/') or _title != 'Zola Books | Your Collection':
            raise AssertionError("Not on the Your Collection page.")
        
    ##################################################################################
    ##################################################################################

    def click_all_rated(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[6]").click()
    
    def click_purchased(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[2]").click()
    
    def click_preordered(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[3]").click()
    
    def click_favorites(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[4]").click()
        
    def click_wishlist(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[5]").click()
        
    def click_not_for_me(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[7]").click()
        
    def click_private_books(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[8]").click()
        
    def click_edit_devices(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("t-center").find_element_by_xpath("a").click()
        
    def click_save_devices(self):
        self.confirm_page()
        
        self._webd_wrap.wait.until(EC.visibility_of( self._webd_wrap._driver.find_element_by_class_name('deauthorize-device') ))
        
        self._webd_wrap._driver.find_element_by_class_name("t-center").find_element_by_xpath("a").click()
        
    def click_view_all(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div/div[2]/a').click()
         
    def click_first_book(self):
        self.confirm_page()    
        
        self._webd_wrap._driver.find_element_by_class_name('trigger-modal-book').find_element_by_xpath('img').click()
        
    #################################################################################
    #################################################################################
    
    def confirm_filter_selected(self, _filter):
        self.confirm_page()

        _header = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('header/h1').text.lower()            
        
        if _filter not in _header:
            raise AssertionError("Correct filter not selected")
        
        
        
