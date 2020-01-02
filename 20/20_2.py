from common import read_data


def divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
        i = i + 1
    return sorted(divisors)


goal = read_data()

i = 1
while True:
    if sum(d for d in divisors(i) if i <= d * 50) >= goal / 11:
        print(i)
        break
    i += 1
