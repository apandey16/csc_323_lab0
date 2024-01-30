import math
from xor import xor
from encodeAndDecode import base64Decode
from singleByteXor import *

file = open("Encrypted Messages/Lab0.TaskII.C.txt", "r")
lines = file.read()
file.close()

def convertToStr(input) -> str:
    retStr = ""
    for letter in input:
        retStr += chr(letter)
    return retStr

msgDecoded = base64Decode(lines)
msg = convertToStr(msgDecoded)

def keyLen(input):
    curKeyLen = None
    curScore = 25
    scoreLenDict = {}
    

    for keySize in range(2, 20):
        curStr = ""
        curStr = input[::keySize]
        
        tempScore = scoreMsg(curStr)

        if curScore > tempScore:
            curScore = tempScore
            curKeyLen = keySize
            scoreLenDict[curScore] = curKeyLen
            
    return scoreLenDict.items()

def decoded(input):
    localContentDict = {}
    singleByteLocal = list(range(0, 256))
    for key in singleByteLocal:
        contentBytes = xor(key, input)
        
        decodedStr = ""
        for single_byte in contentBytes:
            decodedStr += chr(single_byte)
        localContentDict[decodedStr] = (float(scoreMsg(decodedStr)), key)
                
    return dict(sorted(localContentDict.items(), key=operator.itemgetter(1)))

def filter(inputText):
    sortedDict = decoded(inputText)
    return sorted(sortedDict.items(), key=operator.itemgetter(1))


def decoderM(input, keySize):
    windows = []
    retWindows = []
    print()
    for i in range(0,keySize):
        windows.append(input[i::keySize])
    print(input)
    print(windows)
    print()
    
    for window in windows:
        print(window)
        sortedLst = filter(window)[:1]
        for item in sortedLst:
            print("MESSAGE:\n" + item[0])
            print("SCORE: \n" + str(item[1][0]))
            print("KEY BYTE VAL: \n" + str(item[1][1]) +"\n")
            retWindows.append(item[0])
        print("_______________________________________________________________________________________________________")
        
    return retWindows

def displayMessage(input):
    retStr = ""
    for i in range(len(input[0])):
        retStr += input[0][i]
        if i < len(input[1]):
            retStr += input[1][i] 
        if i < len(input[2]):
            retStr += input[2][i]
        if i < len(input[3]):
            retStr += input[3][i]
        if i < len(input[4]):
            retStr += input[4][i]
    return retStr

keyLenLst = list(keyLen(msg))
print("retVal: " + str(keyLenLst))

decodedWindows = decoderM(msgDecoded, keyLenLst[0][1])

print(displayMessage(decodedWindows))

