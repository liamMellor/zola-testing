# First full test module written by Liam
from service_base.service import Manager

sets = "########################### CURATION #################################"

class v4curation():

    def __init__(self, auth_member_id, auth_token, action, isbn, author_id):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.isbn           = isbn
        self.author_id      = author_id

    def curation(self, api_url):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'isbn'           : self.isbn,
					  'contributor_id'      : self.author_id
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "collection/curation")

class curationTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url        = api_url
        self.auth_member_id = member_id
        self.auth_token     = auth_token
    
    def curation(self):

		print Manager.WARNING + sets + Manager.ENDC

		# Test curation for isbn
		curator = v4curation(self.auth_member_id, self.auth_token, 'get', '9781939126009', None)
		curator.curation(self.api_url)

		#test curation for author_id
		curator = v4curation(self.auth_member_id, self.auth_token, 'get', None, '64361')
		curator.curation(self.api_url)