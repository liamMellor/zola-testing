from selenium.webdriver.common.by import By
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.app_objects.base_app_object import base_app_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from datetime import datetime
import random
import os
from UnitTesting.app_objects.home_screen import home_screen
from UnitTesting.app_objects.appium_wrapper import appium_wrapper
import pprint


class my_ebooks_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)

    def click_home_button(self):
        self.driver.find_element_by_name('ipad nav home off').click()
        time.sleep(3)

    def click_my_ebooks(self):
        self.driver.find_element_by_name('ipad nav myebooks on').click()

    def refresh(self):
        time.sleep(5)
        self.driver.find_element_by_name('ipad purchased refresh').click()

    def click_purchased_tab(self):
        self.driver.find_element_by_name('PURCHASED').click()

    def check_home_button(self):
        #self.wait.until(EC.element_to_be_clickable((By.NAME,'ipad landing gear')))
        home_button = self.driver.find_element_by_name('ipad nav home off')
        home_button.size()

    def click_on_this_device_tab(self):
        self.driver.find_element_by_name('ON THIS DEVICE').click()

    def click_wishlist_tab(self):
        self.driver.find_element_by_name('WISHLIST').click()
    
#    def click_first_book(self):
#        self.driver.find_element_by_xpath('//window[1]/tableview[1]/cell[1]/button[2]').click()
#        time.sleep(8)

    def click_first_book(self):
        iphonebookdl = self.driver.find_elements_by_xpath("//button[contains(@text, 'download')]")
        iphonebookdl[0].click()
        time.sleep(10)
    
    def click_book_with_shimmer(self, num_books):
        self.driver.find_element_by_xpath('//window[1]/tableview[1]/cell[1]/button[2]').click()
        appium_wrap = appium_wrapper(num_books)
        time.sleep(1)
        appium_wrap.get_screenshot()
        time.sleep(5)
    
    def click_third_book(self):
        self.driver.find_element_by_xpath('//window[1]/tableview[1]/cell[3]/button[2]').click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Downloading Book..."
        time.sleep(7)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Download Complete"
    
    def iphone_confirm_purchase(self):
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "on purchased tab...debugging..." + str(self.driver.find_element_by_xpath("//text[contains(@text,'Purchased')]").text)
        if (self.driver.find_element_by_xpath("//text[contains(@text,'Purchased')]").text) != (str("Purchased")):
            raise AssertionError("...not on purchased tab")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "...on purchased tab"

    def confirm_purchase(self, num_books):
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Number of Books Purchased: " + str(self.driver.find_element_by_xpath("//text[contains(@text,'Purchased')]").text)
        if self.driver.find_element_by_xpath("//text[contains(@text,'Purchased')]").text != (str(num_books) + " Purchased"):
            raise AssertionError("Number of Books Purchased Incorrect")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Number of Books Purchased Correct"

    def return_book_title(self):
        
        return True if self.driver.find_element_by_xpath("//text[contains(@text,'Making Mavericks,')]") else False

    def click_making_mavs_download(self):
        self.driver.find_element_by_xpath("//text[contains(@text,'Making')]").find_element_by_name('ipad bookdetail download').click()

    def confirm_book_title(self):
        print self.driver.find_element_by_xpath("//text[contains(@text,'Making Mavericks,')]").get_attribute('name')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Making Mavericks Exists: True or False?"
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), self.return_book_title()
                                                                                                  
                                                                                            
#//window[1]/tableview[1]/cell[1]
