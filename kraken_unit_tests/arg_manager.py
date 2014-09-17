import argparse
#                                                 Slightly "un-pythonic" module.....  -___-
useStaging     = False
# Print options
verboseHigh    = False
verboseLow     = False
JSONdump       = False
# API Group Options
TestSession    = False
TestEcomm      = False
TestSocial     = False
TestCollection = False
TestContent    = False
# API endpoint options
SessionIsLoggedIn = False
SessionLogin      = False
SessionAccount    = False
SessionProfile    = False
SessionAvatar     = False
SessionPassword   = False
SessionToken      = False
SessionPing       = False
SocialCnt         = False
SocialActivity    = False
MetadataDetails   = False
SocialMember      = False
SocialFollow      = False
CollectionList    = False
CollectionCur     = False
CollectionPurchase = False
ContentArticle    = False
ContentReview     = False
EcommBounty       = False
EcommSaleable     = False
EcommAddress      = False
EcommCommerce     = False
EcommDownload     = False
RecommendationRec = False
SearchFind        = False
#ContentRSS       = False

# Set the options from command line
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--useStaging",        help="Run all testing on Staging Server *not production*", action="store_true")
    parser.add_argument("--verboseHigh",       help="Maximum verbosity print output. Includes urls for API calls AND JSON Dumps.", action="store_true")
    parser.add_argument("--verboseLow",        help="Lower verbosity print output. Includes urls for API calls." , action="store_true")
    parser.add_argument("--JSONdump",          help="Enable for a pretty() dump of each returned JSON for API endpoint calls through Manager class.", action="store_true")
    
    parser.add_argument("--TestSession",       help="Flag for testing on Session endpoint API calls.", action="store_true")
    parser.add_argument("--TestEcomm",         help="Flag for testing on Ecomm endpoint API calls.", action="store_true")
    parser.add_argument("--TestSocial",        help="Flag for testing on Social endpoint API calls.", action="store_true")
    parser.add_argument("--TestCollection",    help="Flag for testing on Collection endpoint API calls.", action="store_true")
    parser.add_argument("--TestContent",       help="Flag for testing on Content endpoint API calls.", action="store_true")
    
    parser.add_argument("--SessionLogin",      help="Run testing on 'session/login' calls.", action="store_true")
    parser.add_argument("--SessionIsLoggedIn", help="Run testing on 'session/is_logged_in' calls.", action="store_true")
    parser.add_argument("--SessionAccount",    help="Run testing on 'session/account' calls.", action="store_true")
    parser.add_argument("--SessionProfile",    help="Run testing on 'session/profile' calls.", action="store_true")
    parser.add_argument("--SessionAvatar",     help="Run testing on 'session/avatar' calls.", action="store_true")
    parser.add_argument("--SessionPassword",   help="Run testing on 'session/password/ calls.", action="store_true")
    parser.add_argument("--SessionToken",      help="Run testing on 'session/token' calls.", action="store_true")
    parser.add_argument("--SessionPing",       help="Run testing on 'session/ping' calls.", action="store_true")
    parser.add_argument("--MetadataDetails",   help="Run testing on 'metadata/details' calls.", action="store_true")
    parser.add_argument("--ContentArticle",    help="Run testing on 'content/article' calls.", action="store_true")
    parser.add_argument("--ContentReview",     help="Run testing on 'content/review' calls.", action="store_true")
    parser.add_argument("--CollectionList",    help="Run testing on 'collection/list' calls.", action="store_true")
    parser.add_argument("--CollectionCur",     help="Run testing on 'collection/curation' calls.", action="store_true")
    parser.add_argument("--CollectionPurchase",help="Run testing on 'collection/purchase' calls.", action="store_true")
    parser.add_argument("--EcommSaleable",     help="Run testing on 'ecomm/saleable' calls.", action="store_true")
    parser.add_argument("--EcommAddress",      help="Run testing on 'ecomm/address' calls.", action="store_true")
    parser.add_argument("--EcommCommerce",     help="Run testing on 'ecomm/commerce/ calls.", action="store_true")
    parser.add_argument("--EcommBounty",       help="Run testing on 'ecomm/bouty' calls.", action="store_true")
    parser.add_argument("--EcommDownload",     help="Run testing on 'ecomm/download' calls.", action="store_true")
    parser.add_argument("--SocialCnt",         help="Run testing on 'social/cnt calls.", action="store_true")
    parser.add_argument("--SocialFollow",      help="Run testing on 'social/follow' calls.", action="store_true")
    parser.add_argument("--SocialActivity",    help="Run testing on 'social/activity' calls.", action="store_true")
    parser.add_argument("--SocialMember",      help="Run testing on 'social/member' calls.", action="store_true")
    parser.add_argument("--RecommendationRec", help="Run testing on 'recommendation/rec' calls.", action="store_true")
    parser.add_argument("--SearchFind",        help="Run testing on 'search/find' calls.", action="store_true")
    #parser.add_argument("--testContentRSS",   help="Run testing on 'content/rss' calls.", action="store_true")
    
    # parse
    args = parser.parse_args()
    global verboseHigh, verboseLow, JSONdump, SessionLogin, SessionIsLoggedIn, SocialCnt, SocialActivity, MetadataDetails, SocialMember, SocialFollow, CollectionList, CollectionCur, CollectionPurchase,ContentArticle, ContentReview, EcommBounty, EcommSaleable, EcommAddress, EcommCommerce, EcommDownload, RecommendationRec, SearchFind, SessionAccount, SessionProfile, SessionAvatar, SessionPassword, SessionToken, SessionPing, useStaging, TestSession, TestEcomm, TestSocial, TestContent, TestCollection
    # set
    verboseHigh       = args.verboseHigh
    verboseLow        = args.verboseLow
    JSONdump          = args.JSONdump
    
    TestSession       = args.TestSession
    TestEcomm         = args.TestEcomm
    TestSocial        = args.TestSocial
    TestContent       = args.TestContent
    TestCollection    = args.TestCollection
    
    SessionLogin      = args.SessionLogin
    SessionIsLoggedIn = args.SessionIsLoggedIn
    SocialCnt         = args.SocialCnt
    SocialActivity    = args.SocialActivity
    MetadataDetails   = args.MetadataDetails
    SocialMember      = args.SocialMember
    SocialFollow      = args.SocialFollow
    CollectionList    = args.CollectionList
    CollectionCur     = args.CollectionCur
    CollectionPurchase= args.CollectionPurchase
    ContentArticle    = args.ContentArticle
    ContentReview     = args.ContentReview
    #ContentRSS       = args.ContentRSS
    EcommBounty       = args.EcommBounty
    EcommSaleable     = args.EcommSaleable
    EcommAddress      = args.EcommAddress
    EcommCommerce     = args.EcommCommerce
    EcommDownload     = args.EcommDownload
    RecommendationRec = args.RecommendationRec
    SearchFind        = args.SearchFind
    SessionAccount    = args.SessionAccount
    SessionProfile    = args.SessionProfile
    SessionAvatar     = args.SessionAvatar
    SessionPassword   = args.SessionPassword
    SessionToken      = args.SessionToken
    SessionPing       = args.SessionPing
    useStaging        = args.useStaging

# If no API args are provided, test all endpoints
def default_run():
    
    global SessionLogin, SessionIsLoggedIn, SocialCnt, SocialActivity, MetadataDetails, SocialMember, SocialFollow, CollectionList, CollectionCur, CollectionPurchase, ContentArticle,  ContentReview, EcommBounty, EcommSaleable, EcommAddress, EcommCommerce, EcommDownload, RecommendationRec, SessionAccount, SearchFind, SessionProfile, SessionAvatar, SessionPassword, SessionToken, SessionPing
    
    
    if  SessionLogin == False and SessionIsLoggedIn == False and SessionAccount == False and SessionProfile == False and SessionAvatar == False and SessionPassword == False and SessionToken == False and SessionPing == False and SocialCnt == False and SocialActivity == False and MetadataDetails == False and SocialMember == False and SocialFollow == False and CollectionList == False and CollectionCur == False and ContentArticle == False and ContentReview == False and EcommBounty == False and EcommSaleable == False and EcommAddress == False and EcommCommerce == False and EcommDownload == False and RecommendationRec == False and SearchFind == False and CollectionPurchase == False:
        
        print "No arguments given. Testing all endpoints by default."
        SessionLogin      = True
        SessionIsLoggedIn = True
        SessionAccount    = True
        SessionProfile    = True
        SessionAvatar     = True
        SessionPing       = True
        SocialCnt         = True
        SocialActivity    = True
        MetadataDetails   = True
        SocialMember      = True
        SocialFollow      = True
        CollectionList    = True
        CollectionCur     = True
        CollectionPurchase= True
        ContentArticle    = True
        ContentReview     = True
        EcommBounty       = True
        EcommSaleable     = True
        EcommAddress      = True
        EcommCommerce     = True
        EcommDownload     = True
        RecommendationRec = True
        SearchFind        = True
        SessionPassword   = True
        SessionToken      = True
        #ContentRSS       = True

def session_run():
    global SessionLogin, SessionIsLoggedIn, SessionPassword, SessionPing, SessionProfile, SessionToken, SessionAccount, SessionAvatar, TestSession
    if TestSession == True:
        SessionLogin      = True
        SessionIsLoggedIn = True
        SessionAccount    = True
        SessionProfile    = True
        SessionAvatar     = True
        SessionPing       = True
        SessionPassword   = True
        SessionToken      = True

def ecomm_run():
    global EcommAddress, EcommBounty, EcommCommerce, EcommDownload, EcommSaleable, TestEcomm
    if TestEcomm == True:
        EcommBounty       = True
        EcommSaleable     = True
        EcommAddress      = True
        EcommCommerce     = True
        EcommDownload     = True

def social_run():
    global SocialCnt, SocialFollow, SocialMember, SocialActivity, TestSocial
    if TestSocial == True:
        SocialCnt         = True
        SocialActivity    = True
        SocialMember      = True
        SocialFollow      = True

def collection_run():
    global CollectionCur, CollectionList, TestCollection
    if TestCollection == True:
        CollectionCur  = True
        CollectionList = True
        CollectionPurchase = True

def content_run():
    global ContentArticle, ContentReview, TestContent
    if TestContent == True:
        ContentArticle = True
        ContentReview  = True