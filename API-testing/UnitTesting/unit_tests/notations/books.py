from selenium import webdriver #imports selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib
import urllib2
import json
import random
import string
import re
import time
import os
from subprocess import Popen, PIPE
import subprocess


def getCode(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))

account1 = getCode(30, 'abcdefghijklmnopqrstuvwxyz')
account2 = getCode(30, 'abcdefghijklmnopqrstuvwxyz')
account3 = getCode(30, 'abcdefghijklmnopqrstuvwxyz')

zola_testing_device = 'zola-testing'
entry_id = '195954'
#api_url = 'https://zolaqc.com/api/v2/'
api_url = 'http://localhost/api/v2/'
#base_url = 'https://zolaqc.com/'
base_url = 'http://localhost/'
auth_url = re.sub(r'(https?://)(.*)', r'\1zola_stage:zola123@\2', base_url)


driver = webdriver.Firefox()
driver.set_window_size(360, 450)
driver.implicitly_wait(40)

def submit_new_member_info(name, email_prefix):
    driver.get(auth_url)
    for x in range(0,5):
        driver.find_element_by_id("h-logo-link").send_keys(Keys.COMMAND, Keys.SUBTRACT)
    driver.find_element_by_link_text("Register / Sign In").click()
    driver.find_element_by_xpath('//*[@id="sign-in-modal"]/div/section/div/div[2]/div/a').click()
    email = 'jay+' + email_prefix[:8] + '@zolabooks.com'
    register_email(email)
    register_password()
    register_name(name)
    register_birthday()
    register_submit()


def register_email(email):
    driver.find_element_by_id("email").send_keys(email)

def register_password():
    driver.find_element_by_id("password").send_keys("password")
    
def register_name(name):
    driver.find_element_by_id("first_name").send_keys(name)
        
def register_birthday():
    driver.find_element_by_id("bday_m").send_keys("10")
    driver.find_element_by_id("bday_d").send_keys("26")
    driver.find_element_by_id("bday_y").send_keys("1990")
    
def register_submit():
    driver.find_element_by_name("submit").click()

def go_to_book():
    driver.get(base_url + "book/how-to-survive-the-hunger-games/overview")
    driver.find_element_by_class_name('l-sidebar-primary').find_element_by_xpath('div/div/span/a').click()

def price_tag():
    _purchase_button = driver.find_element_by_xpath('//*[@id="book-action-btn-fat-195954"]/a')
    element_to_hover_over =  _purchase_button
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    driver.execute_script('(arguments[0]).click()', _purchase_button)

def submit_new_cc_info():
    enter_cc_number()
    click_cc_month_dropdown()
    click_cc_year_dropdown()
    enter_cc_address()
    click_state_dropdown()
    enter_zip()
    click_cc_submit()
    time.sleep(10)

def enter_cc_number():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("card_number").send_keys("378282246310005")
    driver.find_element_by_id('add-payment-profile').find_element_by_id("security_code").send_keys("266")
        
def click_cc_month_dropdown():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_month").find_element_by_xpath("a").click()
    driver.find_element_by_id('add-payment-profile').find_element_by_link_text("08").click()
    
def click_cc_year_dropdown():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_year").find_element_by_xpath("a").click()
    driver.find_element_by_id('add-payment-profile').find_element_by_link_text("2015").click()
            
def enter_cc_address():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_address_1").send_keys("221B Baker Street")
    driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_address_2").send_keys("London")
        
def click_state_dropdown():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_state").find_element_by_xpath("a").click()
    driver.find_element_by_id('add-payment-profile').find_element_by_link_text("CA").click()
    
def enter_zip():
    driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_zip").send_keys("07751")
        
def click_cc_submit():
    driver.find_element_by_name("save_billing_info").click()

def click_buy():
    _buy_button = driver.find_element_by_class_name("l-modal-section-content").find_element_by_xpath("footer/a[1]")
    driver.execute_script("(arguments[0]).click()", _buy_button)
    time.sleep(1)
        
def click_done():
    
    _elt = driver.find_element_by_id('sign-in-modal').find_element_by_xpath('footer/a')
    driver.execute_script("(arguments[0]).click()", _elt)
    
def accountSetUp(account, accountPre):
    submit_new_member_info(account, accountPre)
    time.sleep(5)
    go_to_book()
    price_tag()
    #submit_new_cc_info()
    click_buy()
    click_done()
    time.sleep(5)

def signOut():
    driver.get(base_url+'?ACT=12')

def driverExit():
    driver.quit()

def followAccount(account):
    driver.get(base_url + 'profile/' + account + '-')
    driver.find_element_by_xpath('//*[@id="page"]/div[1]/div[1]/section/section[2]/section/header/ul/li[1]/a').click()

def deviceLogin(account):
    print account
    loginUrl = api_url + 'device/login'

    loginValues = {'username' : account+'-',
                   'password' : 'password',
                   'device_name' : zola_testing_device }
    
    loginData = urllib.urlencode(loginValues)
    loginReq = urllib2.Request(loginUrl, loginData)
    loginResponse = urllib2.urlopen(loginReq)
    auth_creds = json.load(loginResponse)
    print 'DEVICE LOGIN : ' , auth_creds
    return(auth_creds)

def setNotation(auth_creds, shareAll=True, other_member_id=''):
    setNotationUrl = api_url + 'books/set_notation'

    if shareAll:
        shareAll = 'true'
        comment = 'TEST COMMENT SHARE ALL'
        highlight = 'TEST HIGHLIGHT SHARE ALL'
    else:
        shareAll = 'false'
        comment = 'TEST COMMENT EXPLICIT'
        highlight = 'TEST HIGHLIGHT EXPLICIT'
    setNotationValues = {'member_id' : auth_creds["data"]["member_id"],
                         'entry_id' : entry_id,
                         'start_char' : '1',
                         'end_char' : '2',
                         'comment_text' : comment,
                         'highlighted_text' : highlight,
                         'type' : '2',
                         'is_spointer' : 'false',
                         'in_reply_to' : '',
                         'page_number' : '',
                         'share_with_followers' : shareAll,
                         'share_with_member_id' : str(other_member_id),
                         'auth_member_id' : auth_creds["data"]["member_id"],
                         'auth_token' : auth_creds["data"]["auth_token"],
                         'device_name' : zola_testing_device }
    setNotationData = urllib.urlencode(setNotationValues)
    setNotationReq = urllib2.Request(setNotationUrl, setNotationData)
    setNotationResponse = urllib2.urlopen(setNotationReq)
    setNotationJSON = json.load(setNotationResponse)
    print 'SET NOTATION : ' , setNotationJSON
    
def getNotations(auth_creds, getMyNotations, other_member_id='', since_value=''):
    getNotationsUrl = api_url + 'books/get_notations'
    if getMyNotations:
        sharer_id = auth_creds["data"]["member_id"]
    else:
        sharer_id = other_member_id
    
    getNotationsValues = {'member_id' : sharer_id,
                          'entry_id' : entry_id,
                          'type' : '2',
                          'include_replies' : 'true',
                          'since' : since_value,
                          'count' : '',
                          'limit' : '1000',
                          'offset' : '0',
                          'auth_member_id' : auth_creds["data"]["member_id"],
                          'auth_token' : auth_creds["data"]["auth_token"],
                          'device_name' : zola_testing_device }

    getNotationsData = urllib.urlencode(getNotationsValues)
    getNotationsReq = urllib2.Request(getNotationsUrl + '?' + getNotationsData)
    getNotationsResponse = urllib2.urlopen(getNotationsReq)
    getNotationsJSON = json.load(getNotationsResponse)
    return [x for x in getNotationsJSON["data"]]
    
def countFollowingActivitiesForBook(auth_creds, since_value):
    countFollowingActivitiesForBookUrl = api_url + 'books/count_following_activities_for_book'
    countFollowingActivitiesForBookValues = {'entry_id' : entry_id,
                                             'since' : since_value,
                                             'auth_member_id' : auth_creds["data"]["member_id"],
                                             'auth_token' : auth_creds["data"]["auth_token"],
                                             'device_name' : zola_testing_device }

    countFollowingActivitiesForBookData = urllib.urlencode(countFollowingActivitiesForBookValues)
    countFollowingActivitiesForBookReq = urllib2.Request(countFollowingActivitiesForBookUrl + '?' +  countFollowingActivitiesForBookData)
    print countFollowingActivitiesForBookUrl + '?' +  countFollowingActivitiesForBookData
    countFollowingActivitiesForBookResponse = urllib2.urlopen(countFollowingActivitiesForBookReq)
    countFollowingActivitiesForBookJSON = json.load(countFollowingActivitiesForBookResponse)
    return countFollowingActivitiesForBookJSON["data"]["count"]

accountSetUp(account1, account1)
signOut()
accountSetUp(account2, account2)
followAccount(account1)
signOut()
timestamp_0 = time.time()
auth_credsAcc1 = deviceLogin(account1)
setNotation(auth_credsAcc1, True)
acc1_nots = getNotations(auth_credsAcc1, True)
print 'GET NOTATION acc1 :', acc1_nots
auth_credsAcc2 = deviceLogin(account2)
setNotation(auth_credsAcc2, True)
acc2_nots = getNotations(auth_credsAcc2, True)
print 'GET NOTATION acc2 :', acc2_nots
accountSetUp(account3, account3)
followAccount(account1)
driverExit()
print "timestamp_0 : " , timestamp_0
auth_credsAcc3 = deviceLogin(account3)
counted_activities_acc3_0 = countFollowingActivitiesForBook(auth_credsAcc3, since_value=int(time.time() - timestamp_0 + 0.5))
print 'COUNT FOLLOWING ACTIVITIES FOR BOOK : ', counted_activities_acc3_0
assert counted_activities_acc3_0 == 1
timestamp_1 = time.time()
print "timestamp_1 : ", timestamp_1
time.sleep(1)
setNotation(auth_credsAcc1, False, auth_credsAcc3["data"]["member_id"])
counted_activities_acc3_1 = countFollowingActivitiesForBook(auth_credsAcc3, since_value=int(time.time() - timestamp_0 + 0.5))
if counted_activities_acc3_1 != counted_activities_acc3_0 + 1:
    print 'counted_activities_acc3_0 =',counted_activities_acc3_0,' + 1 != countedactivities_acc3_1 =',countedactivities_acc3_1
    raise AssertionError("second count is not greater than previous count")
## currently, share_all notations are always counted
counted_activities_acc3_2 = countFollowingActivitiesForBook(auth_credsAcc3, since_value=int(time.time() - timestamp_1 + 0.5))
assert counted_activities_acc3_2 == counted_activities_acc3_1
## get all notations
## first without since, then with since, then compare
acc3_nots_all1 = getNotations(auth_credsAcc3, True)
print 'GET NOTATION acc3 :', acc3_nots_all1
acc3_nots_all2 = getNotations(auth_credsAcc3, True, since_value=int(time.time() - timestamp_0 + 0.5))
if acc3_nots_all1 != acc3_nots_all2:
    print list(set(acc3_nots_all1)-set(acc3_nots_all2)) + list(set(acc3_nots_all2)-set(acc3_nots_all1))
    raise AssertionError("get all notations and get notations since n seconds did not match")
#getNotations(auth_credsAcc3, False, auth_credsAcc1["data"]["member_id"])
## just get last notation
getNotations(auth_credsAcc3, True, since_value=int(time.time() - timestamp_1 + 0.5))
