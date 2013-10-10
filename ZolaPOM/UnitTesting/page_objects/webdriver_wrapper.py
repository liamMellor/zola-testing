'''
Created on Jun 18, 2013

@author: jsflax
'''
from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random


## module level variables separate from webdriver_wrapper:
mode = 'multi'  # change to 'single' to prevent closing and opening after each test
_drivers = {}  # so webdriver_wrapper can use existing if mode=='single'

class webdriver_wrapper():
    ################################################
    ############# GLOBAL VARIABLES #################
    ################################################

    _browsers = (#"chrome",
        "firefox",
        #"safari",
        )

    _baseURL = 'https://zolaqc.com'
    #_baseURL = 'https://zolabooks.com'
    #_baseURL = 'https://peoplefind.divergence.zolaqc.com'
    #_baseURL = 'https://luke.divergence.zolaqc.com'
    #_baseURL = 'https://amac.divergence.zolaqc.com'
    #_baseURL = 'https://amanda.divergence.zolaqc.com'
    #_baseURL = 'https://wuyou.divergence.zolaqc.com'

    logout_path = '/?ACT=12'

    ################################################
    #################### SETUP #####################
    ################################################

    def __init__(self, browser):
        global _drivers, mode
        self.rand_username_int = str( random.randint(0,1000000) )
        if mode == 'single' and browser in _drivers:
            self._driver = _drivers[browser]
        elif browser == 'chrome':
            self._driver = webdriver.Chrome('/Library/Python/2.7/site-packages/chromedriver')
        elif browser == 'safari':
            self._driver = webdriver.Remote(desired_capabilities={'browserName':'safari'})
        elif browser == 'firefox':
            self._driver = webdriver.Firefox()
        elif browser == 'ie':
            self._driver = webdriver.Ie()
        else:
            raise Exception('bad "browser" value passed in to '+self.__class__.__name__)
        _drivers[browser] = self._driver
        self._driver.implicitly_wait(40)
        self.wait = WebDriverWait(self._driver, 10)

        import re
        authURL = re.sub(r'(https?://)(.*)', r'\1zola_stage:zola123@\2', self._baseURL)
        self._driver.get(authURL)
    
    def open_page(self, path):
        self._driver.get(self._baseURL + path)
        
    def check_url(self, _url):
        ''' raises AssertionError if page is incorrect '''
        _actual_url = self._driver.current_url
        if _url != _actual_url:
            raise AssertionError("Not on correct page.")
        
    def close_the_browser(self):
        global mode
        self._driver.get(self._baseURL + self.logout_path)
        if mode == 'single':
            ## Just sleep to make sure the logout finishes, and don't close browser
            sleep(0.5)
        else:
            self._driver.quit()
        
    def switch_window(self):
        windows = self._driver.window_handles
        window = windows[1]
        self._driver.switch_to_window(window)   
    
    
