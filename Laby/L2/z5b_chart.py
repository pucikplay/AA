import matplotlib.pyplot as plt
import csv

k_vals = [2,3,100,400]
n = []
ratio = []

if __name__ == "__main__":
    for k in k_vals:
        print(k)
        with open('Laby/L2/k={}.csv'.format(k)) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                n.append(int(row[0]))
                ratio.append(float(row[1]))
        plt.plot(n, ratio)
        plt.title("k={}".format(k))
        plt.xlabel("n")
        plt.ylabel("n_est/n")
        plt.savefig("Laby/L2/k={}.png".format(k), dpi=300)
        n.clear()
        ratio.clear()