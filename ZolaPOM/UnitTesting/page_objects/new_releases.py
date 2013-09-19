'''
Created on Jul 25, 2013

@author: emma
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page_object import base_page_object

import time

class new_releases(base_page_object):
    
    def __init__(self,webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def confirm_page(self):
        ''' raises assertion error if page is incorrect '''
        
        _header = self._webd_wrap._driver.find_element_by_css_selector("div[class='l-full c-bg-white']").find_element_by_xpath('header/h2').text
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        if not _url.startswith('https://zolaqc.com/new-releases') or _title != 'Zola Books | New Releases | Browse' or _header != 'NEW RELEASES':
            raise AssertionError("Not on the bestsellers page.")
            
    ########################################################################
    ########################################################################