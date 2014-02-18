import time
import os
from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import random

class SomeTestSuite(unittest.TestCase):

    baseURL = "https://zola_stage:zola123@zolaqc.com"
    r = str( random.randint(0,1000000) )
    

    def test_PurchaseFlow(self):
        # start an instance of firefox and navigate to the zola qc site
        driver = webdriver.Firefox()
        
        #driver = webdriver.Firefox('/Library/Python/2.7/site-packages/webdriver/firefox/webdriver.py')
        driver.get(self.baseURL + '/')
        
        # an implicit wait sets the time to wait when trying to find elements for the entire test
        driver.implicitly_wait(30)
        
        # open top bestseller on homepage
        driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a').click()
        
        # looks for an element that can only exist while a modal is open without clicking, safety for the next step
        #driver.find_element_by_css_selector("html.no-js body.fancybox-lock div.fancybox-overlay div.fancybox-wrap div.fancybox-skin div.fancybox-outer div.fancybox-inner div.l-modal-800px div.l-modal-content section.l-570px div.padding-left-40px section.margin-bottom-20px div.expand-width div.ui-rating-bar div.pct-40 a.ui-rating-option-large")
        driver.find_element_by_xpath("/html/body/div[4]")
        
        purchase_button = driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/span/a')
#purchase_button.click()  # there's a bug in Selenium, so it thinks this is not displayed, so use JS
        driver.execute_script('$(arguments[0]).click()', purchase_button)
        signup_button = driver.find_element_by_xpath('//*[@id="sign-in-modal"]/div/section[2]/div/div[2]/div/a')
        if signup_button is None: raise Exception('signup button not found')
        element_to_hover_over =  signup_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', signup_button)
        
        driver.find_element_by_name("email").send_keys('jay+' + self.r + "@zolabooks.com")
        driver.find_element_by_name("confirm_email").send_keys('jay+' + self.r + "@zolabooks.com")
        
        driver.find_element_by_id("password").send_keys("password")
        driver.find_element_by_id("confirm_password").send_keys("password")
        
        driver.find_element_by_id("first_name").send_keys("Lin")
        driver.find_element_by_id("last_name").send_keys("Robinson")
    
        driver.find_element_by_id("bday_m").send_keys("10")
        driver.find_element_by_id("bday_d").send_keys("26")
        driver.find_element_by_id("bday_y").send_keys("1990")
        
        driver.find_element_by_id('signup_form').find_element_by_name("submit").click()
        
        driver.find_element_by_id("card_number").send_keys("378282246310005")
        driver.find_element_by_id("security_code").send_keys("266")
        
        driver.find_element_by_css_selector("#dk_container_pp_cc_exp_month > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("08").click()
        
        driver.find_element_by_css_selector("#dk_container_pp_cc_exp_year > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("2015").click()
        
        driver.find_element_by_id("pp_address_1").send_keys("106 Rico Drive North")
        driver.find_element_by_id("pp_city").send_keys("Morganville")
        
        driver.find_element_by_css_selector("#dk_container_pp_state > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("CA").click()
        
        driver.find_element_by_id("pp_zip").send_keys("07751")
        
        driver.find_element_by_name("save_billing_info").click()
        time.sleep(3)
        _elt = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/footer/a')
	element_to_hover_over =  _elt
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script("(arguments[0]).click()", _elt)
        time.sleep(8)
        _get_the_app = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/section/div/div[2]/a/div')
        _get_the_app
	_dbn = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/div[4]/a/div')
	element_to_hover_over =  _dbn
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script("(arguments[0]).click()", _dbn)
	_od = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/div/div[5]/a/div')
	element_to_hover_over =  _od
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script("(arguments[0]).click()", _od)
        time.sleep(8)
