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
from social.v4_social_member import MemberTest
from ecomm.v4_ecomm_bounty import V4_bounty
import json
import time

api_url = 'https://zolaqc.com/api/v4/'

class kauf():

    def __init__(self):
        global api_url

    def laufer(self):
        y = 0
        for x in range(2000,2001):
            accountInst = V4_account("create", "zauberer_von_oz"+str(x)+"@zolabooks.com", "kingkong", "Jay", "Flax", "26", "10", "1990", "swagger", "m")
            accountDict = accountInst.account(api_url)
            
            print accountDict

            memberId = accountDict["member_id"]
            authToken = accountDict["auth_token"]
            deviceName = accountDict["device_name"]

            bountyInst = V4_bounty(memberId, authToken, "list", "7560634534324")
            print bountyInst.get(api_url)
            
            y+=1
            
            if y is 2:
                time.sleep(10)
                y = 0

kauffen = kauf()
kauffen.laufer();
