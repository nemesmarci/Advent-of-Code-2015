import sys
from collections import defaultdict

cities = defaultdict(dict)
shortest = None
begin = None

for line in sys.stdin.readlines():
    start, rem = line.split(' to ')
    end, dist = rem.split(' = ')
    dist = int(dist)
    if shortest is None or dist < shortest:
        shortest = dist
        begin = start
    cities[start][end] = dist
    cities[end][start] = dist

visited = [begin]
total_distance = 0

while len(visited) < len(cities):
    valid_targets = {c: d for c, d in cities[begin].items() if c not in visited}
    end = min(valid_targets.keys(), key=lambda c: valid_targets[c])
    visited.append(end)
    total_distance += valid_targets[end]
    begin = end

print(total_distance)