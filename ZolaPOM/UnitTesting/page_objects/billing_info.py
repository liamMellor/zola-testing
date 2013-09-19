'''
Created on Jul 29, 2013

@author: emma
'''
from page_objects.base_page_object import base_page_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class billing_info(base_page_object):
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-section-header-2')))
        
        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith('https://zolaqc.com/profile/billing'):
            raise AssertionError("Not on the billing info page.")