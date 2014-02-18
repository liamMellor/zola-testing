from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class FollowerTabSide(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://zola_stage:zola123@zolaqc.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_follower_tab_side(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Register / Sign In").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("davidtennant@zolabooks.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kingkong")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_class_name("user-avatar").find_element_by_xpath("a/img").click()
        #driver.find_element_by_class_name("wrapper").find_element_by_xpath("div[4]/ul/li[2]/a").click()
        #/html/body/div[3]/header/div/div[4]/ul/li[2]/a
        #/html/body/div[3]/header/div/div[4]/div/a/img
        driver.find_element_by_class_name("mod-info").find_element_by_xpath("span[2]").click()
        #/html/body/div[3]/div/div[2]/a/div/span[2]
        driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("header/h2")
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
#     
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