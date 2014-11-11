from service_base.service import Manager

markers = "#######################################################################\n######################## RECOMMENDATION ###############################\n#######################################################################"

sets = "############################### REC ###################################"

class v4rec():

    def __init__(self, action, isbn, limit, offset, override, format, restrict):
        self.action   = action
        self.isbn     = isbn
        self.limit    = limit
        self.offset   = offset
        self.override = override
        self.format   = format
        self.restrict = restrict


    def rec(self,api_url):
        self.vals = { 'action'          : self.action,
                      'isbn'            : self.isbn,
                      'limit'           : self.limit,
                      'offset'          : self.offset,
                      'origin-override' : self.override,
                      'preferred-format': self.format,
                      'restrict-format' : self.restrict
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "recommendation/rec")

class recTest():

    def __init__(self, api_url):
        self.api_url = api_url

    def rec(self):
        print Manager.OKBLUE + markers + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        
        actions = ['get','get-meta','get-meta-min']
        origins = ['essential','semtag']
        prefers = ['ebook','hardcover','paperback','print','digitalaudio','jigsaw']
        
        for action in actions:
            for origin in origins:
                for format in prefers:
                    testRec = v4rec(action, 9780525478812, 20, 0, origin, format, "false")
                    testRec.rec(self.api_url)
