import hashlib
import sys
sys.path.insert(0, 'X:\Gabriel\Dokumenty\Studia\AA\Laby\L2\Z5')
import z5b

MAX512 = 2**512
MAX128 = 2**128
MAX32 = 2**32
MAX8 = 2**8

def SHA512(x):
    return int.from_bytes(hashlib.sha512(str(x).encode()).digest())/MAX512

def SHA128(x):
    return (int.from_bytes(hashlib.sha512(str(x).encode()).digest()) % MAX128)/MAX128

def SHA32(x):
    return (int.from_bytes(hashlib.sha512(str(x).encode()).digest()) % MAX32)/MAX32

def SHA8(x):
    return (int.from_bytes(hashlib.sha512(str(x).encode()).digest()) % MAX8)/MAX8

def MD5_128(x):
    return int.from_bytes(hashlib.md5(str(x).encode()).digest())/MAX128

def MD5_32(x):
    return (int.from_bytes(hashlib.md5(str(x).encode()).digest()) % MAX32)/MAX32

def MD5_8(x):
    return (int.from_bytes(hashlib.md5(str(x).encode()).digest()) % MAX8)/MAX8

hash_functions = [SHA512, SHA128, SHA32, SHA8, MD5_128, MD5_32, MD5_8]
k = 400
n_vals = [i for i in range(1,10001)]

if __name__ == "__main__":
    with open('Laby/L2/Z6/hash.csv', 'w') as f:
        for n in n_vals:
            print(n)
            f.write('{};'.format(n))
            for hash in hash_functions:
                MM = [i for i in range(1,n+1)]
                f.write(str(z5b.minCount(MM, hash, k)/n))
                if hash != MD5_8:
                    f.write(';')
            f.write('\n')
        f.close()
