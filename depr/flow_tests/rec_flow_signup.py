from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
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

        
        driver.find_element_by_class_name("wrapper").find_element_by_xpath("nav/ul/li[3]/a").click()
        driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section")
        driver.find_element_by_class_name("rating").find_element_by_xpath("div/a").click()
        driver.find_element_by_class_name("fancybox-outer").find_element_by_xpath("div/div/div")

        recommend_button = driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        driver.execute_script("(arguments[0]).click()", recommend_button)
        
        driver.find_element_by_xpath("/html/body/div[3]/div/section/h3")

        #sign up
        signup_button = driver.find_element_by_xpath("/html/body/div[3]/div/section[3]/div/form/footer/a")
        if signup_button is None: raise Exception('signup button not found')
        element_to_hover_over = signup_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', signup_button)
        
        rand = random.randint(0,100000000000) #for generating random email address
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("jay+" +  str(rand) + "@zolabooks.com")
        driver.find_element_by_name("confirm_email").clear()
        driver.find_element_by_name("confirm_email").send_keys("jay+" + str(rand) + "@zolabooks.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("kingkong")
        driver.find_element_by_name("confirm_password").send_keys("kingkong")
        driver.find_element_by_id("first_name").send_keys("Lin")
        driver.find_element_by_id("last_name").send_keys("Robinson")
        driver.find_element_by_id("bday_m").send_keys("10")
        driver.find_element_by_id("bday_d").send_keys("26")
        driver.find_element_by_id("bday_y").send_keys("1990")
        driver.find_element_by_name("submit").click()
        
        
        #clicking skip this
        driver.find_element_by_css_selector('html.no-js body div#page.page div.wrapper div.l-full footer.pad-box-40px form a.t-action-secondary').click()


        driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section")
        driver.find_element_by_class_name("rating").find_element_by_xpath("div/a").click()
        driver.find_element_by_class_name("fancybox-outer").find_element_by_xpath("div/div/div")
        
        recommend_button = driver.find_element_by_class_name("l-230px").find_element_by_xpath("div/div/ul/li[3]/a")
        driver.execute_script("(arguments[0]).click()", recommend_button)
        
        
        #filling in fields
        send_to = driver.find_element_by_id('recommend-email-form').find_element_by_class_name('margin-left-255px').find_element_by_xpath('div/p/div/ul/li/input')
        recommend_email_form = driver.find_element_by_id('recommend-email-form')
        driver.execute_script('$(arguments[0]).val(arguments[1])', recommend_email_form.find_elements_by_class_name('textboxlist-bit-editable-input')[0], '1@zolabooks.com')

        message = driver.find_element_by_id('recommend-email-form').find_element_by_class_name('margin-left-255px').find_element_by_xpath('div/p[3]/textarea')        
        recommend_email_form = driver.find_element_by_id('recommend-email-form')
        driver.execute_script('$(arguments[0]).val(arguments[1])', recommend_email_form.find_elements_by_name('message')[0], 'test')
        
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
