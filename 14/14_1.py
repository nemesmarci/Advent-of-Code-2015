import re
import sys

regex = re.compile(r"([\w]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.")
limit = 2503

distances = dict()

for line in sys.stdin.readlines():
    reindeer, speed, duration, rest = regex.match(line).groups()
    speed, duration, rest = [int(i) for i in [speed, duration, rest]]
    cycle = duration + rest
    cycles = limit // cycle
    distance = cycles * duration * speed
    remaining = limit - cycles * cycle
    if remaining > duration:
        remaining = duration
    distance += remaining * speed
    distances[reindeer] = distance

print(max(distances.values()))