from endpoints.session.v4_session_login import LoginTest
from endpoints.session.v4_session_isLoggedIn import isLoggedTest
from endpoints.session.v4_session_account import accountTest
from endpoints.session.v4_session_profile import profileTest
from endpoints.session.v4_session_avatar import avatarTest
from endpoints.session.v4_session_logout import logoutTest
from endpoints.session.v4_session_token import tokenTest
from endpoints.session.v4_session_password import passwordTest
from endpoints.session.v4_session_ping import pingTest
from endpoints.content.v4_content_article import articleTest
from endpoints.content.v4_content_review import reviewTest
#from endpoints.content.v4_content_rss import rssTest XML data handling not implemented
from endpoints.social.v4_social_cnt import cntTest
from endpoints.metadata.v4_metadata_details import DetailsTest
from endpoints.collection.v4_collection_lists import CollectionTest
from endpoints.collection.v4_collection_curation import curationTest
from endpoints.collection.v4_collection_purchase import purchaseTest
from endpoints.ecomm.v4_ecomm_saleable import saleTest
from endpoints.ecomm.v4_ecomm_address import addressTest
from endpoints.ecomm.v4_ecomm_commerce import commerceTest
from endpoints.ecomm.v4_ecomm_bounty import bountyTest
from endpoints.ecomm.v4_ecomm_download import downloadTest
from endpoints.social.v4_social_follow import Follow
from endpoints.social.v4_social_activity import ActivityTest
from endpoints.social.v4_social_member import MemberTest
from endpoints.recommendation.v4_recommendation_rec import recTest
from endpoints.search.v4_search_find import findTest
from service_base.service import Manager
import json
import arg_manager
import time

# The account being used has the following credentials
# user name : "mail-rollem"
# email     : "liam.mellor@zolabooks.com"
# password  : "testing123"
# device    : "The DeLorean
# member_id : "273196"

# ABOVE IS OLD^^^^^^^ USE BELOW
# user name : michael-jordan
# email     : michael.jordan@zolabooks.com
# password  : 123456123456
# device    : "The DeLorean"
# member_id : "272820"


# Parse Command Line Options
arg_manager.get_args()

arg_manager.collection_run()
arg_manager.social_run()
arg_manager.content_run()
arg_manager.ecomm_run()
arg_manager.session_run()
arg_manager.default_run()


# Specify Production or Staging Server
if arg_manager.useStaging == True:
    api_url = 'https://api-staging.zo.la/v4/'
    print "You are testing on the Staging Server. Endpoints image/dispay, preview/display, session/login_social, session/avatar/set and content/rss are not tested."
else:
    print "You are testing on the Production Server. Endpoints image/dispay, preview/display, session/login_social, session/avatar/set and content/rss are not tested."
    api_url = 'https://api.zo.la/v4/'


class v4_harness():
    
    def __init__(self):
        global api_url
    
    def runner(self):
        
        # Login / Necessary for other tests to run
        login        = LoginTest(api_url)
        accountDict  = login.activate()
        accountDict  = accountDict[1]["data"]
        memberId     = accountDict["member_id"]
        authToken    = accountDict["auth_token"]
        deviceName   = accountDict["device_name"]
        logoutInst   = logoutTest(api_url, memberId, authToken)
        logoutInst.logout()
        # Re login after logout test to complete other tests
        time.sleep(10)
        login        = LoginTest(api_url)
        accountDict  = login.activate1()
        accountDict  = accountDict[1]["data"]
        memberId     = accountDict["member_id"]
        authToken    = accountDict["auth_token"]
        deviceName   = accountDict["device_name"]
        
        # Session/is_logged_in gets user creds if they're logged in
        if arg_manager.SessionIsLoggedIn == True:
            logCheck = isLoggedTest(api_url, memberId, authToken)
            logCheck.checkLog()
        
        # Session/account creates an account or sees if one exists
        if arg_manager.SessionAccount == True:
            accountInstance = accountTest(api_url, memberId, authToken)
            accountInstance.account()
        
        # Session/password updates a password or sends an email to update               # jason-flax-2 : kingkong
        if arg_manager.SessionPassword == True:
            passwordInstance = passwordTest(api_url, memberId, authToken)
            passwordInstance.password()
        
        # Re-login because tokens were deactivated when password was reset above^
        login        = LoginTest(api_url)
        accountDict  = login.activate1()
        accountDict  = accountDict[1]["data"]
        memberId     = accountDict["member_id"]
        authToken    = accountDict["auth_token"]
        deviceName   = accountDict["device_name"]
        
        # Session/profile sets profile values or gets a profile
        if arg_manager.SessionProfile == True:
            profileInstance = profileTest(api_url, memberId, authToken)
            profileInstance.profile()
        
        # Session/avatar uploads or removes a user's avatar
        if arg_manager.SessionAvatar == True:
            avatarInstance = avatarTest(api_url, memberId, authToken)
            avatarInstance.avatar()
        
        # Session/ping returns true if under three sesions are being updated
        if arg_manager.SessionPing == True:
            pingInstance = pingTest(api_url, memberId, authToken)
            pingInstance.ping()
        
        # Metadata/details retrieve metadata details for book or author
        if arg_manager.MetadataDetails == True:
            detailsInstance = DetailsTest(api_url, memberId, authToken)
            detailsInstance.details()
        
        # Content/article displays articles associated with a 'filter_id'
        if arg_manager.ContentArticle == True:
            articleInst = articleTest(api_url)
            articleInst.article()
        
        # Content/review displays reviews for a specific isbn
        if arg_manager.ContentReview == True:
            reviewInst = reviewTest(api_url)                    
            reviewInst.review()
        
        '''
        # Content/rss displays an RSS feed of 25 articles
        if arg_manager.ContentRSS == True:
            rssInst = rssTest(api_url)
            rssInst.rss()
        '''
        
        # Collection/lists retrieves a user's list of books
        if arg_manager.CollectionList == True:
            collectionInst = CollectionTest(api_url, memberId, authToken)
            collectionInst.list()
            #list           = list[1]["data"]["list"]
            #first_book     = list[5]
            #isbn           = first_book["details"]["isbn"]
            #downloadInst = v4_download(memberId, authToken, isbn, "epub")
            #keys = downloadInst.getKeys(api_url)
            #keys = keys[0]
         
        # Collection/curation retrieves curated list of books
        if arg_manager.CollectionCur == True:
            curationInstance = curationTest(api_url, memberId, authToken)   #9780525478812 Fault in our stars
            curationInstance.curation()
        
        # Collection/purchase retreives list of purchased books
        if arg_manager.CollectionPurchase == True:
            purchaseInstance = purchaseTest(api_url, memberId, authToken)
            purchaseInstance.purchase()
         
        # Ecomm/saleable retrieves a book sales data
        if arg_manager.EcommSaleable == True:
            saleInstance = saleTest(api_url)
            saleInstance.sale()

        # Ecomm/address manage eCommerce shipping and billing address
        if arg_manager.EcommAddress == True and arg_manager.EcommCommerce == False:
            addressInst   = addressTest(api_url, memberId, authToken)
            addressInst.address()
        
        # Ecomm/commerce manages eCommerce session info like cart, payments, etc. Also
        if arg_manager.EcommCommerce == True:
            commerceInstance = commerceTest(api_url, memberId, authToken)
            addressInst      = addressTest(api_url, memberId, authToken)
            commerceInstance.commerceInit()
            addressInst.address()
            commerceInstance.commerce()

        # Ecomm/bounty retrieves list of free books
        if arg_manager.EcommBounty == True:
            bountyInstance = bountyTest(api_url, memberId, authToken)
            bountyInstance.bounty()
        
        # Ecomm/download download an epub and get pertinent information
        if arg_manager.EcommDownload == True:
            downloadInstance = downloadTest(api_url, memberId, authToken)
            downloadInstance.download()
        
        # Social/Activity Set and get activity
        if arg_manager.SocialActivity == True:
            activityInst = ActivityTest(api_url, memberId, authToken)
            activityInst.activityTest()

        #  Social/cnt retrieves a count number of activites user has in their feed
        if arg_manager.SocialCnt == True:
            cntInst = cntTest(api_url, memberId, authToken)
            cntInst.count()
            
        # Social/Follow follow or unfollow user or author
        if arg_manager.SocialFollow == True:
            sets = "############################# FOLLOW ##################################"
            print Manager.WARNING + sets + Manager.ENDC
            follower = Follow(api_url, memberId, authToken)
            follower.followTest(api_url, memberId, authToken)
        
        # Social/member retrieve member stream
        if arg_manager.SocialMember == True:
            memberInstance = MemberTest(api_url, memberId, authToken)
            memberInstance.memberTest()
        
        # Recommendation/rec displays a list of recommendations
        if arg_manager.RecommendationRec == True:
            recInstance = recTest(api_url)
            recInstance.rec()

        # Seach/find displays search results
        if arg_manager.SearchFind == True:
            findInstance = findTest(api_url)
            findInstance.find()

        # This is last because it deletes token and nullifies the rest of the tests.
        # Session/token generates or deactivates a session token
        if arg_manager.SessionToken == True:
            tokenInstance = tokenTest(api_url, memberId, authToken)
            data       = tokenInstance.regenerate()
            data       = data[1]["data"]
            memberId   = data["member_id"]
            authToken  = data["auth_token"]
            deviceName = data["device_name"]
            tokenInstance2 = tokenTest(api_url, memberId, authToken)
            tokenInstance2.deactivate()

harness = v4_harness()
harness.runner()
