from common import read_data

print(sum(1 if c == '(' else -1 for c in read_data()))
