from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CategoryToBookmodalSide(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://zola_stage:zola123@zolaqc.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_category_to_bookmodal_side(self):
        driver = self.driver
        driver.get(self.base_url + "/category/graphic-novels-comics/books")
        driver.find_element_by_class_name("rating").find_element_by_xpath("a/img").click()
        driver.find_element_by_class_name('l-570px').find_element_by_xpath('div/section/div[3]/div/div/a[2]')
    
        
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

