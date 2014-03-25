from Crypto import Random
from Crypto.Cipher import AES
import base64
import array

class zbdrm:
    def __init__(self, uuid, email, uri):
        self.uuid = bytearray(uuid.encode("utf-8"))
        self.email = bytearray(email.encode("utf-8"))
        self.uri = bytearray(uri.encode("utf-8"))

    def decrypt(self, chapter):
        uuid = self.uuid
        uri = self.uri
        email = self.email

        key = [0xF0] * 32
        key_tmp = bytearray(10000)
        key_tmp_ptr = bytearray()
        
        symmetric_key = bytearray()
        
        key_tmp = 0xF0 * 32
        
        key_tmp_ptr = bytearray(key_tmp);
        
        ptr = uuid;

        for i in range(len(ptr)):
            key_tmp_ptr[i] ^= ptr[i]

        key_tmp_ptr = bytearray(key_tmp);
        ptr = uri;

        for i in range(len(ptr)):
            key_tmp_ptr[i] ^= ptr[i]

        key_tmp_ptr = bytearray(key_tmp);
        ptr = email;

        for i in range(len(ptr)):
            key_tmp_ptr[i] ^= ptr[i]

        symmetric_key = bytearray(key_tmp)

        enc = base64.b64decode(chapter)
        iv = enc[:16]

        key = str(bytearray(symmetric_key[:32]))
        print len(key)
        cipher = AES.new(key, AES.MODE_OFB, iv)
        
        return cipher.decrypt(enc[:16])

