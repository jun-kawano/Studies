from cryptography.fernet import Fernet

#get the key from file

keyfile = open("key.key", "rb")
key = keyfile.read() #bytes
keyfile.close()
fernet = Fernet(key)

#erase contents of key.key
f = open("key.key", "w")
f.write("Execute key.py")
f.close()

#encrypt or decrypt
mode = ""
while True:
    mode = input("Encrypt (y/n)? ").lower().strip()
    print(type(mode))
    print(mode)
    if mode == "y" or mode == "n":
        break

#read and delete or not
while True:
    read = input("Read result file (y/n)? ").lower().strip()
    print(type(read))
    print(read)
    if read == "y" or read == "n":
        break

#open the file to encrypt
file_name = input("Enter the file to be encrypted/decrypted: ")
with open(file_name, "rb") as f:
    data = f.read()

#encrypt
if mode == "y":
    encrypted = fernet.encrypt(data)
    #write the encrypted file
    new_file = f"{file_name}.encrypted"
    with open(new_file, "wb") as f:
        f.write(encrypted)

#decrypt
if mode == "n":
    decrypted = fernet.decrypt(data)
    #write the decrypted file
    index = file_name.index(".encrypted")
    file_name = file_name[:index]
    new_file = f"{file_name}.decrypted"
    with open(new_file, "wb") as f:
        f.write(decrypted)
    #print the decrypted message
    print(decrypted)