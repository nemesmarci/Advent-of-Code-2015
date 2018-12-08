import sys

vowels = [v for v in "aeiou"]
bads = ["ab", "cd", "pq", "xy"]

def is_nice(line):
    if len([c for c in line if c in vowels]) < 3:
        return 0
    double = False
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            double = True
            break
    if not double:
        return 0
    for b in bads:
        if b in line:
            return 0
    return 1

nices = 0
for line in sys.stdin.readlines():
    nices += is_nice(line)
print(nices)