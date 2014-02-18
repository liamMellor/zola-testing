'''
Created on Jun 13, 2013

@author: jsflax
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains


import random
import unittest

class SomeTestSuite(unittest.TestCase):

    baseURL = "https://zola_stage:zola123@zolaqc.com"
    r = str( random.randint(0,1000000) )
    

    def test_PurchaseFlow(self):
    
        # start an instance of firefox and navigate to the zola qc site
        driver = webdriver.Firefox()
        driver.get(self.baseURL + '/')
        driver.implicitly_wait(15)
        driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a').click() #clicks on bestseller top book
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[2]/a").click() #1 star
        username = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input')       
        login_modal = driver.find_element_by_id('login_modal')
        driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('username')[0], 'davidtennant@zolabooks.com')
        password = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[3]/input')       
        login_modal = driver.find_element_by_id('login_modal')
        driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('password')[0], 'kingkong')
        sign_in = driver.find_element_by_id('login_modal').find_element_by_xpath('div[3]/p/input')
        driver.execute_script('(arguments[0]).click()', sign_in)
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[3]/a").click() #2 star
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[4]/a").click() #3 star
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[5]/a").click() #4 star
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[6]/a").click() #5 star
        driver.find_element_by_class_name("fancybox-skin").find_element_by_xpath('a').click() #close modal
        
        driver.quit()
        self.assert_(True, 'this is a placeholder')
        