import requests
import json
from colorama import Fore
import time


class pp():
    def success(input):
        print(Fore.GREEN + input + Fore.RESET)

    def failure(input):
        print(Fore.RED + input + Fore.RESET)

    def question(input):
        print(Fore.YELLOW + input + Fore.RESET)


def selectWordlistAndURL():
    pp.question("What wordlist do you want to use?")
    with open("wordlists.json", "r") as file:
        data = json.load(file)

    for i in range(0, len(data["wordlists"])):
            print(str(i) + " - " + data["wordlists"][i]["name"])

    selection = input()
    wordlistURL = data["wordlists"][int(selection)]["url"]
    return wordlistURL


def getWordlistContent(url):
    try:
        wordListReq = requests.get(url)
        if wordListReq.status_code == 200:
            pp.success("Response code: " + str(wordListReq.status_code) + " Wordlist successfully retrieved...")
            return wordListReq.text
        else:
            pp.failure("Response code: " + str(wordListReq.status_code) + " Wordlist retrieval failed....")
      
      
    except:
        print("Critical failure, exiting")
        exit()


def main():
    pp.question("What rate limit would you like?")
    try:
        rateLimit = int(input())
    except:
        pp.failure("Rate limit must be an integer, exiting.")
        exit()
    pp.question("What URL do you want to target? (i.e https://google.com)")
    target = input() + "/"
    wordlistURL = selectWordlistAndURL()
    print("Retrieving wordlist from: " + wordlistURL)
    time.sleep(2)
    wordlist = getWordlistContent(wordlistURL).split('\n')
    
    for i in range(0, len(wordlist)):
        if "#" in wordlist[i]:
            print("Wordlist item: " + wordlist[i] + " is a comment, skipping...")
            continue
        else:
            print("Sending request to: " + target + wordlist[i])
            request = requests.get(target + wordlist[i])
            
            if request.status_code == 200:
                pp.success("--> Request to: " + target + wordlist[i] + " (Status Code: " + str(request.status_code) + ")" )
                time.sleep(rateLimit)
            else:
                pp.failure("--> Request to: " + target + wordlist[i] + " (Status Code: " + str(request.status_code) + ")" )
                time.sleep(rateLimit)

if __name__ == '__main__':
    main()