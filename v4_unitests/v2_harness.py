from v2.login import v2_LoginTest
import json

api_url = 'https://zolabooks.com/api/v2/'

class v2_harness():
    
    def __init__(self):
        global api_url
    
    def runner(self):
        login = v2_LoginTest(api_url)
        accountDict = login.activate();
        print accountDict[0]
        accountDict = accountDict[1]["data"]
        
        memberId = accountDict["member_id"]
        authToken = accountDict["auth_token"]
        deviceName = accountDict["device_name"]
        
v2_harness().runner()
        