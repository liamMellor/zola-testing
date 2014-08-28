from service_base.service import Manager


markers = "#######################################################################\n#################### SESSION (Revisited) ##############################\n#######################################################################"
sets = "############################# Token ###################################"


class v4token():
    
    def __init__(self, member_id, auth_token, action):
        self.member_id = member_id
        self.auth_token = auth_token
        self.action = action

    def token(self, api_url):
        self.vals = { 'auth_member_id' : self.member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "session/token")

class tokenTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url    = api_url
        self.member_id  = member_id
        self.auth_token = auth_token

    def regenerate(self):
        print Manager.OKBLUE + markers + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        regenerate = v4token(self.member_id, self.auth_token, 'regenerate')
        return regenerate.token(self.api_url)

    def deactivate(self):
        deactivate = v4token(self.member_id, self.auth_token, 'deactivate')
        deactivate.token(self.api_url)