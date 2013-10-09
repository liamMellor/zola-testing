'''
Created on Jul 15, 2013

@author: emma
'''
from UnitTesting.page_objects.base_page_object import base_page_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class acp_profile(base_page_object):  

    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul[class='ui-button-set ui-button-set-170px']")), 'Not on a Profile page.')
        
        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith(self._webd_wrap._baseURL + '/profile'):
            raise AssertionError("Not on a profile page.")    
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
        
    def click_follow(self):
        ''' clicks the follow link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/header/ul/li[1]/a[1]').click()
        
    def star_first_activity(self):
        ''' stars the first activity on the page '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]').find_element_by_xpath('ul[1]/li/a').click()
        
    ########################################################################
    ########################################################################
    
    def get_name(self):
        self.confirm_page()
        
        _name = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/header/div[2]/div/h2/span')
        return _name.text
    
    
