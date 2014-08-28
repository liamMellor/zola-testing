from service_base.service import Manager

reading = "########################## MEMBER/READING #############################"
stream = "########################## MEMBER/STREAM ##############################"

class Member():

    def __init__(self, auth_member_id, auth_token, action, isbn = None, member_id = None, limit = None, offset= None):
        self.vals = { "auth_member_id": auth_member_id,
                      "auth_token" : auth_token,
                      "action" : action }
        if limit is not None:
            self.vals["limit"] = limit
        if offset is not None:
            self.vals["offset"] = offset

        if action == "reading-book":
            self.vals["isbn"] = isbn

        if action == "activity-stream":
            self.vals["member_id"] = member_id

    def member(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "social/member")


class MemberTest():
    def __init__(self, api_url, member_id, auth_token):
        self.api_url = api_url
        self.auth_member_id = member_id
        self.member_id = member_id
        self.auth_token = auth_token

    def memberTest(self):
    
        a = Member(self.auth_member_id, self.auth_token, "reading-book", isbn = "9781939126009", member_id = self.member_id)
        print Manager.WARNING + reading + Manager.ENDC
        
        a.member(self.api_url)
        b = Member(self.auth_member_id, self.auth_token, "activity-stream", member_id = self.member_id, limit=50)
        
        print Manager.WARNING + stream + Manager.ENDC
        b.member(self.api_url)
        
