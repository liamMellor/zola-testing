'''
Created on Jul 1, 2013

@author: padelstein
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from robot.libraries.BuiltIn import BuiltIn



import time

class Home:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self._webd_wrap = BuiltIn().get_library_instance('WebDriverWrapper')
        
    def confirm_page(self):
        ''' raises assertion error if page is incorrect '''
        
        # checks for the feed webelement to confirm this is the homepage
        #self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'feed')), 'feed not present')
        
        _title = self._webd_wrap._driver.title
        
        if not _title.startswith('Zola Books | Zola Books:'):
            raise AssertionError("Not on the home page.")

    def click_on_link(self, _link_text):
        ''' clicks on a link with arg1 as the link text '''
        self._webd_wrap._driver.find_element_by_link_text(_link_text).click()
        self._webd_wrap.wait.until(EC.title_contains("Zola"))

    ########################################################################
    #######################MAIN PAGE LINKS##################################
    ########################################################################

    def click_first_bestseller(self):
        ''' clicks the first item in the bestseller list '''
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'best-sellers')), 'bestseller list not present')
        
        _bestseller = self._webd_wrap._driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a')
        self._webd_wrap._driver.execute_script("(arguments[0]).click()", _bestseller)
        
    def click_category(self, _category):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('s-browse-by-category').find_element_by_link_text(_category).click()
        
    def click_zola_network(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/a').click()
        
    def click_see_all_fiction(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_elements_by_css_selector("section[class='l-section-carousel c-bg-tan']")[0].find_element_by_xpath('div[1]/div[2]/a').click()
        
    def click_see_all_non_fiction(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_elements_by_css_selector("section[class='l-section-carousel c-bg-tan']")[1].find_element_by_xpath('div[1]/div[2]/a').click()
        
    ########################################################################
    #######################NAVIGATION BAR LINKS#############################
    ########################################################################

    def hover_over_category_dropdown(self):
        ''' hovers the mouse over the category drop down menu '''
        self.confirm_page()
        
        _element = self._webd_wrap._driver.find_element_by_id("h-shop-by-category").find_element_by_xpath("h2/a")
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        
    def hover_over_connect_dropdown(self):
        ''' hovers the mouse over the connect drop down menu '''
        self.confirm_page()
        
        _element = self._webd_wrap._driver.find_element_by_id("h-connect").find_element_by_xpath("h2/a")
        _hov = ActionChains(self._webd_wrap._driver).move_to_element(_element)
        _hov.perform()
        
    def click_wishlist(self):
        self.confirm_page()
        self._webd_wrap.wait.until(EC.presence_of_element_located((By.ID, 'h-user-toolbar')))
        
        self._webd_wrap._driver.find_element_by_id('h-wishlist-link').find_element_by_xpath('a').click()
        
    def click_bestsellers(self):
        ''' clicks the link to the bestsellers list '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_xpath('div/nav/ul/li[3]/a').click()    
        
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
        
    def click_my_ebooks(self):
        ''' clicks the my ebooks link '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-user-personalized-toolbar').find_element_by_xpath('ul/li[1]/a').click()
        
    def click_deals(self):
        ''' clicks the deals link in the nav bar '''
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_link_text('DEALS').click()
        
    def click_about_zola(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_link_text('ABOUT ZOLA').click()
    
    def click_new_releases(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_link_text('NEW RELEASES').click()
        
    def click_find_great_ebooks(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_link_text('FIND GREAT eBOOKS').click()

    def click_home_icon(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-header').find_element_by_link_text('HOME').click()
        
    def click_zola_icon(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id('h-logo-link').find_element_by_xpath('a')

    ##############################################################################################################
    ####################################BOTTOM LINKS##############################################################
    ##############################################################################################################
    
    def click_bottom_about_zola(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li/a").click()
     
    def click_contact_us(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li[6]/a").click()  
        
    def click_help(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li[2]/a").click()
        
    def click_news(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li[5]/a").click()
        
    def click_privacy(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li[3]/a").click()
        
    def click_terms(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("list-inline").find_element_by_xpath("li[4]/a").click()
      
    def click_copyright_icon(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("site_logo").find_element_by_xpath("a").click()
        
    def click_copyright(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("g-footer-copyright").find_element_by_xpath("a").click()

    def check_copyright_page(self):
        ''' raises AssertionError if page is incorrect '''
        _actual_url = self._webd_wrap._driver.current_url
        if _actual_url != self._webd_wrap._baseURL + '/terms#':
            raise AssertionError("Not on copyright page.")
        
      
    def click_facebook_icon(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("g-footer").find_element_by_xpath("div/nav/ul[2]/li/a/span").click()
        
    def click_twitter_icon(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("g-footer").find_element_by_xpath("div/nav/ul[2]/li[2]/a/span").click()  
        
    ###################################################################################################################
    #######################################NEW RELEASE LINKS###########################################################
    ###################################################################################################################
        
    def click_fiction_new_releases_link(self, category, num):
        self.confirm_page()
        self._webd_wrap._driver.find_element_by_class_name("tabs-nav").find_element_by_xpath("li[" + str(num) + "]/a/span").click()
        
        _tabs = self._webd_wrap._driver.find_element_by_class_name("tabs-nav").find_elements_by_xpath('li')
        
        for tab in _tabs:
            if tab.get_attribute('class') == 'active':
                _active_tab = tab.find_element_by_xpath('a/span').text

        if _active_tab != category:
            raise AssertionError('the correct tab is not selected')
        
    def click_nonfiction_new_releases_link(self, category, num):
        self.confirm_page()
        self._webd_wrap._driver.find_element_by_class_name("l-main-primary").find_element_by_xpath("section[5]/div[2]/div/ul/li[" + str(num) + "]/a/span").click()
        
        _tabs = self._webd_wrap._driver.find_element_by_class_name("l-main-primary").find_elements_by_xpath('section[5]/div[2]/div/ul/li')
        
        for tab in _tabs:
            if tab.get_attribute('class') == 'active':
                _active_tab = tab.find_element_by_xpath('a/span').text

        if _active_tab != category:
            raise AssertionError('the correct tab is not selected')
        
    ##############################################################################################################
    ####################################SIDE LINKS################################################################
    ##############################################################################################################
        
    def click_more_zola_bestsellers(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("best-sellers").find_element_by_xpath("p/a").click()  
        
    def click_nyt_bestsellers(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("best-sellers").find_element_by_xpath("p[2]/a").click()
        
    def click_usa_today_bestsellers(self):  
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("best-sellers").find_element_by_xpath("p[3]/a").click()
        
    def click_the_feed(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_class_name("margin-bottom-50px").find_element_by_xpath("a/h2").click()
        
    def click_people_finder(self):
        self.confirm_page()
        
        self._webd_wrap._driver.find_element_by_id("people-finder").find_element_by_xpath("a/img").click()
        
    def click_first_user_in_feed(self):
        self.confirm_page()
         
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/ul/li[1]').find_element_by_class_name('avatar-forced-dimensions').click()      
     
    def click_zola_exclusives(self):
        self.confirm_page()
         
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/div').find_elements_by_class_name('other-categories')[0].find_element_by_xpath('a').click()            
                 
    def click_all_categories(self):    
        self.confirm_page()
         
        self._webd_wrap._driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('section/div').find_elements_by_class_name('other-categories')[1].find_element_by_xpath('a').click()         
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
    