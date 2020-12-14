import threading
import requests
import sys
import os
import time

# placeholder variable declaration
inputURL = str()
wordFile = str()
wordList = list()
errorCodes = list()
statusCodeDictionary = dict()

allThreads = []

# function to generate url from input and word
def url_creator(inputSite,word):
    return "https://" + inputSite + "/" + word

# possible multithread function
def bruteForceAction(url):
    global statusCodeDictionary
    try:
        response = requests.get(url)
        statusCodeDictionary[url] = int(response.status_code)
    except:
        print("URL error for : " + url)
        statusCodeDictionary[url] = 404


# processing and filling variables
def inputProcessing():
    try:
        global inputURL
        global wordFile
        global errorCodes
        global wordList

        inputURL = sys.argv[1]  
        wordFile = sys.argv[2]
        
        for x in range(3,len(sys.argv)):
            errorCodes.append(int(sys.argv[x]))

        if not(os.path.isfile(wordFile)):
            raise Exception("The word file does not exist !") 

        wordList = open(wordFile,'r').readlines()

        for x in range(len(wordList)):
            wordList[x] = wordList[x].strip()

    except IndexError:
        print("Command Line Arguments have not been properly provided ! Please try again.")
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()

# handling main action
def actionHandler():
    global wordList
    global inputURL
    urls = []
    global statusCodeDictionary
    global allThreads

    for word in wordList:
        urls.append(url_creator(inputURL,word))

    for url in urls:
        allThreads.append(threading.Thread(target=bruteForceAction,args=(url,)))
        # statusCodeDictionary[url] = bruteForceAction(url)
    
    for x in range(len(allThreads)):
        allThreads[x].start()

# writing final output
def outputGeneration():
    global statusCodeDictionary
    global errorCodes
    global allThreads

    for x in range(len(allThreads)):
        allThreads[x].join()

    file = open('output.txt','w')

    print("Printing all results, but writing only required ones !")

    for key,value in statusCodeDictionary.items():
        print(key + " [Status code " + str(value) + "]")
        if value in errorCodes:
            to_write = key + " [Status code " + str(value) + "]"
            file.write(to_write)

    file.close()

if __name__ == "__main__":
    start_time = time.time()
    inputProcessing()
    actionHandler()
    outputGeneration()
    print("--- %s seconds ---" % (time.time() - start_time))