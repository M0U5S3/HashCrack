from colorama import Fore, init

from Data.title import printTitle
import itertools
import hashlib
from Data.Functions import fsha, maxCyclesTaken, isAllInCharacterSet, configInfo, isConfigSet
import xerox
from Data.ConfigInterpreter import SHA1, SHA256, MD5, pathtolist, characterSet, listEncoding

init()

printTitle()

isConfigSet("hash")

hexCharacterSet = "abcdefghijklmnopqrstuvwxyz0123456789"
numbers = "0123456789"
hashed_string = ""

while True:
    crackorhash = input("\n\n\n\nWelcome to hashcrack. Please choose a mode -c / -h  / -l / -q (crack / hash / list crack / quit) ")

    if crackorhash == "-q":
        quit()

    if crackorhash == "-l":

        isConfigSet("pathtolist")
        isConfigSet("listencoding")

        while True:
            hashAns = input("\n\nWhat is your " + configInfo("hashType") + " hash to crack? ")
            if (isAllInCharacterSet(hashAns, hexCharacterSet) == True):
                break

        if hashAns == "":
            print(Fore.RED + "Error: Please enter a hash" + Fore.BLUE)
            continue

        with open(pathtolist, "r", encoding=listEncoding) as f:


            print("\nTask started...")

            try:

                if (SHA1 == True):
                    for line in f:
                        line.rstrip()
                        hashed_string = hashlib.sha1(line.encode(listEncoding)).hexdigest()
                        if hashed_string == hashAns:
                            print(Fore.YELLOW + "\n\nCompiled cracked password: " + line + Fore.BLUE)
                            break



                elif (SHA256 == True):
                    for line in f:
                        line = line.rstrip()
                        hashed_string = hashlib.sha256(line.encode(listEncoding)).hexdigest()
                        if hashed_string == hashAns:
                            print(Fore.YELLOW + "\n\nCompiled cracked password: " + line + Fore.BLUE)
                            break



                elif (MD5 == True):
                    for line in f:
                        line = line.rstrip()
                        hashed_string = hashlib.md5(line.encode(listEncoding)).hexdigest()
                        if hashed_string == hashAns:
                            print(Fore.YELLOW + "\n\nCompiled cracked password: " + line + Fore.BLUE)
                            break


                if hashed_string != hashAns:
                    print(Fore.RED + "\nNot on list" + Fore.BLUE)

            except UnicodeDecodeError as error:
                print("\n\n" + Fore.RED + + str(error) + ". You are probably using the wrong codec\n try some of the suggested codecs in config.txt" + Fore.BLUE)

            continue

    if crackorhash == "-h":

        userreq = str(input("\n\nWhat do you want to hash? (" + configInfo("hashType") + ") "))

        if userreq == "":
            print(Fore.RED + "Error: Please enter an input" + Fore.BLUE)
            continue

        userreqhash = fsha(userreq, configInfo("hashType"))

        print("\n" + Fore.YELLOW + userreqhash)
        xerox.copy(userreqhash)
        input("Copied to clipboard. Press enter to continue." + Fore.BLUE)
        continue

    elif crackorhash == "-c":

        while True:
            maxPassLength = str(input("\n\nWhat is the max length the password can be? "))
            if (isAllInCharacterSet(maxPassLength, numbers) == True):
                break


        while True:
            hashAns = input("\n\nWhat is your " + configInfo("hashType") + " hash to crack? ")
            if (isAllInCharacterSet(hashAns, hexCharacterSet) == True):
                break

        input("This will take a maximum " + str(maxCyclesTaken(maxPassLength, characterSet)) + " cycles. Press enter to begin task.")
        print(Fore.MAGENTA + "\nTask started..." + Fore.BLUE)

        if (SHA1 == True):
            for i in itertools.product(characterSet, repeat=int(maxPassLength)):
                plainStr = list(i)
                plainStr = ''.join(map(str, plainStr))
                hashed_string = hashlib.sha1(plainStr.encode(listEncoding)).hexdigest()
                if hashed_string == hashAns:
                    print(Fore.YELLOW + "\n\nCompiled cracked password: " + plainStr + Fore.RED)
                    break
            continue

        elif (SHA256 == True):
            for i in itertools.product(characterSet, repeat=int(maxPassLength)):
                plainStr = ''.join(map(str, list(i)))
                hashed_string = hashlib.sha256(plainStr.encode(listEncoding)).hexdigest()
                if hashed_string == hashAns:
                    print(Fore.YELLOW + "\n\nCompiled cracked password: " + plainStr + Fore.RED)
                    break
            continue

        elif (MD5 == True):
            for i in itertools.product(characterSet, repeat=int(maxPassLength)):
                plainStr = ''.join(map(str, list(i)))
                hashed_string = hashlib.md5(plainStr.encode(listEncoding)).hexdigest()
                if hashed_string == hashAns:
                    print(Fore.YELLOW + "\n\nCompiled cracked password: " + plainStr + Fore.RED)
                    break
            continue

        else:
            print(Fore.RED + "Error: No hash has been set in Config" + Fore.BLUE)
            quit()
    else:
        print(Fore.RED + "Invalid syntax" + Fore.BLUE)