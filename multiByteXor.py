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

msg = convertToStr(base64Decode(lines))

def keyLen(input):
    curKeyLen = None
    curScore = 25
    scoreLenDict = {}
    

    for keySize in range(2, 20):
        curStr = ""
        curStr = input[::keySize]
    
        if curScore > scoreMsg(curStr):
            curScore = scoreMsg(curStr)
            curKeyLen = keySize
            scoreLenDict[curScore] = curKeyLen
            
    return scoreLenDict

def decoded(input):
    localContentDict = {}
    singleByteLocal = list(range(0, 256))
    for key in singleByteLocal:
        content = xor(key, input)
        
        decodedStr = ""
        for single_byte in content:
            decodedStr += chr(single_byte)
        localContentDict[decodedStr] = (float(scoreMsg(decodedStr)), key)
                
    return dict(sorted(localContentDict.items(), key=operator.itemgetter(1)))

def filter(inputText):
    sortedDict = {}
    sortedDict = decoded(inputText)
    return sorted(sortedDict.items(), key=operator.itemgetter(1))


def decoderM(input, keySize):
    windows = []
    for i in range(0,keySize):
        windows.append(input[i::keySize])
    
    for window in windows:
        print(window)
        sortedLst = filter(window.encode('utf-8'))[:1]
        for item in sortedLst:
            print("MESSAGE:\n" + item[0])
            print("SCORE: \n" + str(item[1][0]))
            print("KEY BYTE VAL: \n" + str(item[1][1]) +"\n")
    
        print("_______________________________________________________________________________________________________")
    
    return windows
    

print("retVal: " + str(keyLen(msg)))
decoderM(msg, 5)