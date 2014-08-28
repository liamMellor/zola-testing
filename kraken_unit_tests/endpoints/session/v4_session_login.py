from service_base.service import Manager

marker = "######################################################################\n########################### SESSION ##################################\n######################################################################"
sets = "############################# Login ##################################"

class v4_login():
    
    def __init__(self, username, password, device, email, persist):
        self.vals = { "username"   : username,
                      "password"   : password,
                      "device_name": device,
                      "email"      : email,
                      "persist"    : persist
                    }

    def login(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "session/login")

    def loginFail(self, api_url, message):
        manager = Manager(self.vals)
        manager.requestFail(api_url, "session/login", message)

class LoginTest():
    
    def __init__(self, api_url):
        self.api_url = api_url
        
    def activate(self):
        
        print Manager.OKBLUE + marker + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        
        # wrong password catch error
        failLog = v4_login("jason-flax-2", "wrongPassword","awesomefuckingbot",None,'true')
        failLog.loginFail(self.api_url, "Attempt invalid password")
        
        # wrong password and username catch error
        doubleFailLog = v4_login("jason-doobie-2", "wrongPassword2", "awesomefuckingbot",None,'true')
        doubleFailLog.loginFail(self.api_url, "Attempt invalid password and username")
        
        # correct login to be logged out
        a = v4_login("mail-rollem", "testing123", "The DeLorean", "liam.mellor@zolabooks.com", 'true')
        return a.login(self.api_url)

    def activate1(self):
        
        # second correct login to run remaining tests
        b = v4_login("mail-rollem", "testing123", "The DeLorean", "liam.mellor@zolabooks.com", 'false')
        return b.login(self.api_url)