import math
from xor import xor
from encodeAndDecode import base64Decode
from singleByteXor import letterFrequency

file = open("Encrypted Messages/Lab0.TaskII.C.txt", "r")
lines = file.read()
file.close()

def convertToStr(input) -> str:
    retStr = ""
    for letter in input:
        retStr += chr(letter)
    return retStr
msg = convertToStr(base64Decode(lines))

def score(msg):
    msgLen = len(msg)

    msgFrequency = {}

    for char in msg:
        if char in msgFrequency:
            msgFrequency[char] += 1/msgLen
        else:
            msgFrequency[char] = 1/msgLen
        
    score = 0
    for char in msgFrequency:
        if char.upper() in letterFrequency:
            score += math.fabs(msgFrequency[char] - letterFrequency[char.upper()])
        else:
            score += 1
    
    return score

def keyLen(input):
    curKeyLen = None
    curScore = 25
    scoreLenDict = {}
    

    for keySize in range(2, 20):
        curStr = ""
        curStr = input[::keySize]
        print(curStr)
        print("score " + str(score(curStr)))
        print()
    
        if curScore > score(curStr):
            curScore = score(curStr)
            curKeyLen = keySize
            scoreLenDict[curScore] = curKeyLen
            
    return scoreLenDict

print("retVal: " + str(keyLen(msg)))