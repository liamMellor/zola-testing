from v4_session_login import V4_login
from v4_session_account import V4_account
from v4_session_logout import V4_logout
from v4_session_token import V4_token
from v4_session_password import V4_password

api_url = 'https://api.zolaqc.com/v4/'

class v4_harness():
    
    def __init__(self):
        global api_url
    
    def runner(self):
        thisPassword = "bookish"
        accountInst = V4_account("create", "jackson.gilkey@gmail.com", thisPassword, "Jackson", "Gilkey", "8", "10", "1990", "swagger", "m")
        accountDict = accountInst.account(api_url)
        try: 
            accountDict["member_id"] = int(accountDict["member_id"])
        except ValueError:
            pass
        if accountDict["auth_token"].isalnum() is False:
            assert False, "auth_token is non alpha numeric"
        if accountDict["device_name"].isalpha() is False:
            assert False, "device_name is non alphabetical"
        loginInst = V4_login("jackson-gilkey",thisPassword,"swagger","jackson.gilkey@gmail.com")
        loginDict =  loginInst.login(api_url)
        print loginDict
        memberId = loginDict["member_id"]
        authToken = loginDict["auth_token"]
        deviceName = loginDict["device_name"]
        try:
            memberId = int(memberId)
        except ValueError:
            pass
        if authToken.isalnum() is False:
            assert False, "auth_token is non alpha numeric"
        if deviceName.isalpha() is False:
            assert False, "device_name is non alphabetical"

        passwordInst = V4_password(memberId,authToken,"update","jackson-gilkey",thisPassword,thisPassword,"jackson.gilkey@gmail.com")
        passwordInst.password(api_url)
        tokenInst = V4_token(memberId, authToken, "deactivate")
        tokenInst.token(api_url)
        loginInst = V4_login("jackson-gilkey",thisPassword,"swagger","jackson.gilkey@gmail.com")
        loginDict =  loginInst.login(api_url)
        memberId = loginDict["member_id"]
        authToken = loginDict["auth_token"]
        deviceName = loginDict["device_name"]
        logoutInst = V4_logout(memberId, authToken, "true")
        print logoutInst.logout(api_url)

harness = v4_harness()
harness.runner()
