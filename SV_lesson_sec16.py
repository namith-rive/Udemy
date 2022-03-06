import string
import random

from Crypto.Cipher import AES
from  Crypto.PublicKey import RSA

print(AES.block_size)
print(string.ascii_letters)
key = ''.join(
     random.choice(string.ascii_letters) for _ in range(AES.block_size))
print(key)

iv = ''.join(
     random.choice(string.ascii_letters) for _ in range(AES.block_size))
print(iv)

plaintext = 'hello_world'
cipher = AES.new(key, AES.MODE_CBC,iv)
# #文字長が16文字の倍数になるように調整する
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length

cipher_text = cipher.encrypt(plaintext)
print(cipher_text)

# print(padding_length)
# print(AES.block_size)
# print(len(plaintext) % AES.block_size)
# print(len(plaintext) )
# print( chr(padding_length) )
# print(plaintext)