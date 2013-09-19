from page_objects.modals.book_modal import book_modal
from page_objects.modals.sign_in_modal import sign_in_modal
from page_objects.modals.purchase_confirm_modal import purchase_confirm_modal
from page_objects.modals.recommend_modal import recommend_modal
from page_objects.modals.pledge_modal import pledge_modal
from page_objects.modals.bookseller_modal import bookseller_modal
from page_objects.modals.message_modal import message_modal
from page_objects.modals.user_modal import user_modal
from page_objects.modals.acp_modal import acp_modal


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class base_page_object():
    
    def __init__(self, webd_wrap):
        self._webd_wrap = webd_wrap
        self._driver = self._webd_wrap._driver
        self._wait = WebDriverWait(self._driver, 30)
        
        # add all modals as new attributes in this object
        self.book_modal = book_modal(webd_wrap)
        self.sign_in_modal = sign_in_modal(webd_wrap)
        self.purchase_confirm_modal = purchase_confirm_modal(webd_wrap)
        self.recommend_modal = recommend_modal(webd_wrap)
        self.pledge_modal = pledge_modal(webd_wrap)
        self.bookseller_modal = bookseller_modal(webd_wrap)
        self.acp_modal = acp_modal(webd_wrap)
        self.message_modal = message_modal(webd_wrap)
        self.user_modal = user_modal(webd_wrap)
    
    def get_title(self):
        ''' returns the title of the page '''
        return self.get_title()

    def click_on_link(self, _link_text):
        ''' clicks on a link with arg1 as the link text '''
        self._driver.find_element_by_link_text(_link_text).click()
        self._wait.until(EC.title_contains("Zola"))
        return self
        
    def page_title_should_be(self, _correct_title):
        ''' raises AssertionError if page title is not arg1 '''
        actual = self._driver.title
        if actual != _correct_title:
            raise AssertionError("Title should have been '%s' but was '%s'" % (_correct_title, actual))
        