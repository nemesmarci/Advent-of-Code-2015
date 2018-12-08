import sys

level = 0
for c in sys.stdin.readline().strip():
    level += 1 if c == '(' else -1
print(level)