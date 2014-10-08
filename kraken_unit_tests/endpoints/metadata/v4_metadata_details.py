from service_base.service import Manager

marker = "######################################################################\n########################### METADATA #################################\n######################################################################"

sets = "############################ Details #################################"

class v4Details():
    
    def __init__(self, action, authorId, isbn, format, limit, offset):
        self.vals = { "isbn"             : isbn,
                      "action"           : action,
                      "preferred-format" : format,
                      "limit"            : limit,
                      "offset"           : offset,
                      "contributor_id"   : authorId
                    }

    def details(self, api_url):
        manager = Manager(self.vals)
        manager.request(api_url, "metadata/details")

    def detailsFail(self, api_url, message):
        manager = Manager(self.vals)
        manager.requestFail(api_url, "metadata/details", message)

class DetailsTest():
    
    def __init__(self, api_url, member_id, auth_token):
        self.api_url    = api_url
        self.member_id  = member_id
        self.auth_token = auth_token

    def details(self):
        print Manager.OKBLUE + marker + Manager.ENDC
        print Manager.WARNING + sets + Manager.ENDC
        
        ######## Valid Calls
        book = v4Details("book", None, "9780525478812", None, None, None)
        book.details(self.api_url)

        bookMin = v4Details("book-min", None, "9780525478812", None, None, None)
        bookMin.details(self.api_url)

        author = v4Details("contributor", '87f6d5e5-09d3-46ed-957f-4f09be8fb3a2', None, None, None, None)
        author.details(self.api_url)
        
        authorBook = v4Details("books-by-contributor", '87f6d5e5-09d3-46ed-957f-4f09be8fb3a2', None, None, None, None)
        authorBook.details(self.api_url) 



