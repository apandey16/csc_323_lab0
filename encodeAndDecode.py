import base64 

def base64Encode(input: str) -> str:
    stringBytes = input.encode("ascii")
    encodedBytes = base64.b64encode(stringBytes)
    return encodedBytes.decode("ascii")

def base64Decode(input: str) -> str:
    encodedBytes = input.encode("ascii")
    stringBytes = base64.b64decode(encodedBytes)
    return stringBytes.decode("ascii")
