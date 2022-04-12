import hashlib
import webbrowser
from Data.ConfigInterpreter import SHA1, SHA256, MD5, configtxtlist, pathtolist, listEncoding
import os.path
from colorama import Fore

def fsha(plain_str, shatype):

    if str(shatype) == "SHA-1":
        hashed_str = hashlib.sha1(plain_str.encode(listEncoding)).hexdigest()
        return hashed_str

    elif str(shatype) == "SHA-256":
        hashed_str = hashlib.sha256(plain_str.encode(listEncoding)).hexdigest()
        return hashed_str

    elif str(shatype) == "MD5":
        hashed_str = hashlib.md5(plain_str.encode(listEncoding)).hexdigest()
        return hashed_str

def maxCyclesTaken(maxPasswordLength, characterSet):
    return len(characterSet) ** int(maxPasswordLength) - 1



def isAllInCharacterSet(inp, characterSet):
    iCount = -1
    for y in inp:
        iCount += 1
        if (y in characterSet) == False:
            print("\nInvalid syntax: Character(s) is not included in characterSet (index: " + str(iCount) + ")")
            return False
    return True

def configInfo(setting):

    if (SHA1 == True) & (setting == "hashType"):
        return "SHA-1"

    elif(SHA256 == True) & (setting == "hashType"):
        return "SHA-256"

    elif (MD5 == True) & (setting == "hashType"):
        return "MD5"

    else:
        print("\nError: No hashing algorithm selected")
        quit()

def isConfigSet(setting):

    print(Fore.RED + "\nChecking " + setting + " config...")

    if setting == "hash":
        if configtxtlist[1] in ["SHA-1\n", "SHA-256\n", "MD5\n"]:
            print("Selected hashing algorithm: " + configtxtlist[1].rstrip() + Fore.BLUE)
            return True
        else:
            print("No valid hashing algorithm has been selected")
            quit()

    if setting == "pathtolist":

        if pathtolist == "":
            print("No path for the password list has been configured" + Fore.BLUE)
            quit()
        else:
            passwordlistexists = os.path.exists(pathtolist)

            if (passwordlistexists == False):
                buf = input("Password list not found or file path entered in config is incorrect.\nIf you haven't installed one download rockyou.txt (y), otherwise press enter to quit.")
                if buf == "y" or buf == "Y":
                    print("\nDownloading rockyou.txt (133MB)")
                    webbrowser.open("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", new=1)
                quit()
        print("Path to list: " + pathtolist + Fore.BLUE)
        return True

    if setting == "listencoding":

        if listEncoding == "":
            print("Error: No encoding for password list has been set")
            quit()

        else:
            print("List encoding: " + listEncoding + Fore.BLUE)
            return True