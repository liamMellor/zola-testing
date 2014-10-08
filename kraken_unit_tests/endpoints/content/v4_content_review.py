from service_base.service import Manager

sets = "########################### REVIEW ###################################"

class v4review():

    def __init__(self,action,isbn, filter_id, filter_type, interval, period, fromVar, to, sort, sortType, limit, offset):
        self.vals = { 'action'      : action,
                      'isbn'        : isbn,
                      'filter_type' : filter_type,
                      'filter_id'   : filter_id,
                      'interval'    : interval,
                      'period'      : period,
                      'from'        : fromVar,
                      'to'          : to,
                      'sort'        : sort,
                      'sort-type'   : sortType,
                      'limit'       : limit,
                      'offset'      : offset
        			}
        
    def review(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "content/review")

class reviewTest():

    def __init__(self, api_url):
        self.api_url = api_url
        
    def review(self):
        print Manager.WARNING + sets + Manager.ENDC

        filters = ['all','rating','publication','reviewer','id']
        periods = ['days','months','years','all-time']

        for filterType in filters:
            for periodType in periods:
                if filterType == "id":
                    testReview = v4review('get', '9780307596901', '542f079989c8c1dd515b6eab', filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', 'date', '20', '0')
                    testReview.review(self.api_url)
                else:
                    testReview = v4review('get', '9780307596901', None , filterType, '1', periodType, '2013-01-01', '2014-01-01', 'desc', 'date', '20', '0')
                    testReview.review(self.api_url)
		
		#tests sort-type score
        testReview = v4review('get','9780307596901', None, 'all', '1', 'all-time', '2013-01-01', '2014-01-01', 'desc', 'score', '20','0')
        testReview.review(self.api_url)
        testReview = v4review('get','9780307596901', None, 'all', '1', 'all-time', '2013-01-01', '2014-01-01', 'desc', 'rating', '20','0')
        testReview.review(self.api_url)
