from session.v4_session_login import LoginTest
from session.v4_session_account import V4_account
from session.v4_session_logout import V4_logout
from session.v4_session_token import V4_token
from session.v4_session_password import V4_password
from book.v4_book_cnt import V4_books_cnt
from book.v4_book_details import DetailsTest
from collection.v4_collection_lists import CollectionTest
from social.v4_social_follow import Follow
from social.v4_social_activity import ActivityTest
from social.v4_social_member import MemberTest
import json

api_url = 'https://zolabooks.com/api/v4/'

class v4_harness():
    
    def __init__(self):
        global api_url
    
    def runner(self):
        login = LoginTest(api_url)
        
        accountDict = login.activate()
        accountDict = accountDict[1]["data"]
        
        memberId = accountDict["member_id"]
        authToken = accountDict["auth_token"]
        deviceName = accountDict["device_name"]

        passwordInst = V4_password(memberId,authToken,"update","jason-flax-2","kingkong","kingkong","jay.flax@zolabooks.com")
        passwordInst.password(api_url)

        cntInst = V4_books_cnt(memberId,authToken,"get","9781939126009")
        cntInst.count(api_url)
        
        collectionInst = CollectionTest(api_url, memberId, "get-purchased", authToken)
        list = collectionInst.list()
        print list
        list = list[1]["data"]["list"]
        
        first_book = list[5]
        isbn = first_book["details"]["isbn_13"]
                
        #downloadInst = v4_download(memberId, authToken, isbn, "epub")
        #keys = downloadInst.getKeys(api_url)
        
        #keys = keys[0]
                
        followTest(api_url, memberId, authToken)

        ActivityTest(api_url, memberId, authToken).activityTest()
        DetailsTest(api_url, memberId, authToken).detailsTest()
        MemberTest(api_url, memberId, authToken).memberTest()
        
        #tokenInst = V4_token(memberId, authToken, "deactivate")
        #tokenInst.token(api_url)

        #loginInst = V4_login("jason-flax-2","kingkong","swagger","jay.flax@zolabooks.com")
        #loginDict =  loginInst.login(api_url)

        #memberId = loginDict["member_id"]
        #authToken = loginDict["auth_token"]
        #deviceName = loginDict["device_name"]
        
        logoutInst = V4_logout(memberId, authToken, "true")
        #logoutCode = logoutInst.logout(api_url)
        #print logoutCode
        #if int(logoutCode) != 204:
        #    assert False, "not logged out"
        #else:
        #    print "logged out"

def followTest(api_url, memberId, authToken):
    startFollowing = Follow(memberId, authToken, "start-following", "79058")
    startFollowing.follow(api_url)
    
    unFollow = Follow(memberId, authToken,"unfollow", "79058")
    unFollow.follow(api_url)

    getFollowers = Follow(memberId, authToken, "get-followers")
    getFollowers.follow(api_url)

    getFollowing = Follow(memberId, authToken, "get-following")
    getFollowing.follow(api_url)

harness = v4_harness()
harness.runner()
