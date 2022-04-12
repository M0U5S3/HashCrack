# open config.txt and convert it to a list of strings (each line)

with open("Config.txt", "r") as configtxt:

    configtxtlist = configtxt.readlines()


    #Select character set to be used

    if configtxtlist[13] == "\n":
        characterSet = (input("\n[ConfigInterpreter.py] characterSet has not been configured please enter characters to use now: "))
    else:
        characterSet = str(configtxtlist[13]).rstrip()



    #Path to rockyou (forward slashes) directory

    pathtolist = str(configtxtlist[5]).rstrip()



    #password list encoding

    if configtxtlist[9].rstrip() == "":
        listEncoding = "utf-8"
    else:
        listEncoding = configtxtlist[9].rstrip().lower()


    #Select a hashing algorithm

    if configtxtlist[1] == "SHA-256\n":
        SHA256 = True
    else:
        SHA256 = False


    if configtxtlist[1] == "SHA-1\n":
        SHA1 = True
    else:
        SHA1 = False


    if configtxtlist[1] == "MD5\n":
        MD5 = True
    else:
        MD5 = False