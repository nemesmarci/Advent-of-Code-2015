import re
import sys

regex = re.compile(r"([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)")

lights = [[0 for x in range(1000)] for y in range(1000)]

for line in sys.stdin.readlines():
    action = "on" if "on" in line else "off" if "off" in line else "toggle"
    a, b, x, y = [int(num) for num in regex.search(line).groups()]
    for i in range(a, a + x - a + 1):
        for j in range(b, b + y - b + 1):
            if action == "on":
                lights[i][j] = 1
            elif action == "off":
                lights[i][j] = 0
            else:
                lights[i][j] = 0 if lights[i][j] == 1 else 1

print(sum([l for ll in lights for l in ll]))