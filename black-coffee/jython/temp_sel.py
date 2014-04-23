from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
for browser in range(0,1):
     driver = None
     if browser is 0:
          driver = webdriver.Firefox();
     try:
          driver.get("http://bookish.com")
          print "Step 1 Complete"
          tags0 = "input"
          attrs0 = ["[@type='text']", "[@placeholder='Search Book Title, Author, Keyword']", "[@x-webkit-speech='']", "[@class='ui-autocomplete-input']", "[@autocomplete='off']", "[@role='textbox']", "[@aria-autocomplete='list']", "[@aria-haspopup='true']"]
          strb0= "//" + tags0
          for r in range(0,len(attrs0)):
              strb0 += attrs0[r]
          #ele0 = driver.find_elements_by_css_selector(tags0 + attrs0[0])
          '''
          if len(ele0) > 1:
              for x0 in range(0,len(ele0)):
                  ele0 = ele0.find_elements_by_css_selector(tags0 + attrs[x0])
                  if len(ele0) < 2:
                      break
          '''
          print strb0
          driver.find_element_by_xpath( strb0 ).send_keys("WOO")
          print "Step 2 Complete"
     except Exception as e:
          print e
     finally:
          driver.quit()