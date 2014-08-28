from service_base.service import Manager

markers = "######################################################################\n############################ ECOMM ###################################\n######################################################################"

sets = "############################# SALEABLE ###############################"

class v4sale():

    def __init__(self, action, store, isbn, bundle_bool):
        self.action      = action
        self.store       = store
        self.isbn        = isbn
        self.bundle_bool = bundle_bool

    def sale(self, api_url):
        self.vals = { 'action'          : self.action,
                      'store_uid'       : self.store,
                      'isbn'            : self.isbn,
                      'include_bundles' : self.bundle_bool
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/saleable")

class saleTest():

    def __init__(self, api_url):
        self.api_url     = api_url

    def sale(self):
		print Manager.OKBLUE + markers + Manager.ENDC
		print Manager.WARNING + sets + Manager.ENDC

		# test store
		storeSale = v4sale('store', 'ZOLA', None, 'true')
		storeSale.sale(self.api_url)
		storeSale = v4sale('store', 'ZOLA', None, 'false')
		storeSale.sale(self.api_url)

		# test affiliate
		afillSale = v4sale('affiliate', 'ZOLA', '9780525478812', 'true')
		afillSale.sale(self.api_url)
		afillSale = v4sale('affiliate', 'ZOLA', '9780525478812', 'false')
		afillSale.sale(self.api_url)

		# test item
		afillSale = v4sale('item', 'ZOLA', '9780525478812', 'true')
		afillSale.sale(self.api_url)
		afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false')
		afillSale.sale(self.api_url)

