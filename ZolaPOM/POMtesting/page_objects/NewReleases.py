'''
Created on Jul 17, 2013

@author: emma
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn

import random

class NewReleases:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises assertion error if page is incorrect '''
        
        _header = self._webd_wrap._driver.find_element_by_css_selector("div[class='l-full c-bg-white']").find_element_by_xpath('header/h2').text
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
      #  if not _url.startswith(self._webd_wrap._baseURL + '/new-releases') or _title != 'Zola Books | New Releases | Browse' or _header != 'NEW RELEASES':
        #    raise AssertionError("Not on the bestsellers page.")
            
    ########################################################################
    ########################################################################