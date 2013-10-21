from selenium.webdriver.common.by import By
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.app_objects.base_app_object import base_app_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import random
import os
from UnitTesting.app_objects.home_screen import home_screen
from UnitTesting.app_objects.appium_wrapper import appium_wrapper


class my_ebooks_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)

    def click_home_button(self):
        self.driver.find_element_by_name('ipad nav home off').click()

    def click_my_ebooks(self):
        self.driver.find_element_by_name('ipad nav myebooks on').click()

    def refresh(self):
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
    
    def click_third_book(self):
        self.driver.find_element_by_xpath('//window[1]/tableview[1]/cell[3]/button[2]').click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Downloading Book..."
        time.sleep(7)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Download Complete"

    def confirm_purchase(self, num_books):
        num_purch = self.driver.find_element_by_xpath('//window[1]/text[2]')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Number of Books Purchased: " + str(num_purch)
        if num_purch.text != (str(num_books) + " Purchased"):
            raise AssertionError("Number of Books Purchased Incorrect")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Number of Books Purchased Correct"

