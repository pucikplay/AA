import matplotlib.pyplot as plt
import csv

n = [i for i in range(1,10001)]
ratios = []

if __name__ == "__main__":
    with open('Laby/L3/z8.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            ratios.append(float(row[0]))
    plt.scatter(n[100:], ratios[100:], s=1)
    plt.xlabel("n")
    plt.ylabel("n_est/n")
    plt.savefig("Laby/L3/z8.png", dpi=300)
    plt.close()