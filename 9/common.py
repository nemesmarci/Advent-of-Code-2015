from math import inf
from collections import defaultdict


def read_data():
    cities = defaultdict(dict)
    shortest = inf

    with open('input.txt') as data:
        for line in data:
            start, rem = line.split(' to ')
            end, dist = rem.split(' = ')
            dist = int(dist)
            if dist < shortest:
                shortest = dist
                begin = start
            cities[start][end] = int(dist)
            cities[end][start] = int(dist)

    return cities, begin


def traverse(cities, begin, sort=min):
    visited = [begin]
    total_distance = 0

    while len(visited) < len(cities):
        valid_targets = {c: d for c, d in cities[begin].items()
                         if c not in visited}
        end = sort(valid_targets.keys(), key=lambda c: valid_targets[c])
        visited.append(end)
        total_distance += valid_targets[end]
        begin = end
    return total_distance
