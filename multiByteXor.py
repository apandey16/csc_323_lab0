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

def decoderM(input, keySize):
    windows = []
    for i in range(0,keySize):
        windows.append(input[i::keySize])
    # Windows are made, now need to xor each window 
    
    for window in windows:
        for key in range(1,256):
            decipheredText = xor(key, convertToBytes(window))
            print(decipheredText)
    # print(main(windows[0]))
    # for window in windows:
    #     asciiKey = {}
    #     decode = decoder(window)
    #     for item in decode:
    #         curKey = int(item[1][1])
    #         print(item)
    #         if curKey in asciiKey:
    #             asciiKey[curKey] += 1
    #         else:
    #            asciiKey[curKey] = 1 
    #     print(asciiKey)
    #     # print(decoder(window))
    #     print()
    #     print()

    
    return windows
    

print("retVal: " + str(keyLen(msg)))
(decoderM(msg, 5))