from cryptography.fernet import Fernet
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

#encrypt
if mode == "y":
    encrypted = fernet.encrypt(data)
    #write the encrypted file
    new_file = f"{file_name}.encrypted"
    with open(new_file, "wb") as f:
        f.write(encrypted)
    print("A encrypted file has been created")
    input("Press enter to exit")

#decrypt
if mode == "n":
    while True:
        try:
            decrypted = fernet.decrypt(data)
        except:
            print("Invalid key")
            input("Execute 'key.py' using the correct password and then press enter")
    while True:
        save = input("Save decrypted file (y/n)? ").lower().strip()
        if save == "y" or save == "n":
            break

    if save == "y":
        #write the decrypted file
        index = file_name.index(".encrypted")
        file_name = file_name[:index]

        new_file = f"{file_name}.decrypted"

        with open(new_file, "wb") as f:
            f.write(decrypted)
    else:
    #print the decrypted message
        print(f"Content of {file_name}: \n")
        print(decrypted.decode())
        input("\nPress enter to exit")