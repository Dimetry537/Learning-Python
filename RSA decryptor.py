from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

public_key = bytes(str(input("Enter public key: ")), 'utf-8')
privat_key = bytes(str(input("Enter privat key: ")), 'utf-8')

msg = bytes(str(input("Enter plain text: ")), 'utf-8')

decryptor = PKCS1_OAEP.new(public_key, privat_key)
decrypted = decryptor.decrypt(msg)
print('Decrypted:', decrypted.decode('utf-8'))