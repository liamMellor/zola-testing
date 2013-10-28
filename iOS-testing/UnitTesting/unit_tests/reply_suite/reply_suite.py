'''
    Created on Jul 15, 2013
    
    @author: Jay
    '''
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

class test_app_full_suite(unittest.TestCase):
    
    def test_ui_comp(self):
        for num_books in appium_wrapper.num_books_options:
            appium_wrap = appium_wrapper(num_books)
            login_screen_inst = login_screen(appium_wrap)
            login_screen_inst.login_check()
            
            appium_wrap.get_screenshot()
            home_screen_inst = home_screen(appium_wrap)
            home_screen_inst.click_my_ebooks()
            appium_wrap.get_screenshot()
            my_ebooks_screen_inst = my_ebooks_screen(appium_wrap)
            my_ebooks_screen_inst.confirm_purchase(num_books)
            my_ebooks_screen_inst.click_first_book()
            book_screen_inst = book_screen(appium_wrap)
            book_screen_inst.tap_midscreen()
            for i in range(20):
                book_screen_inst.page_turn()
            book_screen_inst.highlight_text()
            appium_wrap.get_screenshot()
            book_screen_inst.comment_on_highlight()
            appium_wrap.get_screenshot()
            book_screen_inst.tap_midscreen()
            appium_wrap.get_screenshot()
            book_screen_inst.click_home_button()
            ##logout
            my_ebooks_screen_inst.click_home_button()
            home_screen_inst.deregister_device()
            login_screen_inst.log_in()
            home_screen_inst.click_my_ebooks()
            my_ebooks_screen_inst.click_first_book()
            
            book_screen_inst.tap_midscreen()
            book_screen_inst.click_social_tab()
            
            social_tab_inst = social_tab(appium_wrap)
            social_tab_inst.comment_check()
            appium_wrap.get_screenshot()
            social_tab_inst.click_orange_reply()
            social_tab_inst.add_reply()
            social_tab_inst.check_see_comments()
            appium_wrap.get_screenshot()
            book_screen_inst.click_home_button()
            my_ebooks_screen_inst.click_home_button()