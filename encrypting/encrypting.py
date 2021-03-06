from cryptography.fernet import Fernet
import os


fernet = ""
#get the key from file
while True:
    try:
        keyfile = open("key.key", "rb")
        key = keyfile.read() #bytes
        keyfile.close()
        fernet = Fernet(key)
        if key:
            break
    except:
        input("Execute 'key.py' and then press enter")

#erase contents of key.key
f = open("key.key", "w")
f.write("Execute key.py")
f.close()

#encrypt or decrypt
mode = ""
while True:
    mode = input("Encrypt (y/n)? ").lower().strip()
    if mode == "y" or mode == "n":
        break

#open the file to encrypt
while True:
    try:
        file_name = input("Enter the file to be encrypted/decrypted: ")
        with open(file_name, "rb") as f:
            data = f.read()
        if f:
            break
    except:
        print("File not found")

#delete or keep the original fileaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
delete_file = ""
while True:
    delete_file = input("Delete the original file (y/n)? ").lower().strip()
    if delete_file == "y" or delete_file == "n":
        break

#encrypt
if mode == "y":
    encrypted = fernet.encrypt(data)
    #write the encrypted file

    if ".decrypted" in file_name:
        index = file_name.index(".decrypted")
        new_file = file_name[:index]
        new_file = f"{new_file}.encrypted"
    
    else:
        new_file = f"{file_name}.encrypted"

    with open(new_file, "wb") as f:
        f.write(encrypted)
    print(f"\n{new_file} has been created")

#decrypt
if mode == "n":
    while True:
        try:
            decrypted = fernet.decrypt(data)
        except:
            print("Invalid key")
            input("Execute 'key.py' using the correct password and then press enter")
        if decrypted:
            break
    while True:
        save = input("Save decrypted file (y/n)? ").lower().strip()
        if save == "y" or save == "n":
            break

    if save == "y":
        #write the decrypted file
        index = file_name.index(".encrypted")
        new_file = file_name[:index]

        new_file = f"{new_file}.decrypted"

        with open(new_file, "wb") as f:
            f.write(decrypted)
        print(f"\n{new_file} has been created")
    #else:
#print the decrypted message
    print(f"\nContent of {file_name}: \n")
    print(decrypted.decode())
    print("\n")

#delete file
if delete_file == "y":
    os.remove(file_name)
    print(f"{file_name} has been deleted")

input("Press enter to exit")