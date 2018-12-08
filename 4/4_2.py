import sys
import hashlib

base = sys.stdin.readline().strip()
i = 1
while hashlib.md5((base + str(i)).encode('utf-8')).hexdigest()[:6] != "000000":
    i += 1
print(i)