import sys

sx, sy = 0, 0
rx, ry = 0, 0
houses = set([(sx, sy)])
for i, c in enumerate(sys.stdin.readline().strip()):
    if i % 2:    
        sx += -1 if c == '<' else 1 if c == '>' else 0
        sy += -1 if c == 'v' else 1 if c == '^' else 0
        houses.add((sx, sy))
    else:
        rx += -1 if c == '<' else 1 if c == '>' else 0
        ry += -1 if c == 'v' else 1 if c == '^' else 0
        houses.add((rx, ry))
print(len(houses))