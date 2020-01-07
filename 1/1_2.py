from common import read_data

level = 0
for i, c in enumerate(read_data()):
    level += 1 if c == '(' else -1
    if level == -1:
        break
print(i + 1)
