import random
import matplotlib.pyplot as plt
import math

no_tests = 10000
u_values = [pow(2,b) for b in range(8,16)]
u_lambda = [[],[],[]]

for u in u_values:
    print(u)
    n_values = [2, u//2, u]
    for j in range(0,3):
        rounds = 0
        passed = 0
        n = n_values[j]
        devices = [0] * n
        L = math.ceil(math.log(u,2))
        for i in range(0,no_tests):
            fail = False
            p = 1
            counter = 0
            while sum(devices) != 1:
                devices = [(0 if random.random() > p else 1) for i in range(0,n)]
                if counter > L:
                    fail = True
                else:
                    p *= 0.5
                counter += 1
            if not fail:
                passed += 1
            rounds += 1
            devices = [0] * n
        
        u_lambda[j].append(passed/rounds)

line1 = plt.plot(u_values, u_lambda[0], label="n = 2")
line2 = plt.plot(u_values, u_lambda[1], label="n = u/2")
line3 = plt.plot(u_values, u_lambda[2], label="n = u")
leg = plt.legend()
plt.savefig('z4.jpg', dpi=300)