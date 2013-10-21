#!/usr/bin/env python
import sys
import argparse
from unittest import TestCase, TestSuite, TestLoader, TextTestRunner
from itertools import islice
from inspect import isclass
from UnitTesting.page_objects import webdriver_wrapper

test_modules_to_run = ()

'''
test_modules_to_run += (
    'connect_dropdown_friends',
    'search_test',
    'sub_category_test',
)'''

test_modules_to_run += (
    'activity_star.star_users_activity',
)

test_modules_to_run += (
    'add_to_list_modal.addtolist_flow_notsignedin_test',
    'add_to_list_modal.addtolist_flow_signedin_test',
    'add_to_list_modal.addtolist_flow_signup_test',
)

test_modules_to_run += (
    'add_to_list_profile.addtolist_flow_notsignedin_profile',
    'add_to_list_profile.addtolist_flow_signedin_profil',
    'add_to_list_profile.addtolist_flow_signup_profile',
)

test_modules_to_run += (
    'category_dropdown_links.dropdown_art',
    'category_dropdown_links.dropdown_bio',
    'category_dropdown_links.dropdown_business',
    'category_dropdown_links.dropdown_children',
    'category_dropdown_links.dropdown_classics',
    'category_dropdown_links.dropdown_crafts',
    'category_dropdown_links.dropdown_crime',
    'category_dropdown_links.dropdown_criticism',
    'category_dropdown_links.dropdown_drama',
    'category_dropdown_links.dropdown_fiction',
    'category_dropdown_links.dropdown_graphic',
    'category_dropdown_links.dropdown_historical',
    'category_dropdown_links.dropdown_history',
    'category_dropdown_links.dropdown_humor',
    'category_dropdown_links.dropdown_litfic',
    'category_dropdown_links.dropdown_nonfiction',
    'category_dropdown_links.dropdown_parenting',
    'category_dropdown_links.dropdown_politics',
    'category_dropdown_links.dropdown_reference',
    'category_dropdown_links.dropdown_religion',
    'category_dropdown_links.dropdown_romance',
    'category_dropdown_links.dropdown_science',
    'category_dropdown_links.dropdown_scifi',
    'category_dropdown_links.dropdown_selfhelp',
    'category_dropdown_links.dropdown_travel',
    'category_dropdown_links.dropdown_urban',
    'category_dropdown_links.dropdown_ya',
)

test_modules_to_run += (
    'connect_dropdown_links.authors',
    'connect_dropdown_links.booksellers',
    'connect_dropdown_links.curators',
    'connect_dropdown_links.friends_not_signed_in',
    'connect_dropdown_links.friends_signed_in',
    'connect_dropdown_links.friends_sign_up',
    'connect_dropdown_links.publishers',
)

test_modules_to_run += (
    'follow_acp_list.follow_flow_notsignedin_list',
    'follow_acp_list.follow_flow_signedin_list',
    'follow_acp_list.follow_flow_signup_list',
)

test_modules_to_run += (
    'follow_full_profile.follow_flow_notsignedin_profile',
    'follow_full_profile.follow_flow_signedin_profile',
    'follow_full_profile.follow_flow_signup_profile',
)

test_modules_to_run += (
    'follow_modal.follow_flow_notsignedin_modal',
    'follow_modal.follow_flow_signedin_modal',
    'follow_modal.follow_flow_signup_modal',
)

test_modules_to_run += (
    'homepage_category_links.homepage_art',
    'homepage_category_links.homepage_bio',
    'homepage_category_links.homepage_business',
    'homepage_category_links.homepage_children',
    'homepage_category_links.homepage_classics',
    'homepage_category_links.homepage_crafts',
    'homepage_category_links.homepage_crime',
    'homepage_category_links.homepage_criticism',
    'homepage_category_links.homepage_drama',
    'homepage_category_links.homepage_fiction',
    'homepage_category_links.homepage_graphic',
    'homepage_category_links.homepage_historical',
    'homepage_category_links.homepage_history',
    'homepage_category_links.homepage_humor',
    'homepage_category_links.homepage_litfic',
    'homepage_category_links.homepage_nonfiction',
    'homepage_category_links.homepage_parenting',
    'homepage_category_links.homepage_politics',
    'homepage_category_links.homepage_reference',
    'homepage_category_links.homepage_religion',
    'homepage_category_links.homepage_romance',
    'homepage_category_links.homepage_science',
    'homepage_category_links.homepage_scifi',
    'homepage_category_links.homepage_selfhelp',
    'homepage_category_links.homepage_travel',
    'homepage_category_links.homepage_urban',
    'homepage_category_links.homepage_ya',
)

test_modules_to_run += (
    'homepage_links.all_categories',
    'homepage_links.bottom_about_zola',
    'homepage_links.bottom_contact_us',
    'homepage_links.bottom_copyright_icon',
    'homepage_links.bottom_copyright',
    'homepage_links.bottom_facebook',
    'homepage_links.bottom_help',
    'homepage_links.bottom_news',
    'homepage_links.bottom_privacy',
    'homepage_links.bottom_terms',
    'homepage_links.bottom_twitter',
    'homepage_links.new_releases_bio',
    'homepage_links.new_releases_business',
    'homepage_links.new_releases_fiction',
    'homepage_links.new_releases_history',
    'homepage_links.new_releases_romance',
    'homepage_links.new_releases_scifi',
    'homepage_links.new_releases_scitech',
    'homepage_links.new_releases_selfhelp',
    'homepage_links.new_releases_thrillers',
    #'homepage_links.new_releases_ya',
    'homepage_links.see_all_fiction_new_releases',
    'homepage_links.see_all_nonfiction_new_releases',
    'homepage_links.side_feed_notsignedin',
    'homepage_links.side_feed_signedin',
    'homepage_links.side_feed_signup',
    'homepage_links.side_more_zola_bestsellers',
    'homepage_links.side_nyt_bestsellers',
    'homepage_links.side_people_finder_notsignedin',
    'homepage_links.side_people_finder_signedin',
    'homepage_links.side_people_finder_signup',
    'homepage_links.side_usa_today_bestsellers',
    'homepage_links.user_in_the_feed',
    'homepage_links.wishlist_notsignedin',
    'homepage_links.wishlist_signedin',
    'homepage_links.wishlist_signup',
    'homepage_links.zola_exclusives',
    'homepage_links.zola_network_notsignedin',
    'homepage_links.zola_network_signedin',
    'homepage_links.zola_network_signup',
)
'''
test_modules_to_run += (
    'homepage_links.navigation_bar_links.about_zola',
    'homepage_links.navigation_bar_links.bestsellers',
    'homepage_links.navigation_bar_links.deals',
    'homepage_links.navigation_bar_links.find_great_ebooks',
    'homepage_links.navigation_bar_links.house_icon',
    'homepage_links.navigation_bar_links.my_ebooks',
    'homepage_links.navigation_bar_links.my_zola',
    'homepage_links.navigation_bar_links.new_releases',
)
'''
test_modules_to_run += (
    'message.user_message',
)

test_modules_to_run += (
    'my_ebook_links.all_books_see_all',
    'my_ebook_links.purchased_see_all',
    'my_ebook_links.wishlist_see_all',
)

test_modules_to_run += (
    'my_ebook_links.top_menu.lists',
    'my_ebook_links.top_menu.preordered',
    'my_ebook_links.top_menu.purchased',
    'my_ebook_links.top_menu.rated',
    'my_ebook_links.top_menu.want_to_read',
)
'''
test_modules_to_run += (
    'my_zola_links.billing_info',
    'my_zola_links.collection_book_link',
    'my_zola_links.collection_tab',
    'my_zola_links.edit_profile',
    'my_zola_links.find_people',
    'my_zola_links.followers_tab',
    'my_zola_links.following_tab',
    'my_zola_links.list_tab',
    'my_zola_links.messages_tab',
    'my_zola_links.profile_picture',
    'my_zola_links.sort_everything',
    'my_zola_links.sort_just_me',
    'my_zola_links.starred_tab',
)
'''
test_modules_to_run += (
    'pledge_full_profile.pledge_flow_notsignedin_profile_test',
    'pledge_full_profile.pledge_flow_signedin_profile_test',
    'pledge_full_profile.pledge_flow_signup_profile_test',
)

test_modules_to_run += (
    'pledge_modal.pledge_flow_notsignedin_test',
    'pledge_modal.pledge_flow_signedin_test',
    'pledge_modal.pledge_flow_signup_test',
)

test_modules_to_run += (
    'purchase_book_list.purchase_flow_notsignedincc_list',
    'purchase_book_list.purchase_flow_notsignedin_list',
    'purchase_book_list.purchase_flow_signedincc_list',
    'purchase_book_list.purchase_flow_signedin_list',
    'purchase_book_list.purchase_flow_signup_list',
)

test_modules_to_run += (
    'purchase_full_profile.purchase_flow_notsignedincc_profil',
    'purchase_full_profile.purchase_flow_notsignedin_profile',
    'purchase_full_profile.purchase_flow_signedincc_profile',
    'purchase_full_profile.purchase_flow_signedin_profile',
    'purchase_full_profile.purchase_flow_signup_profile',
)

test_modules_to_run += (
    'purchase_modal.purchase_flow_notsignedincc_modal',
    'purchase_modal.purchase_flow_notsignedin_modal',
    'purchase_modal.purchase_flow_signedincc_modal',
    'purchase_modal.purchase_flow_signedin_modal',
    'purchase_modal.purchase_flow_signup_modal',
)

test_modules_to_run += (
    'rating_book_list.rating_flow_notsignedin_list',
    'rating_book_list.rating_flow_signedin_list',
    'rating_book_list.rating_flow_signup_list',
)

test_modules_to_run += (
    'rating_full_profile.rating_flow_notsignedin_profile',
    'rating_full_profile.rating_flow_signedin_profile',
    'rating_full_profile.rating_flow_signup_profile',
)

test_modules_to_run += (
    'rating_modal.rating_flow_notsignedin_modal',
    'rating_modal.rating_flow_signedin_modal',
    'rating_modal.rating_flow_signup_modal',
)

test_modules_to_run += (
    'recommend_full_profile.recommend_flow_notsignedin_profile',
    'recommend_full_profile.recommend_flow_signedin_profil',
    'recommend_full_profile.recommend_flow_signup_profil',
)

test_modules_to_run += (
    'recommend_modal.recommend_flow_notsignedin_modal',
    'recommend_modal.recommend_flow_signedin_modal',
    'recommend_modal.recommend_flow_signup_modal',
)

test_modules_to_run += (
    'your_collection_links.all_rated',
    'your_collection_links.edit_devices',
    'your_collection_links.favorites',
    'your_collection_links.not_for_me',
    'your_collection_links.open_book_modal',
    'your_collection_links.preordered',
    'your_collection_links.private_books',
    'your_collection_links.purchased',
    'your_collection_links.view_all',
    'your_collection_links.wishlist',
)

test_modules_to_run = ['UnitTesting.unit_tests.'+x for x in test_modules_to_run]

## chunkIt() modified from http://stackoverflow.com/a/2130035/2016290
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        if num == 1:
            yield seq[int(last):]
            last += avg + 1
        else:
            yield seq[int(last):int(last + avg)]
            last += avg
        num -= 1

def run_some_or_all_tests(base_url, browsers, number_of_computers=None, this_machine_number=None):
    '''Initialize webdriver_wrapper with base_url, browsers, and 'single' mode,
    then run unit tests, either all or subset if split up'''
    global test_modules_to_run
    webdriver_wrapper.mode = 'single'
    webdriver_wrapper.webdriver_wrapper._baseURL = base_url
    webdriver_wrapper.webdriver_wrapper._browsers = browsers

    if number_of_computers:
        if not this_machine_number:
            print 'Error: this_machine_number is required if number_of_computers is given'
            return 1
        ## split out the chunk for this machine to test
        generator = chunkIt(test_modules_to_run, number_of_computers)
        idx = this_machine_number - 1
        test_modules_to_run = list(islice(generator, idx, idx+1))[0]

    test_suite = TestSuite()
    test_loader = TestLoader()

    for test_mod in test_modules_to_run:
        test_mod = __import__(test_mod, fromlist=test_mod.split('.')[-1:])
        attributes = map(lambda attr: getattr(test_mod, attr), dir(test_mod))
        test_classes = [x for x in attributes if isclass(x) and issubclass(x, TestCase)]
        for test_class in test_classes:
            test_suite.addTests(test_loader.loadTestsFromTestCase(test_class))

    TextTestRunner(verbosity=2).run(test_suite)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    def url_check(string):
        import re
        if re.match(r'https?://\w', string):
            return string
        raise argparse.ArgumentTypeError('"%s" is not a valid URL' % (string,))

    parser = argparse.ArgumentParser(description=run_some_or_all_tests.__doc__)
    parser.add_argument('--base_url', type=url_check, help='base URL for tests, which must start with https:// or http://', required=True)

    parser.add_argument('--number_of_computers', type=int, help='number of computers splitting the tests')
    parser.add_argument('--this_machine_number', type=int, help='number for this machine, starting with 1')

    parser.add_argument('--test_firefox', action='store_true', help='test using Firefox (default test browser unless others are explicitly specified)')
    parser.add_argument('--test_chrome', action='store_true', help='test using Google Chrome')
    parser.add_argument('--test_safari', action='store_true', help='test using Safari')
    parser.add_argument('--test_ie', action='store_true', help='test using Internet Explorer')
    args = parser.parse_args()

    browsers = []
    if args.test_chrome:  browsers.append('chrome')
    if args.test_safari:  browsers.append('safari')
    if args.test_ie:  browsers.append('ie')
    if not browsers or args.test_firefox:  browsers.append('firefox')

    return run_some_or_all_tests(args.base_url, browsers, args.number_of_computers, args.this_machine_number)

if __name__ == '__main__':
    sys.exit(main())
