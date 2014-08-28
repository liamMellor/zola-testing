from service_base.service import Manager

sets = "############################ CNT ###############################"

class v4cnt():
    
    def __init__(self, member_id, auth_token, action, isbn):
        self.member_id  = member_id
        self.auth_token = auth_token
        self.action     = action
        self.isbn       = isbn

    def count(self, api_url):
        self.vals = { 'auth_member_id' : self.member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'isbn'           : self.isbn
                    }
        manager = Manager(self.vals)
        manager.request(api_url, "social/cnt")

class cntTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url   = api_url
        self.memberId  = memberId
        self.authToken = authToken

    def count(self):
        print Manager.WARNING + sets + Manager.ENDC
        testCount = v4cnt(self.memberId, self.authToken, "get", "7560634534324")
        testCount.count(self.api_url)

