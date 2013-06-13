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
        
        #driver = webdriver.Firefox('/Library/Python/2.7/site-packages/webdriver/firefox/webdriver.py')
        driver.get(self.baseURL + '/')
        
        # an implicit wait sets the time to wait when trying to find elements for the entire test
        driver.implicitly_wait(15)
        driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a').click() #clicks on bestseller top book
        #driver.find_element_by_link_text('Register / Sign In').click()
        #driver.find_element_by_name('username').clear()
        #driver.find_element_by_name('username').send_keys('davidtennant@zolabooks.com')
        #driver.find_element_by_name('password').clear()
        #driver.find_element_by_name('password').send_keys('kingkong')
        #driver.find_element_by_name("submit").click()
        #driver.find_element_by_link_text("MY eBOOKS").click()
        
        #driver.find_element_by_css_selector("img.book").click()
        #rating_button = driver.find_element_by_class_name('pct-40').find_element_by_xpath("a") #Not For Me
        #if rating_button is None: raise Exception('rating button not found')
        #element_to_hover_over =  rating_button
        #hover = ActionChains(driver).move_to_element(element_to_hover_over)
        #hover.perform()
        #driver.execute_script('(arguments[0]).click()', rating_button)
        
        star_click = driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[2]/a").click() #1 star
        driver.execute_script("$(arguments[0]).click()", star_click) #clicks a star
        
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/section[2]/div/div/form[2]/a/div[2]')
        #driver.find_element_by_name("username").clear()
        #driver.find_element_by_name("username").send_keys("davidtennant@zolabooks.com")
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located(driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input').send_keys('davidtennant@zolabooks.com')))
        username = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input')
        if username is None: raise Exception('signup button not found')
        element_to_hover_over =  username
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script("$(arguments[0]).click()", username)
        username.clear() #all of the above is desperately attempting to interact with the 'username' field
        driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input').send_keys('davidtennant@zolabooks.com')
        driver.find_element_by_name('password').click().send_keys('kingkong')
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/section/div/section/div[3]/div/div/form/span/div[3]/a").click()
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[3]/a").click() #2 star
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[4]/a").click() #3 star
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/section/div/section/div[3]/div/div/form/span/div[4]/a").click()
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[5]/a").click() #4 star
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/section/div/section/div[3]/div/div/form/span/div[5]/a").click()
        driver.find_element_by_class_name('pct-40').find_element_by_xpath("a").click() #Not For Me
        driver.find_element_by_class_name('pct-60').find_element_by_xpath("form/span/div[6]/a").click() #5 star
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/section/div/section/div[3]/div/div/form/span/div[6]/a").click()
        driver.find_element_by_class_name("fancybox-skin").find_element_by_xpath('a').click() #close modal
        
        driver.quit()
        self.assert_(True, 'this is a placeholder')
        