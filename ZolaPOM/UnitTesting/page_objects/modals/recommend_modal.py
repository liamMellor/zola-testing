'''
Created on Jul 2, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.modals.base_modal import base_modal

class recommend_modal(base_modal):
    def __init__(self, webd_wrap):
        base_modal.__init__(self, webd_wrap)
        
    def _confirm_modal(self):
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fancybox-inner')), 'User modal not present')
    
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close) 
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    ########################################################################
    
    def submit_recommend(self):
        self._confirm_modal()
        
        self.enter_email()
        self.click_checkbox()
        self.enter_message()
        self.submit()
        
       
    def enter_email(self):
        _recommend_email_form = self._webd_wrap._driver.find_element_by_id('recommend-modal').find_element_by_id('recommend-email-form')
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', _recommend_email_form.find_elements_by_class_name('textboxlist-bit-editable-input')[0], '1@zolabooks.com')
    
    def click_checkbox(self):
        checkbox = self._webd_wrap._driver.find_element_by_id('uniform-share-with-followers').find_element_by_xpath('span/input')
        self._webd_wrap._driver.execute_script("$(arguments[0]).click()", checkbox)
            
    def enter_message(self):
        _recommend_email_form = self._webd_wrap._driver.find_element_by_id('recommend-email-form')
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', _recommend_email_form.find_elements_by_name('message')[0], 'test')
        
    def submit(self):
        send = self._webd_wrap._driver.find_element_by_id('recommend-modal').find_element_by_id("recommend-email-form").find_element_by_xpath("footer/input")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", send)
        
    