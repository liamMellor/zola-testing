from page_objects.base_page_object import base_page_object

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import random 

class sign_up(base_page_object):
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def get_page(self):
        self._webd_wrap.open_page('/signup')
        return self
        
    def confirm_page(self):
        
        _actual_url = self._webd_wrap._driver.current_url
        _url = 'https://zolaqc.com/signup'
        
        if not _actual_url.startswith(_url):
            raise AssertionError("Not on Sign Up page.") 
        
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

    def register_email(self, email):
        self._webd_wrap._driver.find_element_by_name("email").send_keys(email)
        self._webd_wrap._driver.find_element_by_name("confirm_email").send_keys(email)

    def register_password(self):
        self._webd_wrap._driver.find_element_by_name("password").send_keys("password")
        self._webd_wrap._driver.find_element_by_name("confirm_password").send_keys("password")

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