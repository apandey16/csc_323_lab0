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

print("retVal: " + str(keyLen(msg)))

