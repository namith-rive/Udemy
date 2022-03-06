# import string
# import random
#
# from Crypto.Cipher import AES
# from  Crypto.PublicKey import RSA
#
# #print(AES.block_size)
# #print(string.ascii_letters)
# key = ''.join(
#      random.choice(string.ascii_letters) for _ in range(AES.block_size))
# #print(key)
#
# iv = ''.join(
#      random.choice(string.ascii_letters) for _ in range(AES.block_size))
# #print(iv)
#
# plaintext = 'hello_world'
# cipher = AES.new(key, AES.MODE_CBC,iv)
# # #文字長が16文字の倍数になるように調整する
# padding_length = AES.block_size - len(plaintext) % AES.block_size
# plaintext += chr(padding_length) * padding_length
#
# cipher_text = cipher.encrypt(plaintext)
# print(cipher_text)
#
# # print(padding_length)
# # print(AES.block_size)
# # print(len(plaintext) % AES.block_size)
# # print(len(plaintext) )
# # print( chr(padding_length) )
# # print(plaintext)
#
# cipher2 = AES.new(key, AES.MODE_CBC, iv)
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text[-1])
# print(decrypted_text[:-decrypted_text[-1]])

import base64
import hashlib
import os


# print(hashlib.sha256(b'test').digest())
# print(hashlib.sha256(b'test').digest())

user_name = 'user1'
user_pass = 'password'
db={}

salt = base64.b64encode(os.urandom(32))
print(salt)

def get_digest(password):
    password = bytes(user_pass, 'utf-8')
    digest = hashlib.sha256(salt + password).hexdigest()
    for _ in range(1000):
        digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
    print(digest)
    return digest

db[user_name] = get_digest(user_pass)
#print(db)
def is_login(user_name, password):
    return get_digest(password) == db[user_name]

print(is_login(user_name, user_pass))