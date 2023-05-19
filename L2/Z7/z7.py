import csv
import matplotlib.pyplot as plt
import math

k = 400
n = [i for i in range(1,10001)]
ratios = []
alpha = [0.05, 0.01, 0.005]
delta_exp = []
delta_cz = []
delta_ch = []
colours = ['olivedrab','peru','brown']
names = ['delta_exp', 'delta_cz', 'delta_ch']

def f(k,x):
    return (math.e**(k*x))*(1-x)**k

def calc_alpha(delta):
    e1 = 1/(1-delta) - 1
    e2 = 1 - 1/(1+delta)
    return f(400,e2) + f(400,-e1)

def find_delta(alpha):
    l = 0.0
    r = 0.2
    delta = (l+r)/2
    while abs(calc_alpha(delta) - alpha) > 0.0000001:
        delta = (l+r)/2
        if calc_alpha(delta) > alpha:
            l = delta
        else:
            r = delta
    return delta

if __name__ == "__main__":
    with open('L2/Z5/k.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            ratios.append(float(row[4]))
    csvfile.close()
    ratios_sorted = [abs(1-r) for r in ratios]
    ratios_sorted.sort()

    for a in alpha:
        delta_exp.append(ratios_sorted[int((1-a)*10000)])
        delta_cz.append(math.sqrt((1/k)/a))
        delta_ch.append(find_delta(a))

    plt.scatter(n, ratios, s=1)
    for i in range(3):
        plt.plot(n, [1 + delta_exp[i]] * 10000, color=colours[i])
        plt.plot(n, [1 - delta_exp[i]] * 10000, color=colours[i])
    plt.xlabel("n")
    plt.ylabel("est_n/n")
    plt.savefig("L2/Z7/delta.png", dpi=300)
    plt.close()

    for i,a in enumerate(alpha):
        plt.scatter(n, ratios, s=1)
        for j,delta in enumerate([delta_exp, delta_cz, delta_ch]):
            plt.plot(n, [1 + delta[i]] * 10000, color=colours[j], label=names[j])
            plt.plot(n, [1 - delta[i]] * 10000, color=colours[j])
        plt.xlabel("n")
        plt.ylabel("est_n/n")
        plt.title("alpha={}".format(a))
        plt.legend()
        plt.savefig("L2/Z7/delta_{}.png".format(a), dpi=300)
        plt.close()