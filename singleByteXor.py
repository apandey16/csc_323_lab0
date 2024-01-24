from xor import xor
import operator
from encodeAndDecode import *
import math

letterFrequency = {'E': 0.12003601080324099, 'T': 0.09102730819245775, 'A': 0.08122436731019306, 'O': 0.07682304691407423, 'I': 0.0731219365809743, 'N': 0.06952085625687708, 'S': 0.06281884565369612, 'R': 0.06021806541962589, 'H': 0.05921776532959889, 'D': 0.04321296388916676, 'L': 0.03981194358307493, 'U': 0.028808642592777836, 'C': 0.027108132439731925, 'M': 0.026107832349704915, 'F': 0.02300690207062119, 'Y': 0.021106331899569872, 'W': 0.02090627188156447, 'G': 0.020306091827548264, 'P': 0.01820546163849155, 'B': 0.014904471341402423, 'V': 0.011103330999299792, 'K': 0.006902070621186356, 'X': 0.0017005101530459142, 'Q': 0.0011003300990297092, 'J': 0.0010003000900270084, 'Z': 0.0007002100630189059}

def scoreMsg(msg: str) -> float:

    trimmedMsg = msg.replace(" ", "")

    msgFrequency = {}

    for char in trimmedMsg:
        if char in msgFrequency:
            msgFrequency[char] += 1/len(trimmedMsg)
        else:
            msgFrequency[char] = 1/len(trimmedMsg)
        
    score = 0
    for char in msgFrequency:
        if not char.isalpha():
            score += 100
        elif char.upper() in letterFrequency:
            score += math.fabs(msgFrequency[char] - letterFrequency[char.upper()])
    
    return score

singleByte = list(range(0, 256))
contentDict = {}

file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")
lines = file.read().splitlines()
file.close()

for key in singleByte:
    for line in lines:
        byteContent = convertToBytes(line)
        content = xor(bytes([key]), byteContent)

        if not content:
            break
        
        decodedStr = ""
        for single_byte in content:
            decodedStr += chr(single_byte)
        contentDict[decodedStr] = float(scoreMsg(decodedStr))
            
sorted_dict = dict(sorted(contentDict.items(), key=operator.itemgetter(1)))

x = 0
count = 0
for item in sorted_dict:
    if sorted_dict[item] == 0:
        count+=1
        continue
    # print(item, sorted_dict[item])
    if x >= 20:
        break
    print("SCORE:", sorted_dict[item])
    print("MESSAGE:", item)
    print()
    x += 1

print("COUNT", count)

