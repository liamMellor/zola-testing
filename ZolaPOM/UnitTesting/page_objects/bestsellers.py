'''
Created on Jul 3, 2013

@author: padelstein
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page_object import base_page_object

import time

class bestsellers(base_page_object):  

    def __init__(self, webd_wrap):
            base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        _header = self._webd_wrap._driver.find_element_by_css_selector("div[class='l-full c-bg-white']").find_element_by_xpath('header/h2').text
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        if not _url.startswith('https://zolaqc.com/bestsellers') or _title != 'Zola Books | Best Sellers | Browse' or _header != 'BESTSELLERS':
            raise AssertionError("Not on the bestsellers page.")     
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    ########################################################################
    ########################################################################
    
    def click_first_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/a[1]').click()
        
    def click_second_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[3]/div/div/a[1]').click()
        
    def click_eighth_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[9]/div/div/a[1]').click()
        
    def click_buy_first_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/div[1]/a').click()
        
    def click_buy_second_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[3]/div/div/div[1]/a').click()
        
    def click_buy_eighth_book(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[9]/div/div/div[1]/a').click()
        
    def rate_first_book(self):
        self.confirm_page()

        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]').find_element_by_class_name('star-rating-control').find_element_by_xpath('div[4]/a').click()        
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'star-rating-control')), 'rating bar did not reload properly')
        time.sleep(2)
        
    def get_first_book_title(self):
        self.confirm_page()
        
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'l-main-primary')))
        _book_title = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[2]/div/div/a')
        return _book_title.text
    
    def get_second_book_title(self):
        self.confirm_page()
        
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'l-main-primary')))
        _book_title = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[3]/div/div/a')
        return _book_title.text
    
    def get_eighth_book_title(self):
        self.confirm_page()
        
        self._webd_wrap.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'l-main-primary')))
        _book_title = self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('section[9]/div/div/a')
        return _book_title.text
        
    