'''
Created on Jul 10, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time
import random

class MessageModal:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def _confirm_modal(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fancybox-inner')), 'Message modal not present')    
    
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    ########################################################################
    ########################################################################
    
    def enter_message(self, _message=None):
        self._confirm_modal()
        
        if _message is None:
            _message = 'test' + str(random.randint(0,1000000000))
        
        _message_field = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_id('message-form').find_element_by_xpath('section/div/section/div/p[2]/textarea')
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', _message_field, _message)
        
    def submit_message(self):
        self._confirm_modal()
        
        _submit = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_id('message-form').find_element_by_xpath('footer/input')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _submit)
        
        time.sleep(2)
        