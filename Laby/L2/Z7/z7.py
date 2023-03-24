import csv
import matplotlib.pyplot as plt
import sys

k = 400
n = [i for i in range(1,10001)]
ratios = []
alpha = [0.05, 0.01, 0.005]
delta = []
delta_plus = []
delta_minus = []
colours = ['olivedrab','peru','brown']

if __name__ == "__main__":
    with open('Laby/L2/Z5/k.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            ratios.append(float(row[4]))
    csvfile.close()
    ratios_sorted = [abs(1-r) for r in ratios]
    ratios_sorted.sort()

    for a in alpha:
        delta.append(ratios_sorted[int((1-a)*10000)])
    
    for d in delta:
        delta_plus.append([1 + d] * 10000)
        delta_minus.append([1 - d] * 10000)

    plt.scatter(n, ratios, s=1)
    for i in range(3):
        plt.plot(n, delta_plus[i], color=colours[i])
        plt.plot(n, delta_minus[i], color=colours[i])
    plt.xlabel("n")
    plt.ylabel("est_n/n")
    plt.savefig("Laby/L2/Z7/delta.png", dpi=300)