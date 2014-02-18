from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains


class Category_Artarchdesign(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://zola_stage:zola123@zolaqc.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_category_artarchdesign(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        element = driver.find_element_by_class_name("wrapper").find_element_by_xpath("div[2]/h2/a")
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        driver.find_element_by_link_text("Romance & Erotica").click()
        driver.find_element_by_class_name("wrapper page page-with-sidebar").find_element_by_xpath("div/header/div/div/div/h4")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
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
