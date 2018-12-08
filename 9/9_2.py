import sys
from collections import defaultdict

cities = defaultdict(dict)

for line in sys.stdin.readlines():
    start, rem = line.split(' to ')
    end, dist = rem.split(' = ')
    cities[start][end] = int(dist)
    cities[end][start] = int(dist)

max_total = None

for city in cities:
    visited = [city]
    total_distance = 0
    while len(visited) < len(cities):
        valid_targets = {c: d for c, d in cities[city].items() if c not in visited}
        end = max(valid_targets.keys(), key=lambda c: valid_targets[c])
        visited.append(end)
        total_distance += valid_targets[end]
        city = end
    if max_total is None or total_distance > max_total:
        max_total = total_distance

print(max_total)