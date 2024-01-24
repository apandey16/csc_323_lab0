from xor import xor
import operator
from encodeAndDecode import *

encryptionType = "utf-8"

letterFrequency = {'E': 0.12003601080324099, 'T': 0.09102730819245775, 'A': 0.08122436731019306, 'O': 0.07682304691407423, 'I': 0.0731219365809743, 'N': 0.06952085625687708, 'S': 0.06281884565369612, 'R': 0.06021806541962589, 'H': 0.05921776532959889, 'D': 0.04321296388916676, 'L': 0.03981194358307493, 'U': 0.028808642592777836, 'C': 0.027108132439731925, 'M': 0.026107832349704915, 'F': 0.02300690207062119, 'Y': 0.021106331899569872, 'W': 0.02090627188156447, 'G': 0.020306091827548264, 'P': 0.01820546163849155, 'B': 0.014904471341402423, 'V': 0.011103330999299792, 'K': 0.006902070621186356, 'X': 0.0017005101530459142, 'Q': 0.0011003300990297092, 'J': 0.0010003000900270084, 'Z': 0.0007002100630189059}

def scoreMsg(msg: str) -> int:

    msgLen = len(msg)
    msgFrequency = {}

    for char in msg:
        if char in msgFrequency:
            msgFrequency[char] += 1/msgLen
        else:
            msgFrequency[char] = 1/msgLen
        
    sum = 0
    for char in msgFrequency:
        if char.upper() in letterFrequency:
            sum += abs(msgFrequency[char] - letterFrequency[char.upper()])
        else: 
            sum += msgFrequency[char] 
    
    return sum

singleByte = list(range(0, 256))

file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")

lines = file.read().splitlines()

contentDict = {}

def decode(text):
    
    for key in singleByte:
        decodedVal = xor(bytes([key]), convertToBytes(text))

        decodedScore = scoreMsg(decodedVal.decode(encryptionType, 'replace'))

        if text in contentDict:
            scoreKeyPair = contentDict[text]
            if scoreKeyPair[1] > decodedScore:
                contentDict.update({text :[decodedVal, decodedScore, key]})
        else:
            contentDict.update({text :[decodedVal, decodedScore, key]})

def parseDecode(updatedDict):
    retLst = []

    for key, val in updatedDict.items():
        if val[1] < 0.5:
            retLst.append([key,val])
            print(val[0].decode(encryptionType, "replace") + "\n")
    return(retLst)

for line in lines:
    decode(line)

parseDecode(contentDict)

file.close()