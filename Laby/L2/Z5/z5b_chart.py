import matplotlib.pyplot as plt
import csv

k_vals = [2,3,100,400]
n = [i for i in range(1,10001)]
ratios = {k: [] for k in k_vals}

if __name__ == "__main__":
    with open('Laby/L2/Z5/k.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            for i,k in enumerate(k_vals):
                ratios[k].append(float(row[i]))
    for k in k_vals:
        plt.plot(n, ratios[k], label='k={}'.format(k))
    plt.xlabel("n")
    plt.ylabel("n_est/n")
    plt.legend()
    plt.savefig("Laby/L2/Z5/k.png", dpi=300)
    plt.close()
    for k in k_vals:
        plt.plot(n, ratios[k])
        plt.title("k={}".format(k))
        plt.xlabel("n")
        plt.ylabel("n_est/n")
        plt.legend()
        plt.savefig("Laby/L2/Z5/k={}.png".format(k), dpi=300)
        plt.close()