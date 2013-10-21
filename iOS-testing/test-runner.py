#!/usr/bin/env python
import sys
import argparse
from unittest import TestCase, TestSuite, TestLoader, TextTestRunner
from itertools import islice
from inspect import isclass
from UnitTesting.app_objects import appium_wrapper

test_modules_to_run = ()

test_modules_to_run += (
    'full_suite.full_suite',
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

def run_some_or_all_tests(apppath, num_books, number_of_computers=None, this_machine_number=None):
    '''Initialize appium_wrapper with app path and number of books,
    then run unit tests'''
    global test_modules_to_run
    appium_wrapper.mode = 'same driver each time'
    appium_wrapper.appium_wrapper.apppath = apppath
    if num_books is not None:
        appium_wrapper.appium_wrapper.num_books_options = num_books

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
                        help='number of computers splitting the tests',
                        default=1)
    parser.add_argument('--this_machine_number',
                        type=int,
                        help='number for this machine, starting with 1',
                        default=1)
    parser.add_argument('--num_books',
                        type=int,
                        action='append',
                        help='number of books you wish to purchase (please select an integer 1-20)'
                        )
    args = parser.parse_args()

    return run_some_or_all_tests(args.app_path, args.num_books, args.number_of_computers, args.this_machine_number)

if __name__ == '__main__':
    sys.exit(main())
