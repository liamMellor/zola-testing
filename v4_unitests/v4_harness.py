from session.v4_session_login import V4_login
from session.v4_session_account import V4_account
from session.v4_session_logout import V4_logout
from session.v4_session_token import V4_token
from session.v4_session_password import V4_password
from book.v4_book_cnt import V4_books_cnt
from book.v4_book_download import v4_download
from book.v4_book_details import DetailsTest
from collection.v4_collection_lists import v4coll
from social.v4_social_follow import Follow
from social.v4_social_activity import ActivityTest
import json

api_url = 'https://zolaqc.com/api/v4/'

class v4_harness():
    
    def __init__(self):
        global api_url
    
    def runner(self):

        accountInst = V4_account("create", "jay.flax@zolabooks.com", "kingkong", "Jay", "Flax", "26", "10", "1990", "swagger", "m")
        accountDict = accountInst.account(api_url)

        memberId = accountDict["member_id"]
        authToken = accountDict["auth_token"]
        deviceName = accountDict["device_name"]

        try:
            memberId = int(memberId)
        except ValueError:
            pass
        if authToken.isalnum() is False:
            assert False, "auth_token is non alpha numeric"
        if deviceName.isalpha() is False:
            assert False, "device_name is non alphabetical"

        passwordInst = V4_password(memberId,authToken,"update","jason-flax-2","kingkong","kingkong","jay.flax@zolabooks.com")
        passwordInst.password(api_url)

        cntInst = V4_books_cnt(memberId,authToken,"get","9781939126009")
        cntInst.count(api_url)
        
        collectionInst = v4coll(memberId, authToken, "get-purchased", "purchased")
        list = collectionInst.list(api_url)
        list = list["list"]
        
        first_book = list[5]
        isbn = first_book["details"]["isbn_13"]
        
        downloadInst = v4_download(memberId, authToken, isbn, "epub")
        keys = downloadInst.getKeys(api_url)
        
        keys = keys[0]
                
        followTest(api_url, memberId, authToken)
        
        ActivityTest(api_url, memberId, authToken).activityTest()
        print DetailsTest(api_url, memberId, authToken).detailsTest()
        
        #tokenInst = V4_token(memberId, authToken, "deactivate")
        #tokenInst.token(api_url)

        #loginInst = V4_login("jason-flax-2","kingkong","swagger","jay.flax@zolabooks.com")
        #loginDict =  loginInst.login(api_url)

        #memberId = loginDict["member_id"]
        #authToken = loginDict["auth_token"]
        #deviceName = loginDict["device_name"]
        
        #logoutInst = V4_logout(memberId, authToken, "true")
        #logoutCode = logoutInst.logout(api_url)
        #print logoutCode
        #if int(logoutCode) != 204:
        #    assert False, "not logged out"
        #else:
        #    print "logged out"

def followTest(api_url, memberId, authToken):
    startFollowing = Follow(memberId, authToken, "start-following", "79058")
    print startFollowing.follow(api_url)
    
    unFollow = Follow(memberId, authToken,"unfollow", "79058")
    print unFollow.follow(api_url)

    getFollowers = Follow(memberId, authToken, "get-followers")
    print getFollowers.follow(api_url)

    getFollowing = Follow(memberId, authToken, "get-following")
    print getFollowing.follow(api_url)

harness = v4_harness()
harness.runner()
