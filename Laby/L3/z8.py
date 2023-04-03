import hashlib
import math

n_vals = [n for n in range(1,10001)]
b_vals = [b for b in range(4,17)]
hashes = ['blake', 'sha', 'md5']
MAX32 = 2**32

def h_1(x):
    return "{0:032b}".format(int(hashlib.blake2s(str(x).encode(), digest_size=4).hexdigest(), base=16))

def h_2(x):
    return "{0:032b}".format(int(hashlib.sha256(str(x).encode()).hexdigest(), base=16) % MAX32)

def h_3(x):
    return "{0:032b}".format(int(hashlib.md5(str(x).encode()).hexdigest(), base=16) % MAX32)

hash_dict = {'blake' : h_1, 'sha' : h_2, 'md5' : h_3}

def alpha(m):
    if m == 16:
        return 0.673
    if m == 32:
        return 0.697
    if m == 64:
        return 0.709
    if m >= 128:
        return 0.7213/(1 + (1.079/m))
    
def rho(w):
    for i,b in enumerate(w):
        if b == '1':
            return i + 1
    return len(w) + 1
        
def Void(M):
    v = 0
    for y in M:
        if y == 0:
            v += 1
    return v

def hyperLogLog(MM,b,h):
    m = 2**b
    M = [0] * m

    for v in MM:
        x = h(v)
        j = x[:b]
        w = x[b:]
        jj = int(j, base=2)
        M[jj] = max(M[jj], rho(w))

    sum = 0
    for y in M:
        sum += 2**(-y)

    E = alpha(m) * m**2 * (1/sum)

    if E <= (5/2) * m:
        V = Void(M)
        if V != 0:
            return 1, m * math.log(m/V)
        else:
            return 1, E
    if E <= 2**32 / 30:
        return 2, E
    return 3, -(2**32) * math.log(1 - E/2**32)

if __name__ == "__main__":
    for hash in ['md5']:
        with open('Laby/L3/z8_{}.csv'.format(hash), 'w') as f:
            counter = 1
            for n in n_vals:
                print(n)
                for b in b_vals:
                    MM = [i for i in range(counter,counter+n)]
                    res = hyperLogLog(MM,b,hash_dict[hash])
                    f.write("{};{}".format(str(res[0]), str(res[1]/n)))
                    if b != 16:
                        f.write(';')
                counter += n
                f.write('\n')
            f.close()