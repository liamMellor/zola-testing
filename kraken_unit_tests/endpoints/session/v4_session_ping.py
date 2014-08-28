from service_base.service import Manager

sets = "############################# Ping ###################################"

class v4ping():

    def __init__(self, memberId, authToken):
        self.vals = { 'auth_member_id' : memberId,
                      'auth_token'     : authToken
                    }

    def ping(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "session/ping")

class pingTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url   = api_url
        self.memberId  = memberId
        self.authToken = authToken

    def ping(self):
        print Manager.WARNING + sets + Manager.ENDC
        a = v4ping(self.memberId, self.authToken)
        a.ping(self.api_url)