from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("Enter password: ") #string
password = password_provided.encode() #convert to bytes

salt = b'\x16\x1b=\xb9x\xa0\xc5\xef9\xe1\xb0k\x7f\xc1t\xd8'

kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password)) #can only use kdf once
"""
#store the key in a file
f = open("key.key", "wb")
f.write(key)
f.close()
"""
"""
#get the key from file
keyfile = open("key.key", "rb")
key = keyfile.read() #bytes
keyfile.close()
"""
#open the file to encrypt/decrypt
file_name = input("Enter the file to be encrypted: ")
with open(file_name, "rb") as f:
    data = f.read()

fernet = Fernet(key)
#encrypt
encrypted = fernet.encrypt(data)

#decrypt
#encrypted = fernet.decrypt(data)

#write the encrypted file
with open(f"{file_name}.encrypted", "wb") as f:
    f.write(encrypted)

#write the encrypted file
#with open("test.txt.decrypted", "wb") as f:
#    f.write(encrypted)
