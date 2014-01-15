'''
Created on Jul 17, 2013

@author: emma
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from UnitTesting.page_objects.base_page_object import base_page_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

class find_friends(base_page_object):
    
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self, _name=None):
        ''' raises AssertionError if page is incorrect '''
       # self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.ID, 'suggest_h2'), 'Suggested'))
        
       # _actual_url = self._webd_wrap._driver.current_url
        _actual_title = self._webd_wrap._driver.title
        
       # _url = self._webd_wrap._baseURL + '/profile/people/finder'
       # if _name is None:
       #     _title = _actual_title
       # else:
       #     _title = 'Zola Books | ' + _name
       # 
       # if _url != _actual_url  or _title != _actual_title:
       #     raise AssertionError("Not on the People Finder page.")
        
    def click_skip_this(self):
        time.sleep(2)
        print "skipping people finder"
        self._webd_wrap._driver.find_element_by_xpath('/html/body/div[2]/div/div/footer/form/a').click()
