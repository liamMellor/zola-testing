from service_base.service import Manager

markers = "######################################################################\n############################ ECOMM ###################################\n######################################################################"

sets = "############################# SALEABLE ###############################"

class v4sale():

    def __init__(self, action, store, isbn, bundle_bool, id, contributor_id, display_formats, limit, offset):
        self.action          = action
        self.store           = store
        self.isbn            = isbn
        self.bundle_bool     = bundle_bool
        self.id              = id
        self.display_formats = display_formats
        self.contributor_id  = contributor_id
        self.limit           = limit
        self.offset          = offset

    def sale(self, api_url):
        self.vals = { 'action'          : self.action,
                      'store_uid'       : self.store,
                      'isbn'            : self.isbn,
                      'include_bundles' : self.bundle_bool,
                      'id'              : self.id,
                      'display_formats' : self.display_formats,
                      'contributor_id'  : self.contributor_id,
                      'limit'           : self.limit,
                      'offset'          : self.offset
                    }
        manager = Manager(self.vals)
        return manager.request(api_url, "ecomm/saleable")

class saleTest():

    def __init__(self, api_url):
        self.api_url = api_url

    def sale(self):
        print Manager.OKBLUE + markers + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC

        # test store
        storeSale = v4sale('store', 'ZOLA', None, 'true', None, None, None, 20, 0)
        storeSale.sale(self.api_url)
        storeSale = v4sale('store', 'ZOLA', None, 'false', None, None, None, 20, 0)
        storeSale.sale(self.api_url)

        # test affiliate
        afillSale = v4sale('affiliate', 'ZOLA', '9780525478812', 'true',  None, None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('affiliate', 'ZOLA', '9780525478812', 'false',  None, None, None, 20, 0)
        afillSale.sale(self.api_url)

        # test item
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'true',  None, None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false',  None, None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false',  '1508127', None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false',  '1508127', None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false',  '18e1c11f-1c44-4238-99a9-31944e7dc079', None, None, 20, 0)
        afillSale.sale(self.api_url)
        afillSale = v4sale('item', 'ZOLA', '9780525478812', 'false',  '18e1c11f-1c44-4238-99a9-31944e7dc079', None, None, 20, 0)
        afillSale.sale(self.api_url)
        
        

        # test list
        listSale = v4sale('list', 'ZOLA', '9780525478812', 'true', '1', None, 'ebook', 20, 0)
        listSale.sale(self.api_url)
        listSale = v4sale('list', 'ZOLA', '9780525478812', 'true', 'books-by-contributor', '87f6d5e5-09d3-46ed-957f-4f09be8fb3a2', 'ebook', 20, 0)
        listSale.sale(self.api_url)
        listSale = v4sale('list', 'ZOLA', '9780525478812', 'false', '1', None, 'ebook', 20, 0)
        listSale.sale(self.api_url)
        listSale = v4sale('list', 'ZOLA', '9780525478812', 'false', 'books-by-contributor', '87f6d5e5-09d3-46ed-957f-4f09be8fb3a2', 'ebook', 20, 0)
        listSale.sale(self.api_url)







