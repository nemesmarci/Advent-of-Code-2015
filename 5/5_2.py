import sys

def is_nice(line):
    double = False
    for i in range(len(line) - 1):
        pair = line[i:i + 2]
        if pair in line[i + 2:]:
            double = True
            break
    if not double:
        return 0
    one_between = False
    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            one_between = True
            break
    if not one_between:
        return 0
    return 1

nices = 0
for line in sys.stdin.readlines():
    nices += is_nice(line)
print(nices)