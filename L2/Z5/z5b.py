import hashlib

MAX = 2**512
n_vals = [n for n in range(1,10001)]
k_vals = [2,3,10,100,400]

def hash(x):
    return int.from_bytes(hashlib.sha512(str(x).encode()).digest())/MAX

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
    with open('L2/Z5/k.csv', 'w') as f:
        counter = 1
        for n in n_vals:
            print(n)
            for k in k_vals:
                MM = [i for i in range(counter,counter+n)]
                f.write(str(minCount(MM, hash, k)/n))
                if k != 400:
                    f.write(';')
            counter += n
            f.write('\n')
        f.close()