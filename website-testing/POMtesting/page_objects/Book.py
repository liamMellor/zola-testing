'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time

class Book:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
       
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'purchase-button')), 'Not on Book Profile page')
       
        _url = self._webd_wrap._driver.current_url
        
        #if not _url.startswith(self._webd_wrap._baseURL + '/book'):
            #raise AssertionError("Not on a Book Profile page.")
    
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()   
    
    ########################################################################
    ########################################################################
        
    def rate(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-rating-bar-section-large').find_element_by_xpath('span/div[3]/a').click()
        # make sure the rating bar reloads before moving on
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-rating-bar-section-large')), 'rating bar not present')
        
    def click_buy(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/span/a').click()
        
    def click_add_to_list(self):
        self.confirm_page()
        self._webd_wrap._driver.find_element_by_link_text("ADD TO LIST").click()

        
    def click_recommend(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/ul/li[3]/a').click()
        
    def choose_wishlist(self):
        time.sleep(1)
        
        self._webd_wrap._driver.find_element_by_link_text('My Wishlist').click()
#         _element = self._webd_wrap._driver.find_element_by_xpath('/html/body/div[2]/div/section[2]/div[2]/div/div/ul/li[2]/div/div/div/div/section/ul/li/a')
#         _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
#         _hov.perform()
#         self._webd_wrap._driver.execute_script('(arguments[0]).click()', _element)
        
    

    
    