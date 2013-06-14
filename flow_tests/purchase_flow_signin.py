'''
Created on Jun 14, 2013

@author: jsflax
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
        driver.implicitly_wait(30)
        driver.find_element_by_link_text('Register / Sign In').click()
        driver.find_element_by_class_name('ui-content-header-action').click()
        jay_user = 'jay+' + self.r + "@zolabooks.com"
        driver.find_element_by_name("email").send_keys(jay_user)
        elem = driver.find_element_by_name("email")
        
        elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
        elem.send_keys(Keys.CONTROL, 'c') #copy
        driver.find_element_by_name("confirm_email").send_keys(jay_user)
        
        driver.find_element_by_name("password").send_keys("kingkong")
        driver.find_element_by_name("confirm_password").send_keys("kingkong")
        
        driver.find_element_by_id("first_name").send_keys("Lin")
        driver.find_element_by_id("last_name").send_keys("Robinson")
    
        driver.find_element_by_id("bday_m").send_keys("10")
        driver.find_element_by_id("bday_d").send_keys("26")
        driver.find_element_by_id("bday_y").send_keys("1990")
        
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector('html.no-js body div#page.page div.wrapper div.l-full footer.pad-box-40px form a.t-action-secondary').click()
        driver.find_element_by_link_text('Sign Out').click()
        
        driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a').click()
        
        # looks for an element that can only exist while a modal is open without clicking, safety for the next step
        #driver.find_element_by_css_selector("html.no-js body.fancybox-lock div.fancybox-overlay div.fancybox-wrap div.fancybox-skin div.fancybox-outer div.fancybox-inner div.l-modal-800px div.l-modal-content section.l-570px div.padding-left-40px section.margin-bottom-20px div.expand-width div.ui-rating-bar div.pct-40 a.ui-rating-option-large")
        driver.find_element_by_xpath("/html/body/div[4]")
        
        purchase_button = driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/span/a')
#purchase_button.click()  # there's a bug in Selenium, so it thinks this is not displayed, so use JS
        driver.execute_script('$(arguments[0]).click()', purchase_button)
        
        username = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input')       
        login_modal = driver.find_element_by_id('login_modal')
        paste = (Keys.CONTROL, 'v')
        driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('username')[0], jay_user) #paste))
        #driver.execute_script('$(arguments[0]).val(paste(arguments[1]))', login_modal.find_elements_by_name('username')[0]) #paste))
        password = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[3]/input')       
        login_modal = driver.find_element_by_id('login_modal')
        driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('password')[0], 'kingkong')
        sign_in = driver.find_element_by_id('login_modal').find_element_by_xpath('div[3]/p/input')
        driver.execute_script('(arguments[0]).click()', sign_in)
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
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/div[2]/div/div/a")
        driver.find_element_by_id('uniform-receive_author_emails').find_element_by_xpath('span/input').click()
        
        #driver.find_element_by_class("position modal-purchase-book ui-action-1 ui-inline ui-235px").click()
        driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer").click()
        
        driver.quit()
        self.assert_(True, 'this is a placeholder')
        
        
        
        
        