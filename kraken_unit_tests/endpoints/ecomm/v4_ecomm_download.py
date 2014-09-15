from service_base.service import Manager

sets = "############################ DOWNLOAD ################################"

class v4download():

    def __init__(self, auth_member_id, auth_token, action, isbn, type, web):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.isbn           = isbn
        self.type           = type
        self.web            = web

    def download(self, api_url):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'isbn'           : self.isbn,
                      'type'           : self.type,
                      'web'            : self.web
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/download")

class downloadTest():

    def __init__(self, api_url, auth_member_id, auth_token):
        self.api_url        = api_url
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token

    def download(self):
        print Manager.WARNING + sets + Manager.ENDC
		
        actions = ['get-key','get-file-info','download','download-no-header','download-base64']
        bools   = ['true','false']
        for action in actions:
            for bool in bools:
                downloadA = v4download(self.auth_member_id, self.auth_token, action, '9781451667943', 'epub', bool)
                downloadA.download(self.api_url)

