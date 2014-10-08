# First full test module written by Liam
from service_base.service import Manager

sets = "########################### CURATION #################################"

class v4curation():

    def __init__(self, action, isbn, member_id):
        self.action    = action
        self.isbn      = isbn
        self.member_id = member_id

    def curation(self, api_url):
        self.vals = { 'action' : self.action
                    }
        if self.isbn != None:
            self.vals['isbn'] = self.isbn
        if self.member_id != None:
            self.vals['member_id'] = self.member_id

        manager = Manager(self.vals)
        return manager.request(api_url, "collection/curation")

class curationTest():

    def __init__(self, api_url):
        self.api_url = api_url
    
    def curation(self):

		print Manager.WARNING + sets + Manager.ENDC

		# Test curation for isbn
		curator = v4curation( 'get', '9781939126009', None)
		curator.curation(self.api_url)

		#test curation for author_id
		curator = v4curation( 'get', None, '64361')
		curator.curation(self.api_url)