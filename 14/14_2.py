import re
import sys
from collections import defaultdict

regex = re.compile(r"([\w]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.")
limit = 2503

reindeers = dict()
distances = defaultdict(int)
points = defaultdict(int)

for line in sys.stdin.readlines():
    reindeer, speed, duration, rest = regex.match(line).groups()
    speed, duration, rest = [int(i) for i in [speed, duration, rest]]
    reindeers[reindeer] = [speed, duration, rest]

for second in range(limit):

    for name in reindeers:
        reindeer = reindeers[name]
        cycle = reindeer[1] + reindeer[2]
        relative_sec = second % cycle
        if relative_sec < reindeer[1]:
            distances[name] += reindeer[0]

    lead = max(distances.values())

    for name in reindeers:
        if distances[name] == lead:
            points[name] += 1

print(max(points.values()))