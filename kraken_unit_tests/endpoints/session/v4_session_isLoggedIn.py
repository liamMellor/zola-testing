from service_base.service import Manager

sets = "######################## Is-Logged-In ################################"

class v4isLogged():

    def __init__(self, memberId, authToken):
        self.vals = { "auth_member_id" : memberId,
                      "auth_token"     : authToken
                    }

    def isLogged(self, api_url):
        manager = Manager(self.vals)
        manager.request(api_url, "session/is_logged_in")

class isLoggedTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url    = api_url
        self.memberId   = memberId
        self.authToken  = authToken

    def checkLog(self):
        print Manager.WARNING + sets + Manager.ENDC
        a = v4isLogged(self.memberId, self.authToken)
        return a.isLogged(self.api_url)