from service_base.service import Manager

sets = "########################### PURCHASE #################################"

class v4collectionPurchase():

    def __init__(self, auth_member_id, auth_token, action, order_id, interval, period, fromParam, to, sort, limit, offset):
        self.vals = { 'auth_member_id' : auth_member_id,
                      'auth_token'     : auth_token,
                      'action'         : action,
                      'order_id'       : order_id,
                      'interval'       : interval,
                      'period'         : period,
                      'from'           : fromParam,
                      'to'             : to,
                      'sort'           : sort,
                      'limit'          : limit,
                      'offset'         : offset
                    }

    def purchase(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "collection/purchase")

class purchaseTest():

    def __init__(self, api_url, member_id, auth_token):
        self.api_url        = api_url
        self.auth_member_id = member_id
        self.auth_token     = auth_token

    def purchase(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        periods = ['days','months','years','all-time']
        actions = ['history', 'preorder']
        
        for period in periods:
            for action in actions:
                testCase = v4collectionPurchase(self.auth_member_id, self.auth_token, action, None, '1', period , '2013-01-01', '2014-01-01', 'desc', 20, 0)
                testCase.purchase(self.api_url)