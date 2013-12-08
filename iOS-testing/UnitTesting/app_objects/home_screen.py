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

class home_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)

    def click_home_button(self):
        self.driver.find_element_by_name('ipad nav home on').click()

    def click_my_ebooks(self):
        self.driver.find_element_by_xpath('//window[1]/button[2]').click()
        time.sleep(5)

    def refresh(self):
        sync = self.driver.find_element_by_xpath('//window[1]/button[3]').location
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":sync['x'],"y":sync['y']})

    def check_landing_gear(self):
        #self.wait.until(EC.element_to_be_clickable((By.NAME,'ipad landing gear')))
        cog = self.driver.find_element_by_xpath('//window[1]/button[4]').location
        print str(cog)
    
    def iphone_click_landing_gear(self):
        self.driver.find_element_by_xpath('//window[1]/button[4]').click()
        time.sleep(5)

    def click_landing_gear(self):
        #self.driver.find_element_by_xpath('//window[1]/button[4]').click()
        #self.driver.find_element_by_xpath("//text[contains(@text,'gear']").click()
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"711","y":"80"})

    def click_deregister(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'information deregister')]").click()

    def click_send_feedback(self):
        self.driver.find_element_by_name('ipad information sendfeedback').click()

    def click_tos(self):
        self.driver.find_element_by_name('ipad information termsofservic').click()

    def click_privacy_policy(self):
        self.driver.find_element_by_name('ipad information privacy').click()

    def click_logout(self):
        self.driver.find_element_by_name('YES').click()

    def iphone_deregister_device(self):
        self.iphone_click_landing_gear()
        self.click_deregister()
        self.click_logout()

    def deregister_device(self):
        self.click_landing_gear()
        self.click_deregister()
        self.click_logout()