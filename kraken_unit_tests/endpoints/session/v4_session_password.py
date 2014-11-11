from service_base.service import Manager

sets = "########################### Password #################################"


class v4password():
    
    def __init__(self, member_id, auth_token, action, username, current_password, new_password, email):
        self.member_id        = member_id
        self.auth_token       = auth_token
        self.action           = action
        self.username         = username
        self.current_password = current_password
        self.new_password     = new_password
        self.email            = email

    def password(self, api_url):
        self.vals = { "auth_member_id"   : self.member_id,
                      "auth_token"       : self.auth_token,
                      "action"           : self.action,
                      "current_password" : self.current_password,
                      "password"         : self.new_password,
                      "email"            : self.email
                    }
        if self.username != None:
            self.vals["username"] = self.username
        
        manager = Manager(self.vals)
        manager.request(api_url, "session/password")

    def passwordNoEmail(self, api_url):
        self.vals = { "auth_member_id"   : self.member_id,
                      "auth_token"       : self.auth_token,
                      "action"           : self.action,
                      "username"         : self.username,
                      "current_password" : self.current_password,
                      "password"         : self.new_password

                    }
        manager = Manager(self.vals)
        manager.request(api_url, "session/password")

    def passwordFail(self, api_url, message):
        self.vals = { "auth_member_id"   : self.member_id,
                      "auth_token"       : self.auth_token,
                      "action"           : self.action,
                      "username"         : self.username,
                      "current_password" : self.current_password,
                      "password"         : self.new_password,
                      "email"            : self.email
                    }
        manager = Manager(self.vals)
        manager.requestFail(api_url, "session/password", message)

class passwordTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url     = api_url
        self.member_id   = member_id
        self.auth_token  = auth_token

    def password(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        ########## Invalid Calls
        # attempt to update password for non-existing account
        #updateFail = v4password(self.member_id, self.auth_token, 'update', 'Fake-acc-1', 'pass', 'new_pass', 'fake@fake.com')
        #updateFail.passwordFail(self.api_url, "Attempt to update password for non-account")
        
        # attempt to update password for existing account incorrect password
        #updateFail1 = v4password(self.member_id, self.auth_token, 'update', 'Liam-Test1', 'wrong_pass', 'testing123', 'liam@test1.com')
        #updateFail1.passwordFail(self.api_url, "Attempt to update password with incorrect current password")
        
        # attempt to update password to blank string
        #updateFail2 = v4password(self.member_id, self.auth_token, 'update', 'Liam-Test1', 'testing123', '', 'liam@test1.com')
        #updateFail2.passwordFail(self.api_url, "Attempt to update password to empty string")
        
        
        ########## Valid Calls
        '''
        # update password by providing user name
        update1 = v4password(self.member_id, self.auth_token, 'update', 'Liam-Test1', 'testing123', 'testing123', None)
        update1.passwordNoEmail(self.api_url)
        '''
        
        # update password by providing email addres             username was None
        update = v4password(self.member_id, self.auth_token, 'update', 'michael-jordan', '123456123456', '123456123456', 'michael.jordan@zolabooks.com')
        update.password(self.api_url)
        
        # email user password at specified email
        forgot = v4password(self.member_id, self.auth_token, 'forgot', 'mail-rollem', None , None, 'liam.mellor@zolabooks.com')
        forgot.password(self.api_url)






