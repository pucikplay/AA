import matplotlib.pyplot as plt

n_vals = [n for n in range(10001)]
MAX = 2**32

def hash(x):
    x = ((((x >> 16) % MAX) ^ x) * 0x45d9f3b) % MAX
    x = ((((x >> 16) % MAX) ^ x) * 0x45d9f3b) % MAX
    x = (((x >> 16) % MAX) ^ x) % MAX
    return x/MAX


if __name__ == "__main__":
    print(n_vals)
