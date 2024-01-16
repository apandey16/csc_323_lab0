def xor(key: str, value: str) -> str:
    
    keyLen = len(key)
    keyPtr = 0
    retStr = ""

    for num in value:
        retStr += str(int(num) ^ int(key[keyPtr % keyLen]))
        keyPtr += 1

    return retStr
