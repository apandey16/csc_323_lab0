# def xor(key: str, value: str) -> str:
    
#     keyLen = len(key)
#     keyPtr = 0
#     retStr = ""

#     for num in value:
#         retStr += str(int(num) ^ int(key[keyPtr % keyLen]))
#         keyPtr += 1

#     return retStr

def xor(key: bytes, value: bytes) -> bytes:
    ret_bytes = bytearray()

    for byte in value:
        ret_bytes.append(byte ^ key)

    return bytes(ret_bytes)
