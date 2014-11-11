from service_base.service import Manager

markers = "#######################################################################\n############################# SEARCH ##################################\n#######################################################################"

sets = "############################## FIND ###################################"

class v4find():

    def __init__(self, action, query, limit, offset):
        self.action = action
        self.query  = query
        self.limit  = limit
        self.offset = offset

    def find(self, api_url):
        self.vals = { 'action' : self.action,
                      'query'  : self.query,
                      'limit'  : self.limit,
                      'offset' : self.offset
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "search/find")

class findTest():

    def __init__(self, api_url):
        self.api_url = api_url
    
    def find(self):
        print Manager.OKBLUE + markers + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        testFind1 = v4find("title", "Wizard of Oz", 20, 0)
        testFind1.find(self.api_url)
        testFind2 = v4find("contributor", "John", 20, 0)
        testFind2.find(self.api_url)
        testFind3 = v4find("keyword", "magic", 20, 0)
        testFind3.find(self.api_url)
        testFind4 = v4find(None, "magic", 20, 0)
        testFind2.find(self.api_url)
        