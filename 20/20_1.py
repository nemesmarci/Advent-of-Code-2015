from collections import Counter
from common import read_data


def prime_factors(n):
    i = 2
    factors = Counter()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors


goal = read_data()

i = 1
while True:
    sum_divisors = 1
    factors = prime_factors(i)
    for factor, n in factors.items():
        sum_divisors *= sum(factor ** i for i in range(n + 1))

    if sum_divisors >= goal / 10:
        print(i)
        break
    i += 1
