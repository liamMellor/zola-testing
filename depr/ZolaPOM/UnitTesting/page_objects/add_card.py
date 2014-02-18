from UnitTesting.page_objects.base_page_object import base_page_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class add_card(base_page_object):
    def __init__(self, webd_wrap):
        base_page_object.__init__(self, webd_wrap)

    def get_page(self):
        #self._webd_wrap.open_page('/signup')
        return self

    def confirm_page(self):
        ''' raises AssertionError if page is incorrect '''
        
        self._webd_wrap.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'header-modal-capital'), 'CREDIT'), 'Not on the add card page.')
        
        _url = self._webd_wrap._driver.current_url
        
        if not _url.startswith(self._webd_wrap._baseURL + '/profile/add-card'):
            raise AssertionError("Not on the add card page.")
        
    ########################################################################
    ########################################################################
        
    def submit_new_cc_info(self):
        self.confirm_page()
        
        self.enter_cc_number()
        self.click_cc_month_dropdown()
        self.click_cc_year_dropdown()
        self.enter_cc_address()
        self.click_state_dropdown()
        self.enter_zip()
        self.click_cc_submit()
        
    def enter_cc_number(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("card_number").send_keys("378282246310005")
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("security_code").send_keys("266")
        
    def click_cc_month_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_month").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("08").click()
        
    def click_cc_year_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_cc_exp_year").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("2015").click()
            
    def enter_cc_address(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_address_1").send_keys("221B Baker Street")
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_city").send_keys("London")
        
    def click_state_dropdown(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("dk_container_pp_state").find_element_by_xpath("a").click()
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_link_text("CA").click()
    
    def enter_zip(self):
        self._webd_wrap._driver.find_element_by_id('add-payment-profile').find_element_by_id("pp_zip").send_keys("07751")
        
    def click_cc_submit(self):
        self._webd_wrap._driver.find_element_by_name("save_billing_info").click()

    
    