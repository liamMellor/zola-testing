import urllib
import urllib2
import datetime
import json

class v4_rec():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    TIMEPURP = '\033[35m'
    TIMEBLOCK = "### TIME ###\n"

    def __init__(self, value_dict):
        self.value_dict = value_dict

    def request(self, api_url, endpoint):
        url = api_url + endpoint
        data = urllib.urlencode(self.value_dict)
        print url + "?" + data
        req = urllib2.Request(url +"?"+ data)
        response = None
        code = None
        clock1 = datetime.datetime.now()
        clock2 = datetime.datetime.now()
        try:
            clock1 = datetime.datetime.now()
            response = urllib2.urlopen(req)
            clock2 = datetime.datetime.now()
            s = [response.getcode(), json.load(response)]
            if s[1]["status"] == "system_error":
                return v4_rec.FAIL + self.dump(s) + v4_rec.ENDC
            return v4_rec.OKGREEN + self.dump(s) + v4_rec.ENDC
        except urllib2.HTTPError as e:
            s = [e, e.read()]
            return v4_rec.FAIL + self.dump(s) + v4_rec.ENDC
        finally:
            timeattack = clock2 - clock1
            print v4_rec.TIMEPURP + v4_rec.TIMEBLOCK + str(timeattack) + v4_rec.ENDC
    def dump(self, s):
        if len(s) > 1:
            return json.dumps(s[1], indent=4, sort_keys=False)
        else:
            return s

ar = v4_rec({'action':'get',"isbn":"9780446580502","count":"25"})
print ar.request("http://zolaqc.com/api/v4/", "recommendation/rec")
