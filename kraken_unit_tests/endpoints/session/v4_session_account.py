from service_base.service import Manager

sets = "############################ Account #################################"

class v4_account():
    
    def __init__(self,memberId, authToken, action, email, password, first_name, bday_d, bday_m, bday_y, device_name,last_name, gender):
        self.memberId          = memberId
        self.authToken         = authToken
        self.action            = action
        self.email             = email
        self.password          = password
        self.member_first_name = first_name
        self.member_last_name  = last_name
        self.bday_d            = bday_d
        self.bday_m            = bday_m
        self.bday_y            = bday_y
        self.device_name       = device_name
        self.member_gender     = gender
	
    def account(self, api_url):
        self.vals = { 'auth_member_id'    : self.memberId,
                      'auth_token'        : self.authToken,
                      'action'            : self.action,
				      'email'             : self.email,
				      'password'          : self.password,
				      'first_name'        : self.member_first_name,
				      'last_name'         : self.member_last_name,
				      'bday_d'            : self.bday_d,
				      'bday_m'            : self.bday_m,
				      'bday_y'            : self.bday_y,
				      'device_name'       : self.device_name,
				      'gender'            : self.member_gender
                    }
        manager = Manager(self.vals)
        manager.request(api_url, "session/account")

    def accountFail(self,api_url, message):
        self.vals = { 'auth_member_id'    : self.memberId,
                      'auth_token'        : self.authToken,
                      'action'            : self.action,
                      'email'             : self.email,
                      'password'          : self.password,
                      'first_name'        : self.member_first_name,
                      'last_name'         : self.member_last_name,
                      'bday_d'            : self.bday_d,
                      'bday_m'            : self.bday_m,
                      'bday_y'            : self.bday_y,
                      'device_name'       : self.device_name,
                      'gender'            : self.member_gender
                    }
        manager = Manager(self.vals)
        manager.requestFail(api_url, "session/account", message)

class accountTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url   = api_url
        self.memberId  = memberId
        self.authToken = authToken

    def account(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        ############### Invalid calls
        # create invalid account with invalid email. Catch failure
        createFail = v4_account(self.memberId, self.authToken, 'create', 'liamfailisntValid', 'failPass', 'Liam', '20', '10', '1992', 'dank', 'Test', 'm')
        createFail.accountFail(self.api_url, "Attempt create invalid email account")
        
        # create invalid account missing required information. Catch failure
        createFail1 = v4_account(self.memberId, self.authToken, 'create', 'liam@test2.com', 'failPass', 'Liam', None, None, None, None, 'Test', 'm')
        createFail1.accountFail(self.api_url, "Attempt create missing information")
        
        # attempt to create account with age too young
        createFail2 = v4_account(self.memberId, self.authToken, 'create', 'liam@test3.com', 'failPass', 'Liam','20', '10', '2005', 'dank', 'Test', 'm')
        createFail2.accountFail(self.api_url, "Attempt to create account for someone who is too young")

        # check for account that doesn't exist catch error
        existFail = v4_account(self.memberId, self.authToken, 'exists', 'MrFake@fake.com', None, None, None, None, None, None, None, None)
        existFail.accountFail(self.api_url, "Attempt to check for account that doesn't exist")
        
        
        ############# Valid calls
        # create valid account. expect success
        createAcc = v4_account(self.memberId, self.authToken, 'create', 'LiamAccountCreate@SessionAccount.com', 'testing123', 'Liam', '20', '10', '1992', 'The DeLorean', 'Test', 'm')
        createAcc.account(self.api_url)
        
        # check for valid account. expect success
        existsAcc = v4_account(self.memberId, self.authToken, 'exists', 'liam.mellor@zolabooks.com', None, None, None, None, None, None, None, None)
        existsAcc.account(self.api_url)






