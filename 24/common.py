from math import inf
from functools import reduce
from operator import mul


def prod(iterable):
    return reduce(mul, iterable, 1)


def calculate(containers=3):
    with open('input.txt') as data:
        presents = [int(line) for line in data]

    target_weigh = sum(presents) // containers

    best = (inf, inf)
    queue = [(0, (), presents)]

    while queue:
        weight, used, presents = queue.pop(0)

        for present in presents:
            if weight + present > target_weigh:
                break

            new_used = used + tuple([present])
            new_prod = prod(new_used)
            new_len = len(new_used)
            new_weight = weight + present

            if new_weight == target_weigh \
                and (len(new_used) < best[1]
                     or len(new_used) == best[1]
                     and new_prod < best[0]):
                best = (new_prod, new_len)

            elif new_len < best[1]:
                queue.append((new_weight, new_used,
                              [p for p in presents if p > present]))

    return best[0]
