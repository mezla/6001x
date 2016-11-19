def genPrimes():
    n = 2
    primes = [2]
    count = 0
    yield  n

    while True:
        n += 1
        count = 0
        for p in primes:
            if n % p != 0:
                count += 1

        if len(primes) == count:
            primes.append(n)
            yield n
        else:
            continue
