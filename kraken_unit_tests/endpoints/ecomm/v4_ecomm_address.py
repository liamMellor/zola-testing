from service_base.service import Manager

sets = "############################# ADDRESS ################################"

class v4address():

    def __init__(self, auth_member_id, auth_token, action=None, type=None, id=None, country_iso=None, order_id=None, name=None, address1=None, address2=None, city=None, state=None, zip=None, country_alpha2=None, label=None, card_name=None, card_type=None, card_exp_month=None, card_exp_year=None, card_cvv=None, card_number=None):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.type           = type
        self.id             = id
        self.country_iso    = country_iso
        self.order_id       = order_id
        self.name           = name
        self.address1       = address1
        self.address2       = address2
        self.city           = city
        self.state          = state
        self.zip            = zip
        self.country_alpha2 = country_alpha2
        self.label          = label
        self.card_name      = card_name
        self.card_type      = card_type
        self.card_exp_month = card_exp_month
        self.card_exp_year  = card_exp_year
        self.card_cvv       = card_cvv
        self.card_number    = card_number
        
    def address(self, api_url):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'type'           : self.type,
                      'id'             : self.id,
                      'country_numeric_iso_3166_1' : self.country_iso,
                      'order_id'       : self.order_id,
                      'name'           : self.name,
                      'address1'       : self.address1,
                      'address2'       : self.address2,
                      'city'           : self.city,
                      'state'          : self.state,
                      'zip'            : self.zip,
                      'country_alpha2' : self.country_alpha2,
                      'label'          : self.label,
                      'card_name'      : self.card_name,
                      'card_type'      : self.card_type,
                      'card_exp_month' : self.card_exp_month,
                      'card_exp_year'  : self.card_exp_year,
                      'card_cvv'       : self.card_cvv,
                      'card_number'    : self.card_number
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/address")

class addressTest():

    def __init__(self, api_url, auth_member_id, auth_token):
        self.api_url        = api_url          # set from harness
        self.auth_member_id = auth_member_id   # set from harness
        self.auth_token     = auth_token       # set from harness

    def address(self):
		
        print Manager.WARNING + sets + Manager.ENDC

        listTypes  = ['shipping','zip','state','country']
        otherTypes = ['set-default','view','update']

		#######################################   Action == LIST   #######################################
        for type in listTypes:
            if type == 'zip':
                testAddress = v4address(self.auth_member_id, self.auth_token, 'list', type, 11206, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", None, None, None, None)
                testAddress.address(self.api_url)
            else:
                testAddress = v4address(self.auth_member_id, self.auth_token, 'list', type, None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", None, None, None, None)
                testAddress.address(self.api_url)
		
        #######################################   Action == SHIPPING   #######################################
        # shipping action = add
        testAddress = v4address(self.auth_member_id, self.auth_token, 'shipping', 'add', None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        value      = testAddress.address(self.api_url)
        objects    = value[1]['data']
        mostRecent = objects[-1]
        id         = mostRecent['id']
        
        '''
        new      = 0
        for number in objects:
            if number == "default":
                continue                                    # This loop finds most recent addition to address to be removed below
            print number
            number = int(number)
            if number > new:
                new = number
        id = objects[str(new)]['id']
        '''
        
        # shipping action = delete
        testAddress = v4address(self.auth_member_id, self.auth_token, 'shipping', 'delete', id, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        testAddress.address(self.api_url)
        
        # shipping action = add for remainding calls
        testAddress = v4address(self.auth_member_id, self.auth_token, 'shipping', 'add', None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None,None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        value      = testAddress.address(self.api_url)
        objects    = value[1]['data']
        mostRecent = objects[-1]
        id         = mostRecent['id']
        
        '''
        new      = 0
        for number in objects:
            if number == "default":
                continue                                    # This loop finds most recent addition to address to be used for further calls below
            number = int(number)
            if number > new:
                new = number
        id = objects[str(new)]['id']
        '''
        
		# shipping action = set-default + view + update
        for type in otherTypes:
            if type == 'update' or type == 'set-default':
                testAddress = v4address(self.auth_member_id, self.auth_token, 'shipping', type, id, '840', 2, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
                testAddress.address(self.api_url)
            else:
                testAddress = v4address(self.auth_member_id, self.auth_token, 'shipping', type, None, '840', 2, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
                testAddress.address(self.api_url)



        #######################################   Action == BILLING   #######################################
        # billing action = add
        testAddress = v4address(self.auth_member_id, self.auth_token, 'billing', 'add', None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        value      = testAddress.address(self.api_url)
        objects    = value[1]['data']
        mostRecent = objects[-1]
        id         = mostRecent['id']
        
        '''
        new = 0
        for number in objects:
            if number == "default":
                continue                                    # This loop finds most recent addition to billing to be delted below
            number = int(number)
            if number > new:
                new = number
        id = objects[str(new)]['id']
        '''
        
        # billing action = delete
        testAddress = v4address(self.auth_member_id, self.auth_token, 'billing', 'delete', id, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        testAddress.address(self.api_url)

        # billing action = add
        testAddress = v4address(self.auth_member_id, self.auth_token, 'billing', 'add', None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None,None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
        value      = testAddress.address(self.api_url)
        objects    = value[1]['data']
        mostRecent = objects[-1]
        id         = mostRecent['id']
        
        '''
        new = 0
        for number in objects:
            if number == "default":
                continue                                    # This loop finds most recent addition to billing to be used for further calls below
            number = int(number)
            if number > new:
                new = number
        id = objects[str(new)]['id']
        '''

		# billing action = set-default + view + update
        for type in otherTypes:
            if type == 'update' or type == 'set-default':
                testAddress = v4address(self.auth_member_id, self.auth_token, 'billing', type, id, '840', 2, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
                testAddress.address(self.api_url)
            else:
                testAddress = v4address(self.auth_member_id, self.auth_token, 'billing', type, None, '840', 2, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", 06, 2017, 333, 5555555555554444)
                testAddress.address(self.api_url)
		
        
        #######################################   Action == RETURN CHECK   #######################################
		# action = return-check
        testAddress = v4address(self.auth_member_id, self.auth_token, 'return-check', type, None, '840', None, "Liam Mellor", "36 Meserole St", None, "Brooklyn", "NY", "11206", None, None, "Liam Mellor", "Visa", None, None, None, None)
        testAddress.address(self.api_url)
        
