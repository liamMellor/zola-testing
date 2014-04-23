from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
for browser in range(0,3):
     driver = None
     if browser is 0:
          driver = webdriver.Chrome('libs/chromedriver')
     if browser is 1:
          driver = webdriver.Firefox()
     if browser is 2:
          driver = webdriver.Safari('libs/selenium-server-standalone-2.41.0.jar')
     try:
          driver.get("http://bookish.com")
          print "Step 1 Complete"
          driver.find_element_by_css_selector("img[alt='Bookish']").click()
          print "Step 2 Complete"
     except Exception as e:
          print e
     finally:
          driver.quit()