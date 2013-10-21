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

class login_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)

    def log_in(self):
        self.driver.implicitly_wait(180)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Appium Test"
        buttons = self.driver.find_elements_by_tag_name('button')
        text = self.driver.find_elements_by_tag_name('textField')
        text[0].click()
        text[0].send_keys("jay+" + self.appium_wrap.rand_username_int + "@zolabooks.com")
        secure = self.driver.find_elements_by_tag_name("secure")
        secure[0].click()
        secure[0].send_keys("password")
        #secure[0].send_keys("\n")
        #login = self.driver.find_elements_by_name("ipad login loginbutton")
        buttons[0].click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Logging in..."
        time.sleep(5)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Log in Succesful"
