import random
import matplotlib.pyplot as plt
import math

no_tests = 50
u = 1000
n_values = [2, u//2, u]
histogram = {2:{}, u//2:{}, u:{}}

for n in n_values:
    print(n)
    devices = [0] * n
    L = math.ceil(math.log(u,2))
    for i in range(0,no_tests):
        p = 0.5
        no_rounds = 0
        counter = 0
        while sum(devices) != 1:
            devices = [(0 if random.random() > p else 1) for i in range(0,n)]
            if counter > L:
                p = 0.5
                counter = 0
            else:
                p *= 0.5
            counter += 1
            no_rounds += 1
        devices = [0] * n
        histogram[n][no_rounds] = histogram[n].get(no_rounds, 0) + 1

for n in n_values:
    plt.bar(histogram[n].keys(), histogram[n].values())
    plt.show()