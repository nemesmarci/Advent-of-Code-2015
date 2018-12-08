import sys

sum_length = 0
for line in sys.stdin.readlines():
    l, w, h = sorted([int(side) for side in line.split('x')])
    sum_length += 2 * (l + w) + l * w * h
print(sum_length)