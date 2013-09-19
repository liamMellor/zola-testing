'''
Created on Jul 15, 2013

@author: emma
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page_object import base_page_object

import time

class book(base_page_object):
    
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
       
        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith('https://zolaqc.com/book'):
            raise AssertionError("Not on a Book Profile page.")
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()   
    
    ########################################################################
    ########################################################################
        
    def rate(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-rating-bar-section-large').find_element_by_xpath('span/div[3]/a').click()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-rating-bar-section-large')), 'rating bar not present')
        
    def click_buy(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/span/a').click()
        
    def click_add_to_list(self):
        self.confirm_page()
        
        #self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[2]/a').click()
        self._webd_wrap._driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div[2]/div/div/ul/li[2]/div/a').click()
        
   
    def click_recommend(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[3]/a').click()
        
    def choose_wishlist(self):
        time.sleep(1)
        
        _element = self._webd_wrap._driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div[2]/div/div/ul/li[2]/div/div/div/div/section/ul/li/a')
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        self._webd_wrap._driver.execute_script('(arguments[0]).click()', _element)
        
    

    
    