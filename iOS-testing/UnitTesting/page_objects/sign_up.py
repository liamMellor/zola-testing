from UnitTesting.page_objects.base_page_object import base_page_object
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import random 

class sign_up(base_page_object):
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        #base_app_object.__init__(self, appium_wrap)
    
    def get_page(self):
        self._webd_wrap.open_page('/signup')
        return self
        
    def confirm_page(self):
        
       # self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-1'), 'Fill in your'))
        
        _actual_url = self._webd_wrap._driver.current_url
       # _url = self._webd_wrap._baseURL + '/signup'
        
       # if not _actual_url.startswith(_url):
       #     raise AssertionError("Not on Sign Up page.") 
        
    ########################################################################
    ########################################################################
        
    def submit_new_member_info(self):
        self.confirm_page()
        email = "jay+" + (self._webd_wrap.rand_username_int) + "@zolabooks.com"
        self.register_email(email)
        self.register_password()
        self.register_name()
        self.register_birthday()
        self.register_submit()
        
        return email

    def register_email(self, email):
        self._webd_wrap._driver.find_element_by_name("email").send_keys(email)
    
        #above line is before we removed confirm email
        
    def register_password(self):

        self._webd_wrap._driver.find_element_by_id("password").send_keys("password")


    def register_name(self):
        self._webd_wrap._driver.find_element_by_id("first_name").send_keys("Lin")
        self._webd_wrap._driver.find_element_by_id("last_name").send_keys("Robinson")

    def register_birthday(self):
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, "bday_m")))
        self._webd_wrap._driver.find_element_by_id("bday_m").send_keys("10")
        self._webd_wrap._driver.find_element_by_id("bday_d").send_keys("26")
        self._webd_wrap._driver.find_element_by_id("bday_y").send_keys("1990")

    def register_submit(self):
        
        self._webd_wrap._driver.find_element_by_name("submit").click()
        #self._webd_wrap._driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/form/div[2]/footer/p/input').click()
