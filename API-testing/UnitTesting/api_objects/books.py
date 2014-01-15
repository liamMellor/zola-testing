import urllib
import urllib2
import json

class books(self):

    swagger = 'swagger'
    entry_id = '195954'
    
    def deviceLogin(self, loginPage):
        loginUrl = 'https://zolaqc.com/api/v2/device/login'
        loginValues = {'username' : 'class-a',
                       'password' : 'kingkong',
                       'device_name' : 'swagger' }
        
        loginData = urllib.urlencode(loginValues)
        loginReq = urllib2.Request(loginUrl, loginData)
        loginResponse = urllib2.urlopen(loginReq)
        loginPage = json.load(loginResponse)
        print(loginPage)
        return(loginPage)

    def setNotation(self):
        setNotationUrl = 'https://zolaqc.com/api/v2/books/set_notation'
        setNotationValues = {'member_id' : deviceLogin(self, loginPage["data"]["member_id"]),
                             'entry_id' : entry_id,
                             'start_char' : '1',
                             'end_char' : '2',
                             'comment_text' : 'comment, share all',
                             'highlighted_text' : 'highlight, share all',
                             'type' : '2',
                             'is_spointer' : 'false',
                             'in_reply_to' : '',
                             'page_number' : '',
                             'share_with_followers' : 'true',
                             'share_with_member_id' : '',
                             'auth_member_id' : deviceLogin(loginPage["data"]["member_id"]),
                             'auth_token' : deviceLogin(loginPage["data"]["auth_token"]),
                             'device_name' : swagger }
        
        setNotationData = urllib.urlencode(setNotationValues)
        setNotationReq = urllib2.Request(setNotationUrl, setNotationData)
        setNotationResponse = urllib2.urlopen(setNotationReq)
        setNotationPage = setNotationResponse.read()
        print(setNotationPage)
        
