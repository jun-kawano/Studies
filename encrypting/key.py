from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("Enter password: ") #string
password = password_provided.encode() #convert to bytes

salt = b'\x16\x1b=\xb9x\xa0\xc5\xef9\xe1\xb0k\x7f\xc1t\xd8' #salt came from os.urandom(16)

kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password)) #can only use kdf once

#store the key in a file
f = open("key.key", "wb")
f.write(key)
f.close()
