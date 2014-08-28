from service_base.service import Manager

sets = "############################ Profile #################################"

class v4profile():
    
    def __init__(self, auth_member_id, auth_token, action, member_id=None, email=None, bday_d=None, bday_m=None, bday_y=None, receive_newsletter=None, receive_email_if_followed=None, receive_email_if_messaged=None, member_first_name=None, member_last_name=None, member_facebook_username=None, member_twitter_username=None, member_gender=None, member_zip_code=None, member_location=None, member_public_email=None, member_website=None, member_twitter_url=None, member_facebook_url=None, member_phone=None, member_gplus_url=None, member_facebook_id=None, member_gplus_username=None, member_rss_feed=None):
        self.auth_member_id            = auth_member_id
        self.auth_token                = auth_token
        self.action                    = action
        self.member_id                 = member_id
        self.email                     = email
        self.bday_d                    = bday_d
        self.bday_m                    = bday_m
        self.bday_y                    = bday_y
        self.receive_newsletter        = receive_newsletter
        self.receive_email_if_followed = receive_email_if_followed
        self.receive_email_if_messaged = receive_email_if_messaged
        self.member_first_name         = member_first_name
        self.member_last_name          = member_last_name
        self.member_facebook_username  = member_facebook_username
        self.member_twitter_username   = member_twitter_username
        self.member_gender             = member_gender
        self.member_zip_code           = member_zip_code
        self.member_location           = member_location
        self.member_public_email       = member_public_email
        self.member_website            = member_website
        self.member_twitter_url        = member_twitter_url
        self.member_facebook_url       = member_facebook_url
        self.member_phone              = member_phone
        self.member_gplus_url          = member_gplus_url
        self.member_facebook_id        = member_facebook_id
        self.member_gplus_username     = member_gplus_username
        self.member_rss_feed           = member_rss_feed
    
    def profile(self, api_url):
        if self.action == "set":
            self.vals = {   'member_id'                : self.member_id,
                            'auth_member_id'           : self.auth_member_id,
                            'auth_token'               : self.auth_token,
                            'action'                   : self.action,
                            'email'                    : self.email,
                            'bday_d'                   : self.bday_d,
                            'bday_m'                   : self.bday_m,
                            'bday_y'                   : self.bday_y,
                            'receive_newsletter'       : self.receive_newsletter,
                            'receive_email_if_followed' : self.receive_email_if_followed,
                            'receive_email_if_messaged' : self.receive_email_if_messaged,
                            'member_first_name'        : self.member_first_name,
                            'member_last_name'         : self.member_last_name,
                            'member_facebook_username' : self.member_facebook_username,
                            'member_twitter_username'  : self.member_twitter_username,
                            'member_gender'            : self.member_gender,
                            'member_zip_code'          : self.member_zip_code,
                            'member_location'          : self.member_location,
                            'member_public_email'      : self.member_public_email,
                            'member_website'           : self.member_website,
                            'member_twitter_url'       : self.member_twitter_url,
                            'member_facebook_url'      : self.member_facebook_url,
                            'member_phone'             : self.member_phone,
                            'member_gplus_url'         : self.member_gplus_url,
                            'member_facebook_id'       : self.member_facebook_id,
                            'member_gplus_username'    : self.member_gplus_username,
                            'member_rss_feed'          : self.member_rss_feed
                        }
        else:
            self.vals = {   'member_id'                : self.member_id,
                            'auth_member_id'           : self.auth_member_id,
                            'auth_token'               : self.auth_token,
                            'action'                   : self.action,
                            'email'                    : self.email,
                            'bday_d'                   : self.bday_d,
                            'bday_m'                   : self.bday_m,
                            'bday_y'                   : self.bday_y,
                            'receive_newsletter'       : self.receive_newsletter,
                            'receive_email_if_followed': self.receive_email_if_followed,
                            'receive_email_if_messaged': self.receive_email_if_messaged,
                            'first_name'        : self.member_first_name,
                            'last_name'         : self.member_last_name,
                            'facebook_username' : self.member_facebook_username,
                            'twitter_username'  : self.member_twitter_username,
                            'gender'            : self.member_gender,
                            'zip_code'          : self.member_zip_code,
                            'location'          : self.member_location,
                            'public_email'      : self.member_public_email,
                            'website'           : self.member_website,
                            'twitter_url'       : self.member_twitter_url,
                            'facebook_url'      : self.member_facebook_url,
                            'phone'             : self.member_phone,
                            'gplus_url'         : self.member_gplus_url,
                            'facebook_id'       : self.member_facebook_id,
                            'gplus_username'    : self.member_gplus_username,
                            'rss_feed'          : self.member_rss_feed
                        }
        manager = Manager(self.vals)
        manager.request(api_url, "session/profile")

    def profileFail(self, api_url, message):
        if self.action == "set":
            self.vals = {   'member_id'    : self.member_id,
                'auth_member_id'           : self.auth_member_id,
                'auth_token'               : self.auth_token,
                'action'                   : self.action,
                'email'                    : self.email,
                'bday_d'                   : self.bday_d,
                'bday_m'                   : self.bday_m,
                'bday_y'                   : self.bday_y,
                'receive_newsletter'       : self.receive_newsletter,
                'receive_email_if_followed' : self.receive_email_if_followed,
                'receive_email_if_messaged' : self.receive_email_if_messaged,
                'member_first_name'        : self.member_first_name,
                'member_last_name'         : self.member_last_name,
                'member_facebook_username' : self.member_facebook_username,
                'member_twitter_username'  : self.member_twitter_username,
                'member_gender'            : self.member_gender,
                'member_zip_code'          : self.member_zip_code,
                'member_location'          : self.member_location,
                'member_public_email'      : self.member_public_email,
                'member_website'           : self.member_website,
                'member_twitter_url'       : self.member_twitter_url,
                'member_facebook_url'      : self.member_facebook_url,
                'member_phone'             : self.member_phone,
                'member_gplus_url'         : self.member_gplus_url,
                'member_facebook_id'       : self.member_facebook_id,
                'member_gplus_username'    : self.member_gplus_username,
                'member_rss_feed'          : self.member_rss_feed
                }
        else:
            self.vals = {   'member_id'                : self.member_id,
                'auth_member_id'           : self.auth_member_id,
                'auth_token'               : self.auth_token,
                'action'                   : self.action,
                'email'                    : self.email,
                'bday_d'                   : self.bday_d,
                'bday_m'                   : self.bday_m,
                'bday_y'                   : self.bday_y,
                'receive_newsletter'       : self.receive_newsletter,
                'receive_email_if_followed': self.receive_email_if_followed,
                'receive_email_if_messaged': self.receive_email_if_messaged,
                'first_name'        : self.member_first_name,
                'last_name'         : self.member_last_name,
                'facebook_username' : self.member_facebook_username,
                'twitter_username'  : self.member_twitter_username,
                'gender'            : self.member_gender,
                'zip_code'          : self.member_zip_code,
                'location'          : self.member_location,
                'public_email'      : self.member_public_email,
                'website'           : self.member_website,
                'twitter_url'       : self.member_twitter_url,
                'facebook_url'      : self.member_facebook_url,
                'phone'             : self.member_phone,
                'gplus_url'         : self.member_gplus_url,
                'facebook_id'       : self.member_facebook_id,
                'gplus_username'    : self.member_gplus_username,
                'rss_feed'          : self.member_rss_feed
                }
        manager = Manager(self.vals)
        manager.requestFail(api_url, "session/profile", message)

class profileTest():

    def __init__(self, api_url, memberId, authToken):
        self.api_url   = api_url
        self.memberId  = memberId
        self.authToken = authToken

    def profile(self):
        print Manager.WARNING + sets + Manager.ENDC
        
        ############# Invalid Calls
        '''
        # No value checking here so calls below return success. Not a big deal.
        # get invalid memberID profile
        getInvalid = v4profile(self.memberId, self.authToken, 'get', 2731960, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        getInvalid.profileFail(self.api_url, "Attempt to get a profile with invalid Member ID")
        
        # set details for invalid memberID profile
        setInvalid = v4profile(self.memberId, self.authToken, 'set', 2731960, None, None, None, None, None, None, None, 'Fake', 'Name', None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        setInvalid.profileFail(self.api_url, "Attempt to set for profile with invalid Member ID")
        '''
        
        ############# Valid Calls
        profileSet = v4profile(self.memberId, self.authToken, 'set', 273196, 'liam.mellor@zolabooks.com', '20', '10', '1992', 'n', 'n', 'y', 'Liam', 'Mellor', 'liam.mellor', None, 'm', '10012', None, None, None, None, None, None, None, None, None, None)
        profileSet.profile(self.api_url)
        
        profileGet = v4profile(self.memberId, self.authToken, 'get', 273196, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        profileGet.profile(self.api_url)

        profileGetMin = v4profile(self.memberId, self.authToken, 'get-min', 273196, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        profileGetMin.profile(self.api_url)










