import random
import matplotlib.pyplot as plt
import math
import time

no_tests = 50
u = 1000
n_values = [2, u//2, u]
averages = []

for n in n_values:
    print(n)
    devices = [0] * n
    rounds = []
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
        rounds.append(no_rounds)
        devices = [0] * n

    average = sum(rounds) / len(rounds)
    averages.append(average)

plt.plot(n_values, averages)
plt.show()