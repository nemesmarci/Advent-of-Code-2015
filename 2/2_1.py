import sys

sum_area = 0
for line in sys.stdin.readlines():
    l, w, h = [int(side) for side in line.split('x')]
    sides = [(l * w), (w * h), (h * l)]
    smallest = min(sides)
    sum_area += 2 * sum(sides) + smallest
print(sum_area)