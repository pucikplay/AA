from z9_a_1 import nakamoto,grundspan
import matplotlib.pyplot as plt
import numpy as np

p_vals = [0.001,0.01,0.1]
q_vals = [q for q in np.arange(0.001,0.44,0.001)]

def find_fit(p, q, p_func):
    n = 1
    while p_func(n, q) >= p:
        n += 1
    return n

if __name__ == "__main__":
    for p in p_vals:
        n_nakamoto = []
        n_grundspan = []
        for q in q_vals:
            n_nakamoto.append(find_fit(p,q,nakamoto))
            n_grundspan.append(find_fit(p,q,grundspan))
        plt.scatter(q_vals, n_nakamoto, label='nakamoto', s=5)
        plt.scatter(q_vals, n_grundspan, label='grundspan', s=5)
        plt.xlabel('q')
        plt.ylabel('n')
        plt.title('p={}'.format(p))
        plt.legend()
        plt.savefig('Laby/L4/charts/p={}.png'.format(p), dpi=300)
        plt.close()
        
