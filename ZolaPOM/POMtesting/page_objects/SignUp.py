'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import time
import random

class SignUp:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
        self._first_name_list = ['Adam', 'John', 'Lin', 'Jennifer', 'Jerome', 'Alyssa', 'Cassandra', 'Terry',
                            'Dan', 'Katya', 'Andrea', 'Ken', 'Frank', 'Ingrid', 'Monica', 'Natalya']
        self._last_name_list = ['Davidson', 'Robinson', 'Berry', 'Chen', 'Miller', 'Wilson', 'White', 'Hall',
                            'King', 'Green', 'Baker', 'Parker', 'Cook', 'Simpson', 'Porter', 'Shaw']
        
    def confirm_page(self):
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-1'), 'Fill in your'))
        
        #_actual_url = self._webd_wrap._driver.current_url
        #_url = self._webd_wrap._baseURL + '/signup'
        
        #if not _actual_url.startswith(_url):
            #raise AssertionError("Not on Sign Up page.") 
        
    ########################################################################
    ########################################################################
        
    def submit_new_member_info(self):
        self.confirm_page()
        _email = 'jay+' + str( random.randint(0, 100000000) ) + '@zolabooks.com'
        
        self.register_email(_email)
        self.register_password()
        self.register_name()
        self.register_birthday()
        self.register_submit()
        
        return _email

    def register_email(self, _email):
        
        self._webd_wrap._driver.find_element_by_name("email").send_keys(_email)
        self._webd_wrap._driver.find_element_by_name("confirm_email").send_keys(_email)

    def register_password(self):

        self._webd_wrap._driver.find_element_by_id("password").send_keys("password")
        self._webd_wrap._driver.find_element_by_id("confirm_password").send_keys("password")


    def register_name(self):
        
        _first_name = self._first_name_list[ random.randint(0, 15) ]
        _last_name = self._last_name_list[ random.randint(0, 15) ]
        
        self._webd_wrap._driver.find_element_by_id("first_name").send_keys(_first_name)
        self._webd_wrap._driver.find_element_by_id("last_name").send_keys(_last_name)
        
        

    def register_birthday(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "bday_m")))
        self._webd_wrap._driver.find_element_by_id("bday_m").send_keys("10")
        self._webd_wrap._driver.find_element_by_id("bday_d").send_keys("26")
        self._webd_wrap._driver.find_element_by_id("bday_y").send_keys("1990")

    def register_submit(self):
        
        #self._webd_wrap._driver.find_element_by_xpath('/html/body/div[3]/div/section/div/form/div[2]/div/p/input').click()
        #self._webd_wrap._driver.find_element_by_xpath('/html/body/div[2]/div/form/section[2]/div/p[2]/input').click()

	self._webd_wrap._driver.find_element_by_id('signup_form').find_element_by_name("submit").click()
        #/html/body/div[3]/div/section/div/form/div[2]/div/p/input #you
        #/html/body/div[2]/div/form/section[2]/div/p[2]/input #you-mid flow signup page
        #/html/body/div[2]/div/form/section[2]/div/p[2]/input #qc