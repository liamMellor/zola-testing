'''
Created on Jul 15, 2013

@author: emma
'''
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from UnitTesting.page_objects.modals.base_modal import base_modal


class acp_modal(base_modal):  

    def __init__(self, webd_wrap):
        base_modal.__init__(self, webd_wrap)

    def _confirm_modal(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'fancybox-inner')), 'Message modal not present')
        
    def close_modal(self):
        self._confirm_modal()
        
        _close = self._webd_wrap._driver.find_element_by_class_name('fancybox-skin').find_element_by_xpath('a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _close)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))
        
    ######################################################################## 
        
    def click_follow(self):
        self._confirm_modal()
        
        _follow_button = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/div/section[1]/section[2]/section/ul/li[1]/a')
        self._webd_wrap._driver.execute_script('$(arguments[0]).click()', _follow_button)
        self._webd_wrap.wait.until(EC.title_contains("Zola"))
        
    def click_full_profile(self):
        self._confirm_modal()
        
        _full_profile = self._webd_wrap._driver.find_element_by_class_name('fancybox-inner').find_element_by_xpath('div/div/footer/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _full_profile)
        
        # confirms the modal is gone
        self._webd_wrap.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'fancybox-inner')))

    ########################################################################

    def get_name(self):
        self._confirm_modal()
        
        _elt = self._webd_wrap._driver.find_element_by_class_name("fancybox-inner").find_element_by_class_name('name-header').find_element_by_xpath("div/a")
        return _elt.text
    
    