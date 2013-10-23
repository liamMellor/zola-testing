import time
import os
from selenium import webdriver
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
import random
from datetime import datetime

class SomeTestSuite(unittest.TestCase):
    baseURL = "https://zola_stage:zola123@zolaqc.com"
    r = str( random.randint(0,1000000) )
    def setUp(self):
        # set up appium
        #app = "com.zolabooks.zolareader"
        app = os.path.join(os.path.dirname(__file__),
                           '/Users/Zola/Downloads/zola-mobile-Reading-Page-Performance/build/Sim-iphonesimulator',
                           'Zola.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
                                      command_executor='http://127.0.0.1:4723/wd/hub',
                                      desired_capabilities={
                                      'browserName': 'iOS',
                                      'platform': 'Mac',
                                      'version': '7.0',
                                      'app': app
                                      })
        self._values = []
    
    def test_PurchaseFlow(self):
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Light Account Creation"
        # start an instance of firefox and navigate to the zola qc site
        driver = webdriver.Firefox()
        
        #driver = webdriver.Firefox('/Library/Python/2.7/site-packages/webdriver/firefox/webdriver.py')
        driver.get(self.baseURL + '/')
        
        # an implicit wait sets the time to wait when trying to find elements for the entire test
        driver.implicitly_wait(90)
        
        # open top bestseller on homepage
        driver.find_element_by_id('best-sellers').find_element_by_xpath('ul/li/a').click()
        
        # looks for an element that can only exist while a modal is open without clicking, safety for the next step
        #driver.find_element_by_css_selector("html.no-js body.fancybox-lock div.fancybox-overlay div.fancybox-wrap div.fancybox-skin div.fancybox-outer div.fancybox-inner div.l-modal-800px div.l-modal-content section.l-570px div.padding-left-40px section.margin-bottom-20px div.expand-width div.ui-rating-bar div.pct-40 a.ui-rating-option-large")
        driver.find_element_by_xpath("/html/body/div[4]")
        
        purchase_button = driver.find_element_by_class_name('l-230px').find_element_by_xpath('div/div/span/a')
        #purchase_button.click()  # there's a bug in Selenium, so it thinks this is not displayed, so use JS
        driver.execute_script('$(arguments[0]).click()', purchase_button)
        signup_button = driver.find_element_by_xpath('//*[@id="sign-in-modal"]/div/section[2]/div/div[2]/div/a')
        if signup_button is None: raise Exception('signup button not found')
        element_to_hover_over =  signup_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('(arguments[0]).click()', signup_button)
        
        driver.find_element_by_name("email").send_keys('jay+' + self.r + "@zolabooks.com")
        driver.find_element_by_name("confirm_email").send_keys('jay+' + self.r + "@zolabooks.com")
        
        driver.find_element_by_id("password").send_keys("password")
        driver.find_element_by_id("confirm_password").send_keys("password")
        
        driver.find_element_by_id("first_name").send_keys("Lin")
        driver.find_element_by_id("last_name").send_keys("Robinson")
    
        driver.find_element_by_id("bday_m").send_keys("10")
        driver.find_element_by_id("bday_d").send_keys("26")
        driver.find_element_by_id("bday_y").send_keys("1990")
        
        driver.find_element_by_id('signup_form').find_element_by_name("submit").click()
        
        driver.find_element_by_id("card_number").send_keys("378282246310005")
        driver.find_element_by_id("security_code").send_keys("266")
        
        driver.find_element_by_css_selector("#dk_container_pp_cc_exp_month > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("08").click()
        
        driver.find_element_by_css_selector("#dk_container_pp_cc_exp_year > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("2015").click()
        
        driver.find_element_by_id("pp_address_1").send_keys("106 Rico Drive North")
        driver.find_element_by_id("pp_city").send_keys("Morganville")
        
        driver.find_element_by_css_selector("#dk_container_pp_state > a.dk_toggle > span.dk_label").click()
        driver.find_element_by_link_text("CA").click()
        
        driver.find_element_by_id("pp_zip").send_keys("07751")
        
        driver.find_element_by_name("save_billing_info").click()
        time.sleep(10)
        _purchase_button = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/footer/a')
        element_to_hover_over =  _purchase_button
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        driver.execute_script('$(arguments[0]).click()', _purchase_button)
        time.sleep(8)
        _get_the_app = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div/div/section[2]/div/section[2]/div/section/div/div[2]/a/div')
        _get_the_app
        time.sleep(1)
        #driver.wait.until(EC.invisibility_of_element_located((By.ID, 'receive_author_emails')))
       
#         _elt2 = driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
#         driver.execute_script("(arguments[0]).click()", _elt2)
        
        # confirms the modal is gone
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Light Account Creation Complete"
        driver.quit()
    
         
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert().text
            return True
        except:
            return False
         
     
    def test_ui_computation(self):

        self.driver.implicitly_wait(180)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Beginning Appium Test"
        buttons = self.driver.find_elements_by_tag_name('button')
        text = self.driver.find_elements_by_tag_name('textField')
        text[0].click()
        text[0].send_keys('jay+' + self.r + "@zolabooks.com")
        secure = self.driver.find_elements_by_tag_name("secure")
        secure[0].click()
        secure[0].send_keys("password")
        #secure[0].send_keys("\n")
        #login = self.driver.find_elements_by_name("ipad login loginbutton")
        buttons[0].click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Logging in..."
        time.sleep(5)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Log in Succesful"
        ebooks = self.driver.find_elements_by_xpath('//window[1]/button[2]')
        ebooks[0].click()
        #buttons[1].click()
        time.sleep(2)
        download = self.driver.find_elements_by_name('ipad bookdetail download')
        download[0].click()
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Downloading Book..."
        time.sleep(7)
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Download Complete"
        #the below lines turn the pages so that we can highlight text
        page_turn = self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"744.00","y":"384.00"})
        page_turn
        time.sleep(1)
        page_turn2 = self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"744.00","y":"384.00"})
        page_turn2
        time.sleep(1)
        page_turn3 = self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"744.00","y":"384.00"})
        page_turn3
        time.sleep(1)
        page_turn4= self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"744.00","y":"384.00"})
        page_turn4
        time.sleep(1)
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
#         settings = self.driver.find_elements_by_name('ipad reader settings off')
#         settings[0].click()
#         helvetica = self.driver.find_elements_by_name('Helvetica')
#         helvetica[0].click()
#         georgia = self.driver.find_elements_by_name('Georgia')
#         georgia[0].click()
#         #buttons = self.driver.find_elements_by_tag_name('button')
#         buttons = self.driver.find_elements_by_tag_name('button')
#         buttons[12].click()
#         buttons[13].click()
#         buttons[14].click()
#         buttons[15].click()
#         buttons[13].click()
#         small = self.driver.find_elements_by_name('ipad settings smalllineheight')
#         small[0].click()
#         medium = small = self.driver.find_elements_by_name('ipad settings mediumlineheight')
#         medium[0].click()
#         large = self.driver.find_elements_by_name('ipad settings largelineheight')
#         large[0].click()
#         verylarge = self.driver.find_elements_by_name('ipad settings verylargelinehei')
#         verylarge[0].click()
#         medium[0].click()
#         buttons[20].click()
#         buttons[20].click()
#         buttons[21].click()
#         buttons[21].click()
#         general = self.driver.find_elements_by_name('GENERAL')
#         general[0].click()
#         sepia = self.driver.find_elements_by_name('SEPIA')
#         sepia[0].click()
#         night = self.driver.find_elements_by_name('NIGHT READING')
#         night[0].click()
#         pubdef = self.driver.find_elements_by_name('DEFAULT')
#         pubdef[0].click()
        elements = self.driver.find_elements_by_name('ipad_reader_bottombar_marker.png')
        elements[0].click()
        swiper = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/webview[1]/text[1]")
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Highlight Coordinates:",swiper[0].location)
        swiper_location = swiper[0].location
        self.driver.execute_script("mobile: tap",{"tapCount":"2", "tapObject": swiper_location, "duration": 1})
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Highlight:",swiper[0].text
        highlight = self.driver.find_elements_by_name('Highlight')
        highlight[0].click()
        hightext = self.driver.find_elements_by_xpath("//window[1]/textview[1]")
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Checking highlight against:",hightext[0].text
#         if swiper[0].text != hightext[0].text:
#             raise AssertionError("Highlights do not match")
#         else:
#             print ("Highlights match")
        high_typer = self.driver.find_elements_by_xpath("//window[1]/textview[2]")
        high_typer[0].send_keys("testtext")
        #share_checkbox = self.driver.find_elements_by_xpath("//window[1]/button[3]")
        #share_checkbox[0].click()
        hightext[0].click()
        uikeyboard = self.driver.find_elements_by_name("Hide keyboard")
        uikeyboard[0].click()
        SAVE_HIGH = self.driver.find_elements_by_xpath("//window[1]/button[9]")
        SAVE_HIGH[0].click()
        #text1 = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/webview[1]/text[3]")
        #print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "First Reply:", text1[0].text
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        home = self.driver.find_elements_by_name('ipad reader home off')
        home[0].click()
        time.sleep(2)
        sync = self.driver.find_elements_by_xpath('//window[1]/button[3]')
        sync[0].click()
        read_now = self.driver.find_elements_by_name('ipad bookdetail readnow')
        read_now[0].click()
        time.sleep(5)
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        SOCIAL_BUTTON = self.driver.find_elements_by_xpath("//window[1]/button[4]")
        SOCIAL_BUTTON[0].click()
        REPLY_VIEW = self.driver.find_elements_by_xpath("//window[1]/tableview[1]/cell[1]/textview[2]")
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Reply View Text:", REPLY_VIEW[0].text
        if REPLY_VIEW[0].text != "test text":
            raise AssertionError("Replies do not match")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')),("Replies match!")
        #######BROKEN UNTIL HIGHLIGHT BUG FIXED#######
        #SOCIAL_REPLY = self.driver.find_elements_by_xpath("//window[1]/tableview[1]/cell[1]/button[1]")
        #SOCIAL_REPLY[0].click()
        #clicks reply/see all comments button
        #reply_typer = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/textview[3]")
        #reply_typer[0].send_keys("testtext2")
        #adds second reply
        #SOCIAL_SAVE = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/button[2]")
        #SOCIAL_SAVE[0].click()
        #SEE_ALL_COMMENTS = self.driver.find_elements_by_xpath("//window[1]/tableview[1]/cell[1]/button[1]")
        #SEE_ALL_COMMENTS[0].click()
        #print SEE_ALL_COMMENTS[0].text
        #RED_REPLY = self.driver.find_elements_by_xpath("//window[1]/scrollview[1]/text[8]")
        #print RED_REPLY[0].text
        #if RED_REPLY[0].text != "testtext2":
        #    raise AssertionError("Replies do not match")
        #else:
        #    print ("Replies match!")
        #_cancel = self.driver.find_elements_by_name("cancel")
        #_cancel[0].click()
        #unk_var3 = self.driver.find_elements_by_xpath("//window[1]/button[4]")
        #unk_var3[0].click()
        #save = self.driver.find_elements_by_name("ipad highlightmodal save")
        #save[0].click()
        ##############################################
        SOCIAL_BUTTON = self.driver.find_elements_by_xpath("//window[1]/button[4]")
        SOCIAL_BUTTON[0].click()
        #self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        self.driver.execute_script("mobile: swipe", {"touchCount": 1 , "startX": 63, "startY": 983, "endX": 239, "endY": 976, "duration": 0.5 })
        #above line swipes marker
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        time.sleep(3)
        _progress = self.driver.find_element_by_name("ipad_reader_bottombar_marker.png").find_element_by_xpath('/text[1]')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Current Book Progress:", _progress.text
        #self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        home = self.driver.find_elements_by_name('ipad reader home off')
        home[0].click()
        time.sleep(2)
        home_nav = self.driver.find_elements_by_name('ipad nav home off')
        home_nav[0].click()
        gear = self.driver.find_elements_by_name('ipad landing gear')
        gear[0].click()
        dereg = self.driver.find_elements_by_name('ipad information deregister')
        dereg[0].click()
        time.sleep(1)
        yes = self.driver.find_elements_by_name('YES')
        yes[0].click()
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Logging out to check progress..."
        ###recheck for progress, login process###
        self.driver.implicitly_wait(90)
        buttons = self.driver.find_elements_by_tag_name('button')
        text = self.driver.find_elements_by_tag_name('textField')
        text[0].click()
        text[0].send_keys('jay+' + self.r + "@zolabooks.com")
        secure = self.driver.find_elements_by_tag_name("secure")
        secure[0].click()
        secure[0].send_keys("password")
        #secure[0].send_keys("\n")
        #login = self.driver.find_elements_by_name("ipad login loginbutton")
        buttons[0].click()
        time.sleep(10)
        #self.driver.switch_to_alert().mainWindow
        ebooks = self.driver.find_elements_by_xpath("//window[1]/button[2]")
        ebooks[0].click()
        #buttons[1].click()
        time.sleep(2)
        download = self.driver.find_elements_by_name('ipad bookdetail download')
        download[0].click()
        time.sleep(5)
        #self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        ###second login complete###
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Relogging complete"
        self.driver.execute_script("mobile: tap",{"touchCount":"1","x":"0.63","y":"0.25"})
        _progress_check = self.driver.find_element_by_name("ipad_reader_bottombar_marker.png").find_element_by_xpath('/text[1]')
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Current Book Progress:", _progress_check.text
        if _progress_check.text != _progress.text:
            raise AssertionError("Book Progress Not Synced")
        else:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Book Progress Synced"
        time.sleep(10)
        home2 = self.driver.find_elements_by_name('ipad reader home off')
        home2[0].click()
        time.sleep(2)
        home_nav2 = self.driver.find_elements_by_name('ipad nav home off')
        home_nav2[0].click()
        #self.driver.find_element_by_name('ipad landing gear').click()
        self.driver.execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 730, "y": 98 })
        dereg2 = self.driver.find_elements_by_name('ipad information deregister')
        dereg2[0].click()
        time.sleep(1)
        yes2 = self.driver.find_elements_by_name('YES')
        yes2[0].click()
        print (datetime.now().strftime('%Y-%m-%d %H:%M:%S')), "Master suite complete"
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
