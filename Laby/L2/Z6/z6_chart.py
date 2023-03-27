import matplotlib.pyplot as plt
import csv
import z6

k = 400
n = [i for i in range(1,10001)]
ratios = {x: [] for x in z6.hash_functions}

if __name__ == "__main__":
    with open('Laby/L2/Z6/hash.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            for i,hash in enumerate(z6.hash_functions):
                ratios[hash].append(float(row[i]))
        csvfile.close()
        
    for hash in z6.hash_functions:
        plt.scatter(z6.n_vals, ratios[hash], label=hash.__name__, s=1)
    plt.xlabel("n")
    plt.ylabel("est_n/n")
    plt.legend()
    plt.savefig('Laby/L2/Z6/hash.png', dpi=300)
    plt.close()

    for hash in z6.small_functions:
        plt.scatter(z6.n_vals, ratios[hash], label=hash.__name__, s=1)
    plt.xlabel("n")
    plt.ylabel("est_n/n")
    plt.legend()
    plt.savefig('Laby/L2/Z6/small_hash.png', dpi=300)
    plt.close()