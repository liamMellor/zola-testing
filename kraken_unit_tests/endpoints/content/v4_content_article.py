from service_base.service import Manager

markers = "######################################################################\n########################### CONTENT ##################################\n######################################################################"
sets    = "########################### ARTICLE ##################################"

class v4article():

    def __init__(self, action, type, filter_id, filter_type, interval, period, fromVar, to, sort, limit, offset):
    	self.vals = { 'action'      : action,
        			  'type'        : type,
        			  'filter_id'   : filter_id,
        			  'filter_type' : filter_type,
        			  'interval'    : interval,
        			  'period'      : period,
        			  'from'        : fromVar,
        			  'to'          : to,
        			  'sort'        : sort,
        			  'limit'       : limit,
        			  'offset'      : offset
        			}

    def article(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "content/article")

class articleTest():
    
    def __init__(self, api_url):
        self.api_url = api_url

    def article(self):
        print Manager.OKBLUE + markers + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        filterTypes = ['all','author-related','book-related','related-articles','tag','slug']
        periods     = ['days','months','years','all-time']
        
        ########## Valid Calls
        # type all
        for filterType in filterTypes:
            for periodType in periods:
                if filterType == 'slug':
                    test = v4article('get', 'all', 'mindful-change-wisdom-from-thich-nhat-hanh', filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)
                else:
                    test = v4article('get', 'all', None, filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)


        # type text
        for filterType in filterTypes:
            for periodType in periods:
                if filterType == 'slug':
                    test = v4article('get', 'text', 'mindful-change-wisdom-from-thich-nhat-hanh', filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)
                else:
                    test = v4article('get', 'text', None, filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)

        # type list
        for filterType in filterTypes:
            for periodType in periods:
                if filterType == 'slug':
                    test = v4article('get', 'list', 'mindful-change-wisdom-from-thich-nhat-hanh', filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)
                else:
                    test = v4article('get', 'list', None, filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', '20', '0')
                    test.article(self.api_url)


