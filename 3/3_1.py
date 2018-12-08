import sys

x, y = 0, 0
houses = set([(x, y)])
for c in sys.stdin.readline().strip():
    x += -1 if c == '<' else 1 if c == '>' else 0
    y += -1 if c == 'v' else 1 if c == '^' else 0
    houses.add((x, y))
print(len(houses))