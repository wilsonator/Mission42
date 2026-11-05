#this is a demonstration of credential stealing via Google Chrome on Windows and Linux

import sys
import os



def determinePath():
    if sys.platform == 'nt':
        path = os.environ["USERPROFILE"] + "\\AppData\\Local\\Google\\Chrome\\User Data\\Local State"
        return path
    
    elif sys.platform == 'darwin':
        path = "~/Library/Application Support/Google/Chrome/Default/"
        return path

    elif sys.platform == 'linux':
        path = "~/.config/google-chrome/Default/Login Data"
        return path


def main():
    path = determinePath()
    print(path)

if __name__ == '__main__':
    main()
