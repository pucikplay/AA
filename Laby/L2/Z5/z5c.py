import z5b
import math

n_vals = [n for n in range(1,10001)]
n_vals.reverse()

if __name__ == "__main__":
    l = 100
    r = 400
    while l < r:
        k = math.floor((l+r)/2)
        errors = 0
        counter = 1
        for n in n_vals:
            MM = [i for i in range(counter,counter+n)]
            counter += n
            error = abs(z5b.minCount(MM, z5b.hash, k)/n - 1)
            if error >= 0.1:
                errors += 1
            print(k, n, errors, error)
            if errors > 500:
                l = k + 1
                break
        if errors <= 500:
            r = k - 1
    print(r)

# 321 wychodzi
