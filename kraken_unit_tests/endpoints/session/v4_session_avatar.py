from service_base.service import Manager

sets = "############################# Avatar #################################"

class v4avatar():

    def __init__(self, auth_member_id, auth_token, action, url):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.url            = url

    def avatar(self, api_url):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'url'            : self.url
                    }
        manager = Manager(self.vals)
        manager.request(api_url, "session/avatar")

    def avatarFail(self, api_url, message):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'url'            : self.url
                    }
        manager = Manager(self.vals)
        manager.requestFail(api_url, "session/avatar", message)

class avatarTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url   = api_url
        self.memberId  = memberId
        self.authToken = authToken
    
    def avatar(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        ######### Invalid Calls
        
        
        ######### Valid Calls
        avatarUrl = v4avatar(self.memberId, self.authToken, "set-url", "http://solutions.3m.com/innovation/assets/technologies/thumbnails/lm.jpg")
        avatarUrl.avatar(self.api_url)
        
        avatarRem = v4avatar(self.memberId, self.authToken, "remove", None)
        avatarRem.avatar(self.api_url)