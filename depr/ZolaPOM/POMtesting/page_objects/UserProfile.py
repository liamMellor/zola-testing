'''
Created on Jul 2, 2013

@author: padelstein
'''


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class UserProfile:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'activity-container')), 'user profile not found')

        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith(self._webd_wrap._baseURL + '/profile'):
            raise AssertionError("Not on a profile page.")    
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    def click_sign_out(self):
        ''' clicks the sign out link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('logout-link').click()
        
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
        
    def click_send_message(self):
        ''' clicks the send message link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/header/ul/li[2]/a').click()
        
    ########################################################################
    ########################################################################
    
    def get_name(self):
        ''' returns the name of the user '''
        self.confirm_page()
        
        _name = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/header/div[2]/div/h2/span')
        return _name.text
    
    def get_url_ext(self):
        ''' returns the url extension for the user '''
        self.confirm_page()
        
        _url = self._webd_wrap._driver.current_url
        return _url.replace(self._webd_wrap._baseURL + '/profile')
    
    
