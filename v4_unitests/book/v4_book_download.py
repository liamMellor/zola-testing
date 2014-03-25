import urllib 
import urllib2
import json
import os
import zipfile
from zbdrm import zbdrm

files = []
files_for_reading = []

class v4_download():
	
	def __init__(self, auth_member_id, auth_token, isbn, type):
		global api_url
		self.auth_member_id = auth_member_id
		self.auth_token = auth_token
		self.isbn = isbn
		self.type = type 
		self.bs = 32

	def getKeys(self, api_url):
		encoded_vars = urllib.urlencode({'auth_member_id' : self.auth_member_id, 
						 'auth_token' : self.auth_token,
						 'action' : 'get-keys',
						 'isbn' : self.isbn,
						 'type' :self.type })

		keysUrl = api_url + "book/download"
		
		keysReq = urllib2.Request(keysUrl, encoded_vars)
		resp = urllib2.urlopen(keysReq)
		jsonResp = json.load(resp)
		
		return jsonResp["data"]
	
	def downloadEpub(self, api_url, uuid, uri, email):
		encoded_vars = urllib.urlencode({'auth_member_id' : self.auth_member_id,
                                                 'auth_token' : self.auth_token,
                                                 'action' : 'download',
                                                 'isbn': self.isbn,
                                                 'type' :self.type })

		keysUrl = api_url + "book/download"
		
                keysReq = urllib2.Request(keysUrl, encoded_vars)
                resp = urllib2.urlopen(keysReq)
		new_file = './'+self.isbn+'.epub'
		dest = './'+self.isbn
		with open(new_file, 'w') as f:
			f.write(resp.read())
		
		self.unzipEpub(new_file, dest)
		self.listFiles(dest)
		self.parseFiles(dest)
		
		zbdrmInst = zbdrm( uuid, email,uri)
		
		for q in files_for_reading:
			with open (q, "r") as myfile:
				encoded_data = myfile.read()
				decrypted_data = zbdrmInst.decrypt(bytearray(encoded_data))
				print (decrypted_data)
				decrypted_chapter = open(q, "w")
				decrypted_chapter.write(decrypted_data)
				decrypted_chapter.close()
				

	def pad(self, s):
		return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
	
	def unpad(self, s):
		return s[:-ord(s[len(s)-1:])]
	def unzipEpub(self, source_filename, dest_dir):
		with zipfile.ZipFile(source_filename) as zf:
			for member in zf.infolist():
				words = member.filename.split('/')
				path = dest_dir
				for word in words[:-1]:
					drive, word = os.path.splitdrive(word)
					head, word = os.path.split(word)
					if word in (os.curdir, os.pardir, ''): continue
					path = os.path.join(path, word)
					zf.extract(member, path)

	def listFiles(self, source_folder):
		for f in os.listdir(source_folder): 
			if os.path.isfile(self.join(source_folder,f)):
				files.append(self.join(source_folder,f))
			else:
				self.listFiles(self.join(source_folder,f))

	def parseFiles(self, source_folder):
		for f in files:
			if f.endswith(".html") or f.endswith(".chtml") or f.endswith(".xhtml") or f.endswith(".htm") or f.endswith(".chtm"):
				files_for_reading.append(f)

	def join(self, str_1, str_2):
		return str_1 + "/" + str_2
