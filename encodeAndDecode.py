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
    return binascii.unhexlify(hexStr)

# byte_data="hey".encode("utf-16")

# print("BEFORE:",byte_data, type(byte_data))
# print()

# converted = convertToHex(byte_data)
# print("AFTER:", converted, type(converted))
# print()

# print("BACK AGAIN:", convertToBytes(converted))