import zipfile
import time
encrypted_filename= "secret_file.zip"
zFile = zipfile.ZipFile(encrypted_filename, "r")

passFile = open("passwords.txt", "r")
for line in passFile.readlines():
    test_password = line.strip("\n").encode('utf-8')
    try:
        print(test_password)
        zFile.extractall(pwd=test_password)
        print("Match found")
        break
        

    except Exception as err:
        
        pass