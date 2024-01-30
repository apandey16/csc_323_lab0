# https://www.youtube.com/watch?v=QQhJOCfdRg4&ab_channel=LearningPython
# https://www.youtube.com/watch?v=LaWp_Kq0cKs&ab_channel=Theoretically
import math
#need to change scoring function as the right ones aren't being passed
def scoreMsg(msg: str) -> float:

    englishFrequency = {'E': 0.12003601080324099, 'T': 0.09102730819245775, 'A': 0.08122436731019306, 'O': 0.07682304691407423, 'I': 0.0731219365809743, 'N': 0.06952085625687708, 'S': 0.06281884565369612, 'R': 0.06021806541962589, 'H': 0.05921776532959889, 'D': 0.04321296388916676, 'L': 0.03981194358307493, 'U': 0.028808642592777836, 'C': 0.027108132439731925, 'M': 0.026107832349704915, 'F': 0.02300690207062119, 'Y': 0.021106331899569872, 'W': 0.02090627188156447, 'G': 0.020306091827548264, 'P': 0.01820546163849155, 'B': 0.014904471341402423, 'V': 0.011103330999299792, 'K': 0.006902070621186356, 'X': 0.0017005101530459142, 'Q': 0.0011003300990297092, 'J': 0.0010003000900270084, 'Z': 0.0007002100630189059}

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
        if not char.isalpha():
            score += 1
        elif char.upper() in englishFrequency:
            score += math.fabs(msgFrequency[char] - englishFrequency[char.upper()])
    
    return score

def scoreMsgMult(windowFrequency: list, length: int) -> float:
    englishFrequency = [('A', 0.08122436731019306),('B', 0.014904471341402423),('C', 0.027108132439731925),('D', 0.04321296388916676),('E', 0.12003601080324099),('F', 0.02300690207062119),
    ('G', 0.020306091827548264),('H', 0.05921776532959889),('I', 0.0731219365809743),('J', 0.0010003000900270084),('K', 0.006902070621186356),('L', 0.03981194358307493),
    ('M', 0.026107832349704915),('N', 0.06952085625687708),('O', 0.07682304691407423),('P', 0.01820546163849155),('Q', 0.0011003300990297092),('R', 0.06021806541962589),
    ('S', 0.06281884565369612),('T', 0.09102730819245775),('U', 0.028808642592777836),('V', 0.011103330999299792),
    ('W', 0.02090627188156447),('X', 0.0017005101530459142),('Y', 0.021106331899569872),('Z', 0.0007002100630189059)]

    maxScore = 0 
    maxShift = 0

    for count in range(length):
        score = 0
        for i, tupley in enumerate(windowFrequency):
            # here I am always comparing the same char together; need to be able to shift and compare various ones
            # windowFrequency must change but engish should stay the sam eorder
            score += windowFrequency[i][1] * englishFrequency[i][1]
        
        if score > maxScore:
            maxScore = score
            maxShift = count

        windowFrequency = windowFrequency[1::] + [windowFrequency[0]]
    
    return maxShift

def shiftString(inputStr: str):
    result = '0' + inputStr[:-1]
    return result

def countCoincidences(coincidences: list, msg: str, copy: str) -> list:
    count = 0

    for i, char in enumerate(msg):
        if (copy[i] == char):
            count += 1

    coincidences.append(count)
    return coincidences

def keyLength(msg: str) -> list:
    coincidences = []
    x = 0
    copy = msg

    while x < (len(msg)-10):
        copy = shiftString(copy)
        coincidences = countCoincidences(coincidences, msg, copy)
        x += 1

    return coincidences

def vigenereDecrypt(key: str, ciphertext: str) -> str:
    # # Using Vigenere grid, decrypt the sublist (msg) using the subkey
    decryptedMsg = ""
    key = key.upper()
    key_len = len(key)
    
    for i, char in enumerate(ciphertext):
        row = ord(key[i % key_len]) - ord('A')
        col = ord(char.upper()) - ord('A')
        decryptedMsg += chr((col - row) % 26 + ord('A'))

    return decryptedMsg

def findSubKey(subList: list) -> chr:
    msgLen = len(subList)
    msgFrequency = [ ('A', 0), ('B', 0), ('C', 0), ('D', 0), ('E', 0), ('F', 0), ('G', 0),
    ('H', 0), ('I', 0), ('J', 0), ('K', 0), ('L', 0), ('M', 0), ('N', 0),
    ('O', 0), ('P', 0), ('Q', 0), ('R', 0), ('S', 0), ('T', 0), ('U', 0),
    ('V', 0), ('W', 0), ('X', 0), ('Y', 0), ('Z', 0)]

    for char in subList:
        index = ord(char) - ord('A')
        msgFrequency[index] = (char, msgFrequency[index][1] + 1/msgLen)

    return chr(scoreMsgMult(msgFrequency, msgLen) + ord("A"))

def findKey(keyLength: int, msg: str) -> str:
    key = ''

    for i in range(keyLength):
        x = i
        subList = []
        while x < len(msg):
            subList.append(msg[x])
            x += keyLength
            
        key += findSubKey(subList)

    return key

file = open("TaskD/Lab0.TaskII.D.txt", "r")
encryptedMSG = file.readline()
encryptedMSG = encryptedMSG.strip("\n")
file.close()

listy = keyLength(encryptedMSG)
key = findKey(14, encryptedMSG)
print("Key: " + key)
print()
print("Decoded Value: \n" + vigenereDecrypt(key.upper(), encryptedMSG))

