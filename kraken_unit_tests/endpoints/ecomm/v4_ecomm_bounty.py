from service_base.service import Manager

sets = "############################# BOUNTY #################################"

class v4bounty():

    def __init__(self, member_id, auth_token, action, isbn):
        self.member_id  = member_id
        self.auth_token = auth_token
        self.action     = action
        self.isbn       = isbn

    def bounty(self, api_url):
        self.vals = { 'auth_member_id' : self.member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'isbn'           : self.isbn
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/bounty")

    def bountyFail(self, api_url, message):
        self.vals = { 'auth_member_id' : self.member_id,
            'auth_token'     : self.auth_token,
            'action'         : self.action,
            'isbn'           : self.isbn
            }
        manager = Manager(self.vals)
        return manager.requestFail(api_url, "ecomm/bounty", message)



class bountyTest():

    def __init__(self, api_url, member_id, auth_token):
    
        self.api_url    = api_url
        self.member_id  = member_id
        self.auth_token = auth_token

    def bounty(self):
    	
    	print Manager.WARNING + sets + Manager.ENDC
        
        testBounty = v4bounty(self.member_id, self.auth_token, 'list', None)
        testBounty.bounty(self.api_url)
        
        testBounty = v4bounty(self.member_id, self.auth_token, 'get', '1010375482936')
        testBounty.bountyFail(self.api_url, '')



