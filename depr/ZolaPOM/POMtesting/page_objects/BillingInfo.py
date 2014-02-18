'''
Created on Jul 26, 2013

@author: emma
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

class BillingInfo:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'l-section-header-2')))
        
        _url = self._webd_wrap._driver.current_url
        
        #if not _url.startswith(self._webd_wrap._baseURL + '/profile/billing'):
         #   raise AssertionError("Not on the billing info page.")
        
    ##########################################################################
    ##########################################################################
    
    def click_add_card(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-section-header-2').find_element_by_xpath('a').click()
        
    def click_back_to_profile(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-section-capital').find_element_by_xpath('a').click()