import sys
from itertools import groupby

password = sys.stdin.readline().strip()


def increment(password):
    last = password[-1]
    if last == 'z':
        last = 'a'
        password = increment(password[:-1]) + last
    else:
        last = chr(ord(last) + 1)
        password = password[:-1] + last
    return password

triples = [chr(c) + chr(c + 1) + chr(c + 2) for c in range(ord('a'), ord('x') + 1)]


def correct(password):
    if not any(triple in password for triple in triples):
        return False
    if any(c in password for c in 'iol'):
        return False
    doubles = set()
    for c, g in groupby(password):
        if len(list(g)) > 1:
            doubles.add(c)
    if len(doubles) < 2:
        return False
    return True

password = increment(password)

while not correct(password):
    password = increment(password)

password = increment(password)

while not correct(password):
    password = increment(password)

print(password)