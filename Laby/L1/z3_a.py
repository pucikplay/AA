import random
import matplotlib.pyplot as plt
import math

no_tests = 100
n_values = [pow(2,b) for b in range(8,20)]
averages = []
variance = []

for n in n_values:
    print(n)
    devices = [0] * n
    rounds = []
    p = 1/n
    for i in range(0,no_tests):
        L = 0
        while sum(devices) != 1:
            devices = [(0 if random.random() > p else 1) for i in range(0,n)]
            L += 1
        rounds.append(L)
        devices = [0] * n

    average = sum(rounds) / len(rounds)
    averages.append(average)
    variance.append(sum(pow(x - average, 2) for x in averages) / len(averages))


plt.plot(n_values, averages)
plt.plot(n_values, variance)
plt.plot(n_values, [math.e] * len(averages))
plt.show()