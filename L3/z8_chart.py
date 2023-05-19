import matplotlib.pyplot as plt
import csv
import pandas as pd

n_vals = [n for n in range(1,10001)]
b_vals = [b for b in range(4,17)]
colours = ['olivedrab','peru','brown']
names = ['Urny i kule małe', 'HyperLogLog', 'Urny i kule duże']
hashes = ['blake', 'sha', 'md5']

if __name__ == "__main__":
    for hash in hashes:
        ratios = {b: [] for b in b_vals}
        with open('L3/z8_{}.csv'.format(hash)) as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for row in reader:
                for i,b in enumerate(b_vals):
                    ratios[b].append((int(row[i*2]),float(row[i*2 + 1])))
        ratios_vals = {b: [r[1] for r in ratios[b]] for b in b_vals}
        ratios_types = {b: [r[0] for r in ratios[b]] for b in b_vals}
        for b in b_vals:
            df = pd.DataFrame({'x' : n_vals,
                            'y' : ratios_vals[b],
                            'z' : ratios_types[b]})
            groups = df.groupby('z')
            for name, group in groups:
                plt.scatter(group.x, group.y, s=2, label=names[name - 1])
            plt.title("h={}, b={}".format(hash,b))
            plt.legend()
            plt.xlabel("n")
            plt.ylabel("n_est/n")
            plt.savefig("L3/charts/z8_{}_b={}.png".format(hash,b), dpi=300)
            plt.close()