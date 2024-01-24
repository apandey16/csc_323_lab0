from xor import xor
import operator
from encodeAndDecode import *

letterFrequency = {'E': 0.12003601080324099, 'T': 0.09102730819245775, 'A': 0.08122436731019306, 'O': 0.07682304691407423, 'I': 0.0731219365809743, 'N': 0.06952085625687708, 'S': 0.06281884565369612, 'R': 0.06021806541962589, 'H': 0.05921776532959889, 'D': 0.04321296388916676, 'L': 0.03981194358307493, 'U': 0.028808642592777836, 'C': 0.027108132439731925, 'M': 0.026107832349704915, 'F': 0.02300690207062119, 'Y': 0.021106331899569872, 'W': 0.02090627188156447, 'G': 0.020306091827548264, 'P': 0.01820546163849155, 'B': 0.014904471341402423, 'V': 0.011103330999299792, 'K': 0.006902070621186356, 'X': 0.0017005101530459142, 'Q': 0.0011003300990297092, 'J': 0.0010003000900270084, 'Z': 0.0007002100630189059}

def scoreMsg(msg: str) -> int:

    trimmedMsg = msg.replace(" ", "")

    msgFrequency = {}

    for char in trimmedMsg:
        if char in msgFrequency:
            msgFrequency[char] += 1/len(trimmedMsg)
        else:
            msgFrequency[char] = 1/len(trimmedMsg)
        
    sum = 0
    for char in msgFrequency:
        if char.upper() in letterFrequency:
            sum += abs(msgFrequency[char] - letterFrequency[char.upper()])
    
    return sum

singleByte = list(range(0, 256))
singleByte = [0]
file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")

lines = file.read().splitlines()

contentDict = {}

# file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")
# byteMSG = convertToBytes(file.readline())
# potentialMSG = xor(bytes([1]), byteMSG)
# byteStr = ""
# for single_byte in potentialMSG:
#     byteStr += chr(single_byte)
# print(byteStr)

# file.close()

def decode(text):
    
    for key in singleByte:
        decodedVal = xor(bytes([key]), convertToBytes(text))
        print(decodedVal)

        decodedScore = scoreMsg(decodedVal.decode("ascii", 'ignore'))

        if text in contentDict:
            scoreKeyPair = contentDict[decodedVal]
            if scoreKeyPair[1] > decodedScore:
                contentDict.update({text :[decodedVal, decodedScore, key]})
        else:
            contentDict.update({text :[decodedVal, decodedScore, key]})

# print(lines[0])
decode(lines[0])
print(contentDict)

# for key in singleByte:
    
#     while True:

#         content = xor(bytes([key]), convertToBytes(file.readline()))
#         if not content:
#             break
        
#         decodedStr = ""
#         for single_byte in content:
#             decodedStr += chr(single_byte)
#         contentDict[content] = scoreMsg(decodedStr)
            
    

# sorted_dict = dict(sorted(contentDict.items(), key=operator.itemgetter(1)))

# x = 0
# for item in sorted_dict:
#     if x >= 100:
#         break
#     if x >= 0:
#         print("SCORE:", sorted_dict[item])
#         print("MESSAGE:", item)
#         print()
#     x += 1

file.close()