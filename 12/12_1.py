import re
import sys

line = sys.stdin.readline().strip()
line = re.sub(r"[^0-9-]+", " ", line)
print(sum([int(i) for i in line.split()]))