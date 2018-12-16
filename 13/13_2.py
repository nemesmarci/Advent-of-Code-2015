import re
import sys
from collections import defaultdict
from itertools import permutations

regex = re.compile(r"^([\w]+) would (gain|lose) ([0-9]+) happiness units by sitting next to ([\w]+).$")

happiness = defaultdict(dict)

for line in sys.stdin.readlines():
    a, direction, value, b = regex.match(line).groups()
    value = int(value) if direction == 'gain' else -int(value)
    happiness[a][b] = value

for key in list(happiness.keys()):
    happiness['me'][key] = 0
    happiness[key]['me'] = 0

max_happiness = None

for permutation in permutations(happiness.keys()):
    total_happiness = 0

    for i in range(len(permutation)):
        person = permutation[i]
        left = permutation[(i - 1) % len(permutation)]
        right = permutation[(i + 1) % len(permutation)]
        total_happiness += happiness[person][left] + happiness[person][right]

    if max_happiness is None or total_happiness > max_happiness:
        max_happiness = total_happiness

print(max_happiness)