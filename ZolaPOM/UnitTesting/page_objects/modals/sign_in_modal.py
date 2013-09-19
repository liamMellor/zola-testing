from page_objects.modals.base_modal import base_modal
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class sign_in_modal(base_modal):
    def __init__(self, webd_wrap):
        base_modal.__init__(self, webd_wrap)
        
    def _confirm_modal(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fancybox-inner')), 'Sign In modal not present')
        
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))    
   
    ########################################################################
    
    def click_sign_up(self):
        self._confirm_modal()       
        
        _sign_up_button = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/section[2]/div/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _sign_up_button)
        
        # confirms modal is gone
        #self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    def sign_in(self, _username='davidtennant@zolabooks.com', _password='kingkong'): 
        self._confirm_modal()

        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_name('username'), _username)
        self._webd_wrap._driver.execute_script('$(arguments[0]).val(arguments[1])', self._webd_wrap._driver.find_element_by_id('sign-in-modal').find_element_by_name('password'), _password)

        _send = self._webd_wrap._driver.find_element_by_id("login_modal").find_element_by_xpath('div[3]/p/input')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _send)
        
        time.sleep(3) # waits for the login to register before moving on

