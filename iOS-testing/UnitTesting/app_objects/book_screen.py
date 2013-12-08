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

class book_screen(base_app_object):
    
    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)
    
    ###main functions###
            
    def page_turn(self):
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"744.00","y":"384.00"})
    
    def iphone_page_turn(self):
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"290","y":"272"})

    def tap_midscreen(self):
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})

    def click_home_button(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader home off')]").click()
        time.sleep(3)

    def click_ToC(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader contents off')]").click()

    def click_top_info_bar(self):
        #self.driver.find_element_by_name('ipad reader info off').click()
        self.driver.find_element_by_xpath("//button[contains(@text,'reader info off')]").click()

    def click_social_tab(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader activity off')]").click()
    #self.driver.find_element_by_name('ipad reader activity off').click()

    def click_reader_settings(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader settings off')]").click()
    #self.driver.find_element_by_name('ipad reader settings off').click()

    def click_reader_refresh(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader bottombar refresh')]").click()
    #self.driver.find_element_by_name('ipad reader bottombar refresh').click()

    def progress_scoller(self):
        self.driver.find_element_by_xpath("//button[contains(@text,'reader_bottombar_marker')]").click()
    #self.driver.find_element_by_name('ipad_reader_bottombar_marker.png')

    def initial_progress_check(self):
        preprog_print = self.progress_scroller.find_element_by_xpath('/text[1]')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Current Book Progress:", preprog_print.text

    def scroll_progress(self):
        percent = self.driver.find_element_by_name("ipad_reader_bottombar_marker.png")
        #print percent.location
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "scrolling..."
        #self.driver.execute_script("mobile: swipe", {"touchCount": 1 , "startX":(percent.location['x']), "startY":(percent.location['y']),  "endX": 239, "endY": 976, "duration": 1.5 })
    #"startX": 63, "startY": 983,
    
    def post_progress_check(self):
        postprog_print = self.progress_scroller.find_element_by_xpath('/text[1]')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Current Book Progress:", postprog_print.text

    def progress_comparison(self):
        if self.initial_progress_check != self.post_progress_check:
            raise AssertionError("Book Progress Not Synced")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Book Progress Synced"

    def click_bookmark(self):
        self.driver.find_element_by_name('ipad reader bottombar').click()

### highlights ###

    def highlight_text(self):
        swiper = self.driver.find_element_by_xpath("//window[1]/scrollview[1]/webview[1]/text[1]")
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Highlight Coordinates:",swiper[0].location)
        swiper_location = swiper.location
        self.driver.execute_script("mobile: tap",{"tapCount":"2", "tapObject": swiper_location, "duration": 1})
        #return swiper.text
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Highlight:",swiper[0].text
        highlight = self.driver.find_elements_by_name('Highlight')
        highlight[0].click()
        #hightext = self.driver.find_element_by_xpath("//textview[contains(@text, swiper.text)]")
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Checking highlight against:",hightext
        #return hightext
    
    def assert_highlight(self, highlight_text):
        #self.driver.find_element_by_name('Web, Use of UIWebView').click()
        #self.driver.window_handles()
        print self.driver.window_handles
        self.driver.switch_to_window[0]
        css_check = self.driver.find_element_by_css('.highlight').text
        if css_check != self.highlight_text():
            raise AssertionError("highlight not yellow!")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "words properly yellowed (highlighted)"
        self.driver.execute_script("mobile: leaveWebView")

    def comment_on_highlight(self):
        #high_typer = self.driver.find_element_by_xpath("//textview[contains(@text,'UIATextView')]")
        high_typer = self.driver.find_elements_by_xpath("//window[1]/textview[2]")
        high_typer[0].send_keys("testtext")
        uikeyboard = self.driver.find_elements_by_name("Hide keyboard")
        uikeyboard[0].click()
        SAVE_HIGH = self.driver.find_elements_by_xpath("//window[1]/button[9]")
        SAVE_HIGH[0].click()
    
    def percent_path(self):
        percent_check = self.driver.find_element_by_xpath("//text[contains(@text,'%')]").text
        return percent_check

    def progress_check(self, percent_path):
        percent = self.percent_path()
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "initial book progress percentage: ", percent
        return percent

    def secondary_progress_check(self, percent_path):
        secondary_percent = self.percent_path()
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "percentage after book progress: ", secondary_percent
        return secondary_percent
    
    def tertiary_progress_check(self, percent_path):
        tertiary_percent = self.percent_path()
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "percentage after resync: ", tertiary_percent
        return tertiary_percent
    
    def quaternary_progress_check(self, secondary_progress_check, tertiary_progress_check, percent_path):
        #self.progress_check.percent.text
        if self.secondary_progress_check(percent_path) != self.tertiary_progress_check(percent_path):
            raise AssertionError("Book Progress Not Synced")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Book Progress Synced"