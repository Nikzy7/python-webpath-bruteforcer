# website brute force attacker
import requests
import sys
import os

# placeholder variable declaration
inputURL = str()
wordFile = str()
wordList = list()
errorCodes = list()
statusCodeDictionary = dict()

# function to generate url from input and word
def url_creator(inputSite,word):
    return "https://" + inputSite + "/" + word

# possible multithread function
def bruteForceAction():
    pass

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
    for word in wordList:
        urls.append(url_creator(inputURL,word))

    # test code
    # print(urls)


# writing final output
def outputGeneration():
    pass

# process check for inputProcessing()
# def unitTest():
#     print(errorCodes)
#     print(wordFile)
#     print(inputURL)
#     print(sys.argv)

if __name__ == "__main__":
    inputProcessing()
    # unitTest()
    actionHandler()
    outputGeneration()