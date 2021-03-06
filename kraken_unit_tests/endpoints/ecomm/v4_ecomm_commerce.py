from service_base.service import Manager

sets = "############################ COMMERCE ################################"

class v4commerce():

    def __init__(self, auth_member_id, auth_token, action, store_uid=None, type=None, order_id=None, item_id=None, qty=None, isbn=None, code=None, amount=None, session_id=None, carrier=None, email=None, opt_in=None):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.store_uid      = store_uid
        self.type           = type
        self.order_id       = order_id
        self.item_id        = item_id
        self.qty            = qty
        self.isbn           = isbn
        self.code           = code
        self.amount         = amount
        self.session_id     = session_id
        self.carrier        = carrier
        self.email          = email
        self.opt_in         = opt_in
        
    
    def commerce(self,api_url):
        self.vals = { 'auth_member_id' : self.auth_member_id,
                      'auth_token'     : self.auth_token,
                      'action'         : self.action,
                      'store_uid'      : self.store_uid,
                      'order_id'       : self.order_id,
                      'item_id'        : self.item_id,
                      'qty'            : self.qty,
                      'isbn'           : self.isbn,
                      'code'           : self.code,
                      'amount'         : self.amount,
                      'session_id'     : self.session_id,
                      'carrier'        : self.carrier,
                      'email'          : self.email,
                      'opt_in'         : self.opt_in
                    }
        if self.type != None:
            self.vals['type'] = self.type
        
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/commerce")

class commerceTest():

    def __init__(self, api_url, auth_member_id, auth_token):
        self.api_url        = api_url
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token

    def commerce(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        cartTypes = ['add','count','remove','update','view']
        promTypes = ['apply-to-order','remove-from-order','validate']
        certTypes = ['apply-to-order','remove-from-order','validate','balance','add-to-account']
        credTypes = ['apply-to-order','remove-from-order','balance']
        calcTypes = ['ECONOMY','EXPEDITED']
        
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "cart", "ZOLA", 'add', orderID, 1508127, '1', '9780525478812', None, sessionID, None, None, None)
        commerceA.commerce(self.api_url)
        
        # action = cart
        for type in cartTypes:
            if type == 'add' or type == 'remove' or type == 'update':
                commerceA = v4commerce(self.auth_member_id, self.auth_token, "cart", "ZOLA", type, orderID, 1508127, None, None, None, sessionID, None, None, None)
                commerceA.commerce(self.api_url)
            else:
                commerceA = v4commerce(self.auth_member_id, self.auth_token, "cart", "ZOLA", type, orderID, 1508127, None, None, None, sessionID, None, None, None)
                commerceA.commerce(self.api_url)
        
        # action = promotional_code
        for type in promTypes:
            commerceA = v4commerce(self.auth_member_id, self.auth_token, "promotional_code", "ZOLA", type, orderID, 1508127, None, None, "FREE-SHIPPING", sessionID, None, None, None)
            commerceA.commerce(self.api_url)
        
        # action = certificate
        for type in certTypes:
            commerceA = v4commerce(self.auth_member_id, self.auth_token, "certificate", "ZOLA", type, orderID, 1508127, None, None, "FREE-SHIPPING", sessionID, None, None, None)
            commerceA.commerce(self.api_url)
        
        # action = credit
        for type in credTypes:
            commerceA = v4commerce(self.auth_member_id, self.auth_token, "credit", "ZOLA", type, orderID, 1508127, None, None, 0.00, sessionID, None, None, None)
            commerceA.commerce(self.api_url)
        
        # action = process
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "process", "ZOLA", None, orderID, 1508127, None, None, None, None, sessionID, None, "michael.jordan@zolabooks.com", 1)
        commerceA.commerce(self.api_url)
        	 
        # action = detail
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "detail", "ZOLA", None, orderID, None, None, None, None, sessionID, None, None, None)
        commerceA.commerce(self.api_url)
        
        # action = calculate_shipping 
        for type in calcTypes:
            commerceA = v4commerce(self.auth_member_id, self.auth_token, "calculate_shipping", "ZOLA", None, orderID, None, None, None, None, sessionID, 'USPS', None, None)
            commerceA.commerce(self.api_url)
                
        # action = email_receipt
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "email_receipt", "ZOLA", None, orderID, None, None, None, None, None, sessionID, None, "michael.jordan@zolabooks.com", None)
        commerceA.commerce(self.api_url)
    
        # action = opt_in
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "opt_in", "ZOLA", None, orderID, None, None, None, None, sessionID, None, None, 0)
        commerceA.commerce(self.api_url)
    
        # action = send_to_kindle
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "send_to_kindle", "ZOLA", None, orderID, 1508127, None, '9780525478812', None, None, sessionID, None, "liam.mellor@zolabooks.com", 0)
        commerceA.commerce(self.api_url)


    def commerceInit(self):
        global orderID
        global sessionID
        print Manager.WARNING + sets + Manager.ENDC
        # initialize cart
        commerceA = v4commerce(self.auth_member_id, self.auth_token, "initialize", "ZOLA", None, None, None, None, None, None, None, None, None, None)
        info      = commerceA.commerce(self.api_url)
        orderID   = info[1]["data"]['order_id']
        sessionID = info[1]["data"]['session_id']
