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
        driver.find_element_by_link_text("Register / Sign In").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("davidtennant@zolabooks.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kingkong")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_id("h-user-personalized-toolbar").find_element_by_xpath("ul/li[2]/a")
        #accessing connect menu
        element = driver.find_element_by_class_name("wrapper").find_element_by_xpath("div[3]/h2/a")
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        
        driver.find_element_by_link_text("Booksellers").click()
        driver.find_element_by_class_name("header-topic-graphic").find_element_by_xpath("div/div/h4")
        driver.find_element_by_class_name("author").find_element_by_xpath("a/div/img").click()
        driver.find_element_by_class_name("l-960px").find_element_by_xpath("footer/a")

        
    #first pledge button
        pledge_button = driver.find_element_by_class_name("l-710px").find_element_by_xpath("section/p/a/img")
        if pledge_button is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', pledge_button)

 
    #second pledge button
        driver.find_element_by_class_name("margin-left-250px").find_element_by_xpath("p/label")
        pledge_button2 = driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a/img")
        if pledge_button2 is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button2
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', pledge_button2)
             


        driver.find_element_by_class_name("header-topic-graphic").find_element_by_xpath("div/div")
        bookstore_button = driver.find_element_by_class_name("author").find_element_by_xpath("a/div/img")
        #bookstore_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/section/div/a/div/img")
        if bookstore_button is None: raise Exception('bookstore button not found')
        element_to_hover_over =  bookstore_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('$(arguments[0]).click()', bookstore_button)
        

     
     #first unpledge button
        pledge_button = driver.find_element_by_class_name("l-710px").find_element_by_xpath("section/div[2]/a/img")
        if pledge_button is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', pledge_button)
        
     
    #second unpledge button
        driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a[2]")
        pledge_button2 = driver.find_element_by_class_name("l-modal-800px").find_element_by_xpath("section[2]/a/input")
        if pledge_button2 is None: raise Exception('pledge button not found')
        element_to_hover_over =  pledge_button2
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', pledge_button2)
        

    
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

