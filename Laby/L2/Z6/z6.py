import hashlib

MAX512 = 2**512


def hashA512(x):
    return int.from_bytes(hashlib.sha512(str(x).encode()).digest())/MAX