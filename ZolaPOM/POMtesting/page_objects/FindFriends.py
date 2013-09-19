'''
Created on Jul 17, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import random
import time

class FindFriends:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self, _name=None):
        ''' raises AssertionError if page is incorrect '''
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.ID, 'suggest_h2'), 'Suggested'))
        
        _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
        _url = self._webd_wrap._baseURL + '/profile/people/finder'
        if _name is None:
            _title = _actual_title
        else:
            _title = 'Zola Books | ' + _name
        
        #if _url != _actual_url  or _title != _actual_title:
            #raise AssertionError("Not on the People Finder page.")
        
    def click_skip_this(self):
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer[class='pad-box-40px t-center']")))
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div[1]/div/footer/form/input').click()

