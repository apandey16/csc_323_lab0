import base64 
import binascii

def base64Encode(input: str) -> str:
    stringBytes = input.encode("ascii")
    encodedBytes = base64.b64encode(stringBytes)
    return encodedBytes.decode("ascii")

def base64Decode(input: str) -> str:
    encodedBytes = input.encode("ascii")
    stringBytes = base64.b64decode(encodedBytes)
    return stringBytes.decode("ascii")

def convertToHex(binary: bytes) -> str:
    return str(binary.hex())

def convertToBytes(hexStr: str) -> bytes:
    hexStr = ''.join(c for c in hexStr if c in '0123456789ABCDEFabcdef')

    if len(hexStr) % 2 != 0:
        hexStr = '0' + hexStr
    return binascii.unhexlify(hexStr)
