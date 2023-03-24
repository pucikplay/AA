import matplotlib.pyplot as plt
import csv
import z6

k = 400
n = []
ratios = {x: [] for x in z6.hash_functions}

if __name__ == "__main__":
    with open('Laby/L2/Z6/hash.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            n.append(int(row[0]))
            for i,hash in enumerate(z6.hash_functions):
                ratios[hash].append(float(row[i + 1]))
    for hash in z6.hash_functions:
        plt.plot(z6.n_vals, ratios[hash], label=hash.__name__)
        plt.xlabel("n")
        plt.ylabel("est_n/n")
    plt.legend()
    plt.savefig('Laby/L2/Z6/hash.png', dpi=300)