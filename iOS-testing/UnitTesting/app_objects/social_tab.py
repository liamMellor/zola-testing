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

class social_tab(base_app_object):

    def __init__(self, appium_wrap):
        base_app_object.__init__(self, appium_wrap)

    def comment_check(self):
        REPLY_VIEW = self.driver.find_elements_by_xpath("//window[1]/tableview[1]/cell[1]/textview[2]")
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Reply View Text:", REPLY_VIEW[0].text
        if REPLY_VIEW[0].text != "test text":
            raise AssertionError("Comments do not match")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')),("Comments match!")

    def click_orange_reply(self):
        time.sleep(1)
        self.driver.find_element_by_xpath("//window[1]/tableview[1]/cell[1]/button[1]").click()

    def add_reply(self):
        reply_typer = self.driver.find_element_by_xpath("//window[1]/scrollview[2]/textview[3]")
        reply_typer.click()
        reply_typer.send_keys("testtext2")
        SOCIAL_SAVE = self.driver.find_element_by_name("ipad highlightcell reply")
        SOCIAL_SAVE.click()

    def check_see_comments(self):
        SEE_ALL_COMMENTS = self.driver.find_element_by_xpath("//button[contains(@text, 'SEE')]")
        # print SEE_ALL_COMMENTS.text
        if SEE_ALL_COMMENTS.text != "SEE 1 REPLY":
            raise AssertionError((datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Too many comments!")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Proper amount of comments"

    def add_second_reply(self):
        self.driver.find_element_by_xpath("//window[1]/tableview[1]/cell[1]/button[1]").click()
        self.driver.find_element_by_name("ipad_highlightcellreply_replyframe.png").send_keys("test text2")
        self.driver.find_element_by_xpath("//window[1]/scrollview[1]/button[2]").click()

    def check_second_reply(self):
        s_reply = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/text[8]")
        if s_reply.text != "test text2":
            raise AssertionError((datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Second Reply failure!")
        else:
            print ((datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Second Reply Matches!")
        cancel = self.driver.find_elements_by_name("cancel")
        cancel[0].click()

    def click_social_tab(self):
        try:
            self.driver.implicitly_wait(0)
            self.driver.find_element_by_name('ipad reader activity off').click()
            self.driver.implicitly_wait(10)
        except:
            self.driver.find_element_by_name('ipad reader activity on').click()