from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii



msg = bytes(str(input("Enter plain text: ")), 'utf-8')

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted.decode('utf-8'))