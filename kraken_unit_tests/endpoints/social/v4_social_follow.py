from service_base.service import Manager

sets = "########################## FOLLOW ##############################"

class Follow():
    def __init__(self, auth_member_id, auth_token, action, member_id = None):
        self.auth_member_id = auth_member_id
        self.auth_token     = auth_token
        self.action         = action
        self.member_id      = member_id
        self.vals = { "auth_member_id": auth_member_id,
                      "auth_token": auth_token,
                      "action": action 
                    }
        if action == "start-following" or "unfollow":
            self.vals["member_id"] = member_id
        
    def follow(self, api_url):
        manager = Manager(self.vals)
        return manager.request(api_url, "social/follow")
        
    def followTest(self, api_url, memberId, authToken):
        startFollowing = Follow(memberId, authToken, "start-following", "79058")
        startFollowing.follow(api_url)
    
        unFollow = Follow(memberId, authToken,"unfollow", "79058")
        unFollow.follow(api_url)

        getFollowers = Follow(memberId, authToken, "get-followers")
        getFollowers.follow(api_url)

        getFollowing = Follow(memberId, authToken, "get-following")
        getFollowing.follow(api_url)


