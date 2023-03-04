import random
import matplotlib.pyplot as plt
import math
import time

no_tests = 50
n = 1000
u_values = [1000 * b for b in range(1,20)]
devices = [0] * n
averages = []

for u in u_values:
    print(u)
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

plt.plot(u_values, averages)
plt.show()