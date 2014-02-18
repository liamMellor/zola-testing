from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from UnitTesting.page_objects.modals.base_modal import base_modal

import time

class purchase_confirm_modal(base_modal):
    def __init__(self, webd_wrap):
        base_modal.__init__(self, webd_wrap)
    
         
    def _confirm_modal(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "web-purchase")), 'Purchase Confirm Modal not present.')
    
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    ########################################################################
        
    def click_receive_emails(self):
        self._confirm_modal()
        
        _receive_emails = self._webd_wrap._driver.find_element_by_id('receive_author_emails')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _receive_emails)
        time.sleep(1)
        
    def click_buy(self):
        self._confirm_modal()
        
        _buy_button = self._webd_wrap._driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer/a[1]")
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _buy_button)
        time.sleep(1)
        
    def click_done(self):
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.ID, 'receive_author_emails')))
       
        _elt = self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _elt)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))