import hashlib
import math

n_vals = [n for n in range(1,10001)]
MAX32 = 2**32

def h_1(x):
    return "{0:032b}".format(int(hashlib.blake2s(str(x).encode(), digest_size=4).hexdigest(), base=16))

def h_2(x):
    return "{0:032b}".format(int(hashlib.sha256(str(x).encode()).hexdigest(), base=16) % MAX32)

def bblSort(M, k):
    x = M[k-1]
    i = k-2
    while M[i] > x:
        i -= 1
    M[i+2:k] = M[i+1:k-1]
    M[i+1] = x

def minCount(MM, h, k):
    M = [1] * k
    for x in MM:
        hash = h(x)
        if hash < M[k-1] and hash not in M:
            M[k-1] = hash
            bblSort(M, k)
    if M[k-1] == 1:
        return sum(1 for a in M if a != 1)
    else:
        return (k-1)/M[k-1]

def alpha(m):
    if m == 16:
        return 0.673
    if m == 32:
        return 0.697
    if m == 64:
        return 0.709
    if m >= 128:
        return 0.7213/(1 + 1.079/m)
    
def rho(w):
    for i,b in enumerate(w):
        if b == '1':
            return i + 1
        
def Void(M):
    v = 0
    for m in M:
        if m == 0:
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
        if Void(M):
            print(1)
            return m * math.log2(m/v)
        else:
            print(2)
            return E
    if E <= (1/30) * 2**32:
        print(3)
        return E
    print(4)
    return -(2**32) * math.log2(1 - E/2**32)

if __name__ == "__main__":
    with open('Laby/L3/z8.csv', 'w') as f:
        counter = 1
        for n in n_vals:
            print(n)
            MM = [i for i in range(counter,counter+n)]
            f.write(str(hyperLogLog(MM,5,h_2)/n))
            counter += n
            f.write('\n')
        f.close()
    # print(hyperLogLog([i for i in range(10000)], 5, h_2))