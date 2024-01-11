import base64 

def base64Encode(input: str):
    inputBytes = input.encode("ascii")
    base64Bytes = base64.b64encode(inputBytes)
    base64String = base64Bytes.decode("ascii")
    return base64String

