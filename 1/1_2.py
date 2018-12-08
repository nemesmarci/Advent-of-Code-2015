import sys

level = 0
for i, c in enumerate(sys.stdin.readline().strip()):
    level += 1 if c == '(' else -1
    if level == -1:
        break
print(i + 1)