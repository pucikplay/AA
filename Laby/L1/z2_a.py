import random
import matplotlib.pyplot as plt

no_tests = 100
n = 1000
devices = [0] * n
p = 1/n
histogram = {}

for i in range(0,no_tests):
    no_rounds = 0
    while sum(devices) != 1:
        devices = [(0 if random.random() > p else 1) for i in range(0,n)]
        no_rounds += 1
    histogram[no_rounds] = histogram.get(no_rounds, 0) + 1
    devices = [0] * n

plt.bar(histogram.keys(), histogram.values())
plt.show()