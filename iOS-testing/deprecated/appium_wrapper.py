from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

from UnitTesting.page_objects.webdriver_wrapper import webdriver_wrapper
from UnitTesting.page_objects.sign_up import sign_up
from UnitTesting.page_objects.homepage import homepage
from UnitTesting.page_objects.add_card import add_card
from UnitTesting.page_objects.my_zola import my_zola
from UnitTesting.page_objects.book import book
from UnitTesting.page_objects.find_friends import find_friends
from UnitTesting.page_objects.bestsellers import bestsellers
from UnitTesting.page_objects.billing_info import billing_info

mode = 'new driver each time'  # if running a suite of tests, use 'same driver each time'
driver = None
zb_users = {}

class appium_wrapper():

    version = "7.0"  # other options: "6.1", "6.0"
    num_books_options = (1,3,10)
    apppath = '/Users/Zola/Downloads/zola-mobile-Reading-Page-Performance/build/Sim-iphonesimulator/Zola.app'

    def __init__(self, num_books):
        global driver, mode, zb_users
        ## setup webdriver for appium
        if mode == 'same driver each time' and driver:
            self.driver = driver
        else:
            self.driver = webdriver.Remote(
                                            command_executor='http://127.0.0.1:4723/wd/hub',
                                            desired_capabilities={
                                            'browserName': 'iOS',
                                            'platform': 'Mac',
                                            'version': self.version,
                                            'app': appium_wrapper.apppath
                                            })
            self.driver.implicitly_wait(80)
            driver = self.driver

        ## setup Zola Books user
        if num_books in zb_users:
            self.rand_username_int = zb_users[num_books]
        else:
            self.rand_username_int = str( random.randint(0,1000000) )
            zb_users[num_books] = self.rand_username_int

            if num_books > 22:  ## maximum number of bestsellers
                raise Exception('num_books value of '+str(num_books)+' is too high in '+self.__class__.
                    __name__)

            ## Use a browser to signup a new user and buy some books
            browser = webdriver_wrapper._browsers[0]
            self.webd_wrap = webdriver_wrapper(browser, self.rand_username_int)
            self.light_signup()
            for book_num in range(num_books):
                self.light_purchase(book_num)
            self.webd_wrap.close_the_browser()
            del self.webd_wrap


    def light_signup(self):
        page_homepage = homepage(self.webd_wrap)
        page_homepage.get_page()
        page_homepage.click_sign_in()
        page_homepage.sign_in_modal.click_sign_up()

        page_sign_up = sign_up(self.webd_wrap)
        email = page_sign_up.submit_new_member_info()

        page_find_friends = find_friends(self.webd_wrap)
        page_find_friends.click_skip_this()
        page_homepage.click_my_zola()
        page_my_zola = my_zola(self.webd_wrap)
        page_my_zola.click_billing_info()
        page_billing_info = billing_info(self.webd_wrap)
        page_billing_info.click_add_card()
        page_add_card = add_card(self.webd_wrap)
        page_add_card.submit_new_cc_info()

#page_homepage.click_sign_out()


    def light_purchase(self, book_num):
        page_homepage = homepage(self.webd_wrap)
        page_homepage.get_page()
        page_homepage.click_bestsellers()
        
        page_bestsellers = bestsellers(self.webd_wrap)
        page_bestsellers.click_bestseller_book(book_num)
        page_bestsellers.book_modal.click_buy()
        
        page_bestsellers.purchase_confirm_modal.click_receive_emails()
        page_bestsellers.purchase_confirm_modal.click_buy()
        page_bestsellers.purchase_confirm_modal.click_done()


        def close_appium(self):
            global mode
            if mode != 'same driver each time':
                self.driver.quit()





