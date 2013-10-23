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
from UnitTesting.app_objects.my_ebooks_screen import my_ebooks_screen

class login_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)
    
    def textfield(self):
        self.driver.find_element_by_xpath('//window[1]/textfield[1]')
    
    def log_in(self):
        self.driver.implicitly_wait(180)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Appium Test"
        buttons = self.driver.find_elements_by_tag_name('button')
        text = self.driver.find_elements_by_xpath('//window[1]/textfield[1]')
        text[0].click()
        text[0].send_keys("jay+" + self.appium_wrap.rand_username_int + "@zolabooks.com")
        secure = self.driver.find_elements_by_xpath("//window[1]/secure[1]")
        secure[0].click()
        secure[0].send_keys("password")
        #secure[0].send_keys("\n")
        #login = self.driver.find_elements_by_name("ipad login loginbutton")
        buttons[0].click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Logging in..."
        time.sleep(40)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Log in Succesful"

    def login_check(self):
        app_home_screen = home_screen(self.appium_wrap)
        app_my_ebooks_screen = my_ebooks_screen(self.appium_wrap)
        try:
            self.driver.implicitly_wait(0)
            self.driver.find_element_by_xpath('//window[1]/textfield[1]')
            self.driver.implicitly_wait(10)
            self.log_in()
    #self.driver.find_element_by_xpath('//window[1]/textfield[1]').location['y'] == 212 and self.driver.find_element_by_xpath('//window[1]/textfield[1]').location['x'] == 182:
            # app_home_screen.deregister_device()
            
        #   app_home_screen.refresh()
        except:
            cog = self.driver.find_element_by_xpath('//window[1]/button[4]')
            cog.size['width'] == 33 and cog.size['height'] == 26
            app_home_screen.deregister_device()
            self.log_in()
    #    app_home_screen.refresh()
    #       cog = self.driver.find_element_by_xpath('//window[1]/button[4]')
    #       cog.size['width'] == 33 and cog.size['height'] == 26
    #       app_home_screen.deregister_device()
#       self.log_in()
        #   app_home_screen.refresh()