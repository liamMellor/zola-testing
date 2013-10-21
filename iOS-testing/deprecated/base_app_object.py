from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class base_app_object():
    
    def __init__(self, appium_wrap):

        self.appium_wrap = appium_wrap
        self.driver = self.appium_wrap.driver
        self.wait = WebDriverWait(self.driver, 30)
        