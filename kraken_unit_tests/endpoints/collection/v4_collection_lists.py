from service_base.service import Manager

marker = "######################################################################\n######################### COLLECTIONS ################################\n######################################################################"

sets = "############################ LISTS ###################################"

class v4coll():
	
	def __init__(self, auth_member_id, auth_token, action, isbn, type):
		self.vals = { 'auth_member_id' : auth_member_id, 
                      'auth_token'     : auth_token,
                      'action'         : action,
  				      'isbn'           : isbn,
                      'type'           : type,
                     }
		
	def list(self, api_url):
		manager = Manager(self.vals)
		return manager.request(api_url, "collection/lists")
		
class CollectionTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url        = api_url
        self.auth_member_id = member_id
        self.auth_token     = auth_token

    def list(self):
        print Manager.OKBLUE + marker + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        types   = ['purchased','reading','wishlist']

        listTest = v4coll(self.auth_member_id, self.auth_token, None, None, None)
        listTest.list(self.api_url)

        # take care of gets
        for type in types:
            listTest = v4coll(self.auth_member_id, self.auth_token, 'get', None, type)
            listTest.list(self.api_url)
         
         # now do sets and removes for wishlist only
        listTest = v4coll(self.auth_member_id, self.auth_token, 'set', '1010375482936', 'wishlist')
        listTest.list(self.api_url)
        listTest = v4coll(self.auth_member_id, self.auth_token, 'remove', '1010375482936', 'wishlist')
        listTest.list(self.api_url)
        
        # test case where action is get and type '' returns all three
        listTest = v4coll(self.auth_member_id, self.auth_token, 'get', None, '')
        listTest.list(self.api_url)


