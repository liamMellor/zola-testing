from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains


class PledgeUnpledgePy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://zola_stage:zola123@zolaqc.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_pledge_unpledge_py(self):
        driver = self.driver
        driver.get(self.base_url + "/")
#         driver.find_element_by_link_text("Register / Sign In").click()
#         driver.find_element_by_name("username").clear()
#         driver.find_element_by_name("username").send_keys("davidtennant@zolabooks.com")
#         driver.find_element_by_name("password").clear()
#         driver.find_element_by_name("password").send_keys("kingkong")
#         driver.find_element_by_name("submit").click()
        #driver.find_element_by_id("h-user-personalized-toolbar").find_element_by_xpath("ul/li[2]/a")
        #element = driver.find_element_by_class_name("wrapper").find_element_by_xpath("div[3]/h2/a")
        #hov = ActionChains(driver).move_to_element(element)
        #hov.perform()
        
        driver.find_element_by_class_name("wrapper").find_element_by_xpath("nav/ul/li[3]/a").click()
        #/html/body/div[3]/header/div/nav/ul/li[3]/a
        #element = driver.find_element_by_class_name("wrapper").find_element_by_xpath("div[3]/h2/a")
        #hov = ActionChains(driver).move_to_element(element)
        #hov.perform()
        #driver.find_element_by_class_name("l-section-header-category c-bg-white").find_element_by_xpath("h2")
        #driver.find_element_by_xpath("/html/body/div[3]/div/div/header/h2")
        driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section")
        #driver.find_element_by_class_name("l-full c-bg-white").find_element_by_xpath("header")
        driver.find_element_by_class_name("rating").find_element_by_xpath("div/a").click()
        #/html/body/div[3]/div/div[3]/section[2]/div/div/a
        driver.find_element_by_class_name("fancybox-outer").find_element_by_xpath("div/div/div")
        #/html/body/div[4]/div/div/div/div/div/div
        recommend_button = driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        driver.execute_script("(arguments[0]).click()", recommend_button)
        
        
        #sign in modal
#         username = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[2]/input')
#         login_modal = driver.find_element_by_id('login_modal')
#         driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('username')[0], 'davidtennant@zolabooks.com')
#         password = driver.find_element_by_id('login_modal').find_element_by_class_name('margin-bottom-5px').find_element_by_xpath('p[3]/input')
#         login_modal = driver.find_element_by_id('login_modal')
#         driver.execute_script('$(arguments[0]).val(arguments[1])', login_modal.find_elements_by_name('password')[0], 'kingkong')
#         sign_in = driver.find_element_by_id('login_modal').find_element_by_xpath('div[3]/p/input')
#         driver.execute_script('(arguments[0]).click()', sign_in)

        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("davidtennant@zolabooks.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kingkong")
        driver.find_element_by_name("submit").click()
        
        
        
        driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section")
        #driver.find_element_by_class_name("l-full c-bg-white").find_element_by_xpath("header")
        driver.find_element_by_class_name("rating").find_element_by_xpath("div/a").click()
        #/html/body/div[3]/div/div[3]/section[2]/div/div/a
        driver.find_element_by_class_name("fancybox-outer").find_element_by_xpath("div/div/div")
        #/html/body/div[4]/div/div/div/div/div/div
        recommend_button = driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        driver.execute_script("(arguments[0]).click()", recommend_button)
        
        
        
        
        
        #filling in fields
        send_to = driver.find_element_by_id('recommend-email-form').find_element_by_class_name('margin-left-255px').find_element_by_xpath('div/p/div/ul/li/input')

        #/html/body/div[4]/div/div/div/div/div/div/form/section/div/section[2]/div/p/div/ul/li/input
        recommend_email_form = driver.find_element_by_id('recommend-email-form')

        driver.execute_script('$(arguments[0]).val(arguments[1])', recommend_email_form.find_elements_by_class_name('textboxlist-bit-editable-input')[0], '1@zolabooks.com')

        message = driver.find_element_by_id('recommend-email-form').find_element_by_class_name('margin-left-255px').find_element_by_xpath('div/p[3]/textarea')
        

        recommend_email_form = driver.find_element_by_id('recommend-email-form')

        driver.execute_script('$(arguments[0]).val(arguments[1])', recommend_email_form.find_elements_by_name('message')[0], 'test')

        #sign_in = driver.find_element_by_id('login_modal').find_element_by_xpath('div[3]/p/input')

        #driver.execute_script('(arguments[0]).click()', sign_in)
        
       # driver.find_element_by_class_name("margin-bottom-20px").find_element_by_xpath("label/div/span/input").click()
        #driver.find_element_by_name("share-with-followers").click()
        #share = driver.find_element_by_name("share_with_followers")
        #share_with_followers = driver.find_element_by_name("share_with_followers")
        #driver.execute_script('$(arguments[0].val(arguments[1])', share_with_followers.find_elements_by_name("share_with_followers")[0])
        
        checkbox = driver.find_element_by_id('uniform-share-with-followers').find_element_by_xpath('span/input')
        driver.execute_script("$(arguments[0]).click()", checkbox)

        send = driver.find_element_by_id("recommend-email-form").find_element_by_xpath("footer/input")
        driver.execute_script("(arguments[0]).click()", send)
        
        
        driver.find_element_by_id("email-form-confirm").find_element_by_xpath("section")
        exit_button = driver.find_element_by_class_name("fancybox-skin").find_element_by_xpath("a")
        driver.execute_script("(arguments[0]).click()", exit_button)

        
        
        
        
        

        

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
#     def is_alert_present(self):
#         try: self.driver.switch_to_alert()
#         except NoAlertPresentException, e: return False
#         return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()