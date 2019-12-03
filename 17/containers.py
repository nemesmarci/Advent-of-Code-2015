from itertools import combinations

TOTAL = 150


def read_data():
    with open('input.txt') as data:
        return [int(line.strip()) for line in data]


def possible_combinations(containers, return_early=False):
    n = 0
    for i in range(len(containers)):
        for combination in combinations(containers, i):
            if sum(combination) == TOTAL:
                n += 1
        if return_early and n != 0:
            break
    return n
