import math
import scipy.special as scp
import matplotlib.pyplot as plt
import numpy as np

n_vals = [1,3,6,12,24,48]
q_vals = [q for q in np.arange(0.001,0.5,0.001)]

def fact(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x

def nakamoto(n, q):
    p = 1 - q
    l = n * (q / p)
    sum = 0
    for k in range(n):
        sum += (math.e**(-l) * ((l**k)) / fact(k) * (1 - (q/p)**(n-k)))
    return 1 - sum

def grundspan(n, q):
    p = 1 - q
    sum = 0
    for k in range(n):
        sum += (p**n * q**k - q**n * p**k) * scp.comb(k + n - 1, k)
    return 1 - sum

if __name__ == "__main__":
    for n in n_vals:
        p_nakamoto = []
        p_grundspan = []
        for q in q_vals:
            p_nakamoto.append(nakamoto(n,q))
            p_grundspan.append(grundspan(n,q))
        plt.scatter(q_vals, p_nakamoto, label='nakamoto', s=5)
        plt.scatter(q_vals, p_grundspan, label='grundspan', s=5)
        plt.xlabel('q')
        plt.ylabel('p_nq')
        plt.title('n={}'.format(n))
        plt.legend()
        plt.savefig('L4/charts/n={}.png'.format(n), dpi=300)
        plt.close()