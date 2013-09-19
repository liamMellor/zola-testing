'''
Created on Jul 11, 2013

@author: emma
'''

from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
import selenium.common.exceptions as Exceptions
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.base_page_object import base_page_object

import time

class my_zola(base_page_object):
    
    
    def __init__(self,webd_wrap):
        base_page_object.__init__(self, webd_wrap)
        
    def confirm_page(self, _name=None):
        ''' raises AssertionError if page is incorrect '''
        
        _url = self._webd_wrap._driver.current_url
        _title = self._webd_wrap._driver.title
        
        # enables option to test for a specific username or just a general My Zola page
        if _name is None:
            _actual_title = _title
        else:
            _actual_title = 'Zola Books | ' + _name
        
        if not _url.startswith('https://zolaqc.com/profile') or _title != _actual_title:
            raise AssertionError("Not on My Zola page.")
        
    def click_my_zola(self):
        self.confirm_page()
        
        time.sleep(2)
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('div/a').click()
        
    def click_sign_in(self):
        ''' clicks the sign in button '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_link_text("Register / Sign In").click()
        
    def click_sign_out(self):
        ''' clicks the sign out link '''
        self.confirm_page()
    
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'h-user-toolbar')))    
        self._webd_wrap._driver.find_element_by_id('logout-link').click()

        
    ########################################################################
    ########################################################################
    
    def click_starred(self):
        ''' clicks the starred filter on the activities '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-buttonset-filterbar-3').find_element_by_xpath('ul/li[3]/a').click()
        
    def click_messages(self):
        ''' clicks the users message link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('ui-buttonset-filterbar-3').find_element_by_xpath('ul/li[2]/a').click()
    
    def click_my_followers(self):
        ''' clicks the users followers link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('page').find_element_by_xpath('div[1]/div[2]/a[1]').click()
    
    ########################################################################
    ################## Follower/Following Lists ############################
    ########################################################################
    
    def click_first_user(self):
        ''' clicks first user in followers or following list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[1]/h5/a').click()
        
    def click_follow_first_user(self):
        ''' clicks follow first user in followers or following list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-main-primary').find_element_by_xpath('div/section[1]/div/div/div[2]/a[1]').click()
        
    ########################################################################
    ########################################################################
        
    def first_activity_should_be_purchased_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        self.confirm_page()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'activity-container')), 'no activities')
        
        try:
            actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
            
        if actual != _book_title:
            raise AssertionError("Purchased book should have been %s but was %s" % (_book_title, actual))
    
    def first_activity_should_be_recommended_book(self, _book_title):
        ''' raises AssertionError if page title is not arg1 '''
        self.confirm_page()
        
        try:
            actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
        if actual != _book_title:
            raise AssertionError("Recommended book should have been %s but was %s" % (_book_title, actual))
        
    def first_activity_should_be_follow(self):
        ''' raises AssertionError if first activity is not a follow '''
        self.confirm_page()
        
        try:
            actual = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
        
        if not "following" in actual:
            raise AssertionError("First activity should have been a follow")
        
    def first_activity_should_be_rated_book(self, _book_title):
        ''' raises AssertionError if first activity is not a rate the proper book '''
        self.confirm_page()
        
        try:
            _actual_book_title = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
            _description = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
        
        if not "rated" in _description or _book_title != _actual_book_title:
            raise AssertionError("First activity should have been rated %s" % (_actual_book_title))
        
    def first_activity_should_be_added_book(self, _book_title):
        ''' raises AssertionError if first activity is not an add the proper book'''
        self.confirm_page()
        
        try:
            _actual_book_title = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[2]/ul/li/a[2]').text
            _description = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
        
        if "added" not in _description or _book_title.strip() != _actual_book_title.strip():
            raise AssertionError("First activity should have been added %s but was %s" % (_actual_book_title, _book_title))

    def first_starred_activity_should_be_from(self, _name):
        ''' raises AssertionError if first starred activity is not from _name '''
        self.confirm_page()
        
        try:
            _actual_name = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div/h5/a[2]').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No activity in the feed")
        
        if not _actual_name in _name:
            raise AssertionError("First starred activity should have been from %s but was %s" % (_name, _actual_name))
        
    def first_message_should_be_from(self, _name):
        ''' raises AssertionError if first message is not from _name '''
        self.confirm_page()
        
        try:
            _actual_name = self._webd_wrap._driver.find_element_by_id('activity-container').find_element_by_xpath('section[1]/div[1]/h5/a').text
        except Exceptions.NoSuchElementException:
            raise AssertionError("No message in the feed")
        
        if _actual_name.lower() != _name.lower():
            raise AssertionError("First message should have been from %s but was %s" % (_name.lower(), _actual_name.lower()))


    #############################################################################################################
    ###################################LINKS#####################################################################
    #############################################################################################################
    
    def click_followers_tab(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a/div/span[2]").click()
        #self._webd_wrap._driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/a/div/span[2]').click()
   
        
    def click_following_tab(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[2]/div/span[2]").click()
   
    
    def click_collection_tab(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/a[3]/span[2]").click()
   
    
    def click_collection_book_link(self):
        self._webd_wrap._driver.find_element_by_class_name("page").find_element_by_xpath("div/div[2]/a[4]/div/div/img").click()        

        
    def click_list_tab(self):
        self._webd_wrap._driver.find_element_by_class_name("l-section-border").find_element_by_xpath("li/a").click()
        
    def click_edit_profile(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/section/ul/li/a").click()
        
    def click_billing_info(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/section/ul/li[2]/a").click()
        
    def click_find_people(self):
        self._webd_wrap._driver.find_element_by_id("page").find_element_by_xpath("div/div[2]/section/ul/li[3]/a").click()
        
    def click_profile_picture(self):
        self._webd_wrap._driver.find_element_by_class_name("avatar-forced-dimensions").find_element_by_xpath("img").click()
        
    def click_messages_tab(self):
        self._webd_wrap._driver.find_element_by_class_name("list").find_element_by_xpath("li[2]/a").click()
        
    def click_starred_tab(self):
        self._webd_wrap._driver.find_element_by_class_name("list").find_element_by_xpath("li[3]/a").click()
        
    def sort_just_me(self):
        self._webd_wrap._driver.find_element_by_id("dk_container_category").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_class_name("dk_options_inner").find_element_by_xpath("li[2]/a").click()
        
    def sort_everything(self):
        self._webd_wrap._driver.find_element_by_id("dk_container_category").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_class_name("dk_options_inner").find_element_by_xpath("li[2]/a").click()    
        self._webd_wrap._driver.find_element_by_id("dk_container_category").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_class_name("dk_options_inner").find_element_by_xpath("li[2]/a").click()  
