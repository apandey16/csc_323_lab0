from xor import xor
import operator
from encodeAndDecode import *
from scoreFunction import scoreMsg

singleByte = list(range(0, 256))
contentDict = {}

file = open("Encrypted Messages/Lab0.TaskII.B.txt", "r")
lines = file.read().splitlines()
file.close()

def main():
    for key in singleByte:
        for line in lines:
            byteContent = convertToBytes(line)
            content = xor(bytes([key]), byteContent)
            
            decodedStr = ""
            for single_byte in content:
                decodedStr += chr(single_byte)
            contentDict[decodedStr] = float(scoreMsg(decodedStr))
                
    sorted_dict = dict(sorted(contentDict.items(), key=operator.itemgetter(1)))

    x = 0
    for item in sorted_dict:
        if x < 5:
            print("SCORE:", sorted_dict[item])
            print("MESSAGE:", item)
            print()
            x += 1
        else:
            break

main()