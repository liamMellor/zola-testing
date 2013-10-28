import unittest #imports unit test/ability to run as pyunit test
from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.add_card import add_card
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.book import book
from UnitTesting.page_objects.find_friends import find_friends
from UnitTesting.app_objects.appium_wrapper import appium_wrapper
from UnitTesting.app_objects.login_screen import login_screen
from UnitTesting.app_objects.home_screen import home_screen
from UnitTesting.app_objects.my_ebooks_screen import my_ebooks_screen
from UnitTesting.app_objects.book_screen import book_screen
from UnitTesting.app_objects.social_tab import social_tab
import time
from subprocess import Popen

class test_app_book_insert(unittest.TestCase):
    
    def test_ui_comp(self):
        for emails in login_screen.book_insert_mails:
            outfile = open('appium_output_file.txt', 'a')
            cmd = ['appium', '--app', 'com.zolabooks.zolareader', '-U', '3bf568bbe558ec9a639b61b6181dca52f1d45bbe']
            p = Popen(cmd, stdout=outfile, stderr=outfile)
            appium_wrap = appium_wrapper(self)
        
            login_screen_inst = login_screen(appium_wrap)
            print p.returncode and p.pid
            try:
                time.sleep(5)
                login_screen_inst.book_insert_login(emails)
                
                home_screen_inst = home_screen(appium_wrap)
                home_screen_inst.click_my_ebooks()
                
                my_ebooks_screen_inst = my_ebooks_screen(appium_wrap)
                my_ebooks_screen_inst.confirm_book_title()
                
                my_ebooks_screen_inst.click_home_button()
                home_screen_inst.deregister_device()

                time.sleep(10)
            finally:
                p.kill(); print "Appium Killed"
                time.sleep(10)
