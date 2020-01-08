from hashlib import md5
from itertools import count


def find_hash(zeros=5):
    with open('input.txt') as data:
        base = data.read()

    return next(i for i in count(start=1)
                if md5((base + str(i)).encode('utf-8'))
                .hexdigest()[:zeros] == '0' * zeros)
