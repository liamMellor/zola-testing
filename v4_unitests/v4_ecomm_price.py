# Lozin Shakya
# Created: 02/6/2014

import urllib
import urllib2
import json
import random
import string
import re
import time
import os

api_url = 'https://api.zolabooks.com/v4/'

class V4_book_price():
     def __init__ (self, action, isbn):
	self.action = action
	self.isbn = isbn

     def book_price(self):
	book_priceUrl = api_url + 'ecomm/price'
	book_priceValues = {'action' : self.action,
			    'isbn' : self.isbn}
	
	book_priceData = urllib.urlencode(book_priceValues)
	book_priceReq = urllib2.Request(book_priceUrl, book_priceData)
	book_priceResponse = urllib2.urlopen(book_priceReq)
	book_priceJSON = json.load(book_priceResponse)
	
	book_priceContainer = {}
	for x,y in book_priceJSON["data"].iteritems():
            book_priceContainer[x] = y
	
	return book_priceContainer
book_priceTest = V4_book_price("get", "1112223334445")
print book_priceTest.book_price()
