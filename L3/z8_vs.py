import matplotlib.pyplot as plt
import hashlib
from z8 import hyperLogLog, h_2

MAX32 = 2**32

n_vals = [n for n in range(1,10001)]

def SHA32(x):
    return (int.from_bytes(hashlib.sha512(str(x).encode()).digest(), 'big') % MAX32)/MAX32

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
    

if __name__ == "__main__":
    ratios_hll = []
    ratios_mc = []
    counter = 1
    for n in n_vals:
        print(n)
        MM = [i for i in range(counter,counter+n)]
        ratios_hll.append(hyperLogLog(MM,5,h_2)[1]/n)
        ratios_mc.append(minCount(MM,SHA32,5)/n)
        counter += n
    
    plt.scatter(n_vals, ratios_mc, s=1, label='minCount')
    plt.scatter(n_vals, ratios_hll, s=1, label='HyperLogLog')
    plt.title("minCount vs HyperLogLog")
    plt.legend()
    plt.xlabel("n")
    plt.ylabel("n_est/n")
    plt.savefig("L3/charts/z8_vs.png", dpi=300)
    plt.close()