import random
import matplotlib.pyplot as plt
import math

no_tests = 50
n = 1000
devices = [0] * n
probs = [pow(2,b) for b in range(int(-1.5*math.log(n,2)),int(-0.75*math.log(n,2)))]
averages = []

for p in probs:
    print(p)
    rounds = []
    for i in range(0,no_tests):
        no_rounds = 0
        while sum(devices) != 1:
            devices = [(0 if random.random() > p else 1) for i in range(0,n)]
            no_rounds += 1
        rounds.append(no_rounds)
        devices = [0] * n

    average = sum(rounds) / len(rounds)
    averages.append(average)

plt.plot(probs, averages)
plt.show()