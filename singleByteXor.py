from xor import xor
import operator
from encodeAndDecode import *
from scoreFunction import scoreMsg

singleByte = list(range(0, 256))
contentDict = {}

file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")
flines = file.read().splitlines()
file.close()

def scoreMsg(msg: str) -> float:

    trimmedMsg = msg.replace(" ", "")
    msgLen = len(trimmedMsg)

    msgFrequency = {}

    for char in trimmedMsg:
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

def decoder(lines):

    for key in singleByte:
        for line in lines:
            byteContent = convertToBytes(line)
            content = xor(key, byteContent)
            
            decodedStr = ""
            for single_byte in content:
                decodedStr += chr(single_byte)
            contentDict[decodedStr] = (float(scoreMsg(decodedStr)), key)
                
    return sorted(contentDict.items(), key=operator.itemgetter(1))

def main():
    sortedList = decoder(flines)[:5]
    
    for item in sortedList:
        print("MESSAGE:\n" + item[0])
        print("SCORE: \n" + str(item[1][0]))
        print("KEY BYTE VAL: \n" + str(item[1][1]) +"\n")

if __name__ == "__main__":
        main()