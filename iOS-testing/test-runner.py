#!/usr/bin/env python
import sys
import argparse
from unittest import TestCase, TestSuite, TestLoader, TextTestRunner
from itertools import islice
from inspect import isclass
from UnitTesting.app_objects import appium_wrapper
import time

test_modules_to_run = ()

test_modules_to_run += (
                        'full_suite.full_suite',
                        'highlight_suite.highlight_suite',
                        'reply_suite.reply_suite',
                        'progress_suite.progress_suite',
                        #'book_insert.book_insert',
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

def run_some_or_all_tests(apppath, num_books_options, appium_binary_path, appium_output_file, ios_device_id=None, number_of_computers=None, this_machine_number=None, enable_screenshots=False):
    '''Initialize appium_wrapper with app path and number of books,
    then run unit tests'''
    global test_modules_to_run
    appium_wrapper.mode = 'same driver each time'
    appium_wrapper.appium_wrapper.apppath = apppath
    appium_wrapper.screenshots_enabled = enable_screenshots
    
    if num_books_options is not None:
        appium_wrapper.appium_wrapper.num_books_options = num_books_options

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

    outfile = open(appium_output_file, 'w')
    from subprocess import Popen
    cmd = ['appium', '--app', apppath]
    if apppath[:4] == 'com.':  # this is a real device not a simulator
        cmd.append('-U')
        cmd.append(ios_device_id)
    else:  # this is a simulator
        cmd.append('--force-ipad')
    appium_wrapper.appium_process = Popen(cmd, stdout=outfile, stderr=outfile)
    print appium_wrapper.appium_process.returncode and appium_wrapper.appium_process.pid
    try:
        
        time.sleep(10)
        TextTestRunner(verbosity=2).run(test_suite)
    
    finally:
        appium_wrapper.appium_process.kill(); print "Appium Killed"

def main(argv=None):
    if argv is None:
        argv = sys.argv

    def app_check(string):
        import os
        if os.path.exists(string) or string[:4] == 'com.':
            return string
        raise argparse.ArgumentTypeError('"%s" is not a valid App Path' % (string,))

    parser = argparse.ArgumentParser(description=run_some_or_all_tests.__doc__)
    parser.add_argument('--app_path',
                        #type=app_check,
                        #help='app path for tests, must be Bundle ID or App Path',
                        required=True)

    parser.add_argument('--number_of_computers',
                        type=int,
                        help='number of computers splitting the tests')
    parser.add_argument('--this_machine_number',
                        type=int,
                        help='number for this machine, starting with 1')
    parser.add_argument('--num_books',
                        type=int,
                        action='append',
                        help='number of books you wish to purchase (please select an integer 1-20)'
                        )
    parser.add_argument('--appium_binary_path',
                        help='path to appium binary',
                        ##verison 0.10.4 below
                        #default='/usr/local/bin/appium'
                        ##version 0.11.0 below
                        default='/User/Zola/appium/bin/appium.js')
    parser.add_argument('--appium_output_file',
                        help='logfile path to store appium output',
                        default='./appium_logfile.txt')
    parser.add_argument('--ios_device_id',
                        help='UDID - unique device ID for iOS device')
    parser.add_argument('--enable_screenshots',
                        help='enables screen capture, which is disabled by default',
                        action='store_true')
    args = parser.parse_args()

    if args.app_path[:4] == 'com.' and args.ios_device_id is None:
        print 'ERROR: missing --ios_device_id argument'

    return run_some_or_all_tests(args.app_path, args.num_books, args.appium_binary_path, args.appium_output_file, args.ios_device_id, args.number_of_computers, args.this_machine_number, args.enable_screenshots)

if __name__ == '__main__':
    sys.exit(main())
