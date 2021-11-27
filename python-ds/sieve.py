import math

def sieve(maxn=1000000):
    arry = [0] * math.ceil(maxn / 8)

    def setbit(idx):
        i = idx // 8
        j = idx % 8
        arry[i] |= (1 << j)

    def isbitset(idx):
        i = idx // 8
        j = idx % 8
        return (arry[i] & (1 << j)) > 0

    for i in range(2, maxn):
        if isbitset(i):
            continue
        for j in range(i * i, maxn, i):
            setbit(j)

    primes = []
    for i in range(2, maxn):
        if not isbitset(i):
            primes.append(i)

    return primes

