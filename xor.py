# def xor(key: str, value: str) -> str:
    
#     keyLen = len(key)
#     keyPtr = 0
#     retStr = ""

#     for num in value:
#         retStr += str(int(num) ^ int(key[keyPtr % keyLen]))
#         keyPtr += 1

#     return retStr

def xor(key: bytes, value: bytes) -> bytes:
    key_len = len(bytearray(key))

    key_ptr = 0
    ret_bytes = bytearray()

    for byte in value:
        ret_bytes.append(byte ^ key)
        key_ptr += 1

    return bytes(ret_bytes)
