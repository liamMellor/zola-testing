from selenium.webdriver.common.by import By
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.app_objects.base_app_object import base_app_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import random
import os
from UnitTesting.app_objects.home_screen import home_screen
from UnitTesting.app_objects.appium_wrapper import appium_wrapper
from UnitTesting.app_objects.my_ebooks_screen import my_ebooks_screen

class login_screen(base_app_object):
    book_insert_mails = ["jay+908062@zolabooks.com",
                         
                         "jay+803668@zolabooks.com",
                         
                         "jay+324332@zolabooks.com",
                         
                         "jay+895285@zolabooks.com",
                         
                         "jay+720579@zolabooks.com",
                         
                         "jay+500820@zolabooks.com",
                         
                         "jay+978087@zolabooks.com",
                         
                         "jay+364289@zolabooks.com",
                         
                         "jay+16786@zolabooks.com",
                         
                         "jay+419559@zolabooks.com",
                         
                         "jay+503109@zolabooks.com",
                         
                         "jay+675687@zolabooks.com",
                         
                         "jay+26378@zolabooks.com",
                         
                         "jay+624314@zolabooks.com",
                         
                         "jay+849468@zolabooks.com",
                         
                         "jay+206212@zolabooks.com",
                         
                         "jay+112525@zolabooks.com",
                         
                         "jay+575004@zolabooks.com",
                         
                         "jay+981331@zolabooks.com",
                         
                         "jay+359305@zolabooks.com",
                         
                         "jay+566838@zolabooks.com",
                         
                         "jay+818047@zolabooks.com",
                         
                         "jay+262822@zolabooks.com",
                         
                         "jay+878359@zolabooks.com",
                         
                         "jay+478361@zolabooks.com",
                         
                         "jay+284899@zolabooks.com",
                         
                         "jay+663444@zolabooks.com",
                         
                         "jay+521737@zolabooks.com",
                         
                         "jay+165452@zolabooks.com",
                         
                         "jay+154079@zolabooks.com",
                         
                         "jay+806217@zolabooks.com",
                         
                         "jay+75223@zolabooks.com",
                         
                         "jay+1603@zolabooks.com",
                         
                         "jay+65641@zolabooks.com",
                         
                         "jay+672402@zolabooks.com",
                         
                         "jay+358509@zolabooks.com",
                         
                         "jay+260533@zolabooks.com",
                         
                         "jay+905734@zolabooks.com",
                         
                         "jay+225981@zolabooks.com",
                         
                         "jay+91553173@zolabooks.com",
                         
                         "jay+46855481@zolabooks.com",
                         
                         "jay+75530130@zolabooks.com",
                         
                         "jay+11401622@zolabooks.com",
                         
                         "jay+35262801@zolabooks.com",
                         
                         "jay+55918936@zolabooks.com",
                         
                         "jay+25449492@zolabooks.com",
                         
                         "jay+18076276@zolabooks.com",

                         "jay+18113958@zolabooks.com",
                         
                         "jay+292872@zolabooks.com",
                         
                         "jay+48286118@zolabooks.com"]
                         
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)
    
    def textfield(self):
        self.driver.find_element_by_xpath('//window[1]/textfield[1]')
    
    def log_in(self):
        time.sleep(3)
        try:
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Appium Test"
            buttons = self.driver.find_elements_by_tag_name('button')
            text = self.driver.find_elements_by_xpath('//window[1]/textfield[1]')
            text[0].click()
            text[0].send_keys("jay+" + self.appium_wrap.rand_username_int + "@zolabooks.com")
            secure = self.driver.find_elements_by_xpath("//window[1]/secure[1]")
            secure[0].click()
            secure[0].send_keys("password")
            #secure[0].send_keys("\n")
            #login = self.driver.find_elements_by_name("ipad login loginbutton")
            buttons[0].click()
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Logging in..."
            time.sleep(40)
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Log in Succesful"
    
    def book_insert_login(self, emails):
        #for emails in (self.book_insert_mails):
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Appium Test"
            buttons = self.driver.find_elements_by_tag_name('button')
            text = self.driver.find_elements_by_xpath('//window[1]/textfield[1]')
            text[0].click()
            text[0].send_keys(emails)
            secure = self.driver.find_elements_by_xpath("//window[1]/secure[1]")
            secure[0].click()
            secure[0].send_keys("password")
            #secure[0].send_keys("\n")
            #login = self.driver.find_elements_by_name("ipad login loginbutton")
            buttons[0].click()
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Logging in..."
            time.sleep(40)
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Log in Succesful"

    def login_check(self):
        app_home_screen = home_screen(self.appium_wrap)
        app_my_ebooks_screen = my_ebooks_screen(self.appium_wrap)
        try:
            self.driver.implicitly_wait(0)
            self.driver.find_element_by_xpath('//window[1]/textfield[1]')
            self.driver.implicitly_wait(10)
            self.log_in()
    #self.driver.find_element_by_xpath('//window[1]/textfield[1]').location['y'] == 212 and self.driver.find_element_by_xpath('//window[1]/textfield[1]').location['x'] == 182:
            # app_home_screen.deregister_device()
            
        #   app_home_screen.refresh()
        except:
            #cog = self.driver.find_element_by_xpath('//window[1]/button[4]')
            #cog.size['width'] == 33 and cog.size['height'] == 26
            #app_home_screen.refresh()
            app_home_screen.deregister_device()
            self.log_in()
    #    app_home_screen.refresh()
    #       cog = self.driver.find_element_by_xpath('//window[1]/button[4]')
    #       cog.size['width'] == 33 and cog.size['height'] == 26
    #       app_home_screen.deregister_device()
#       self.log_in()
        #   app_home_screen.refresh()