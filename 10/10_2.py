import sys
from itertools import groupby

num = sys.stdin.readline().strip()

def look_and_say(num):
    ret = ""
    for _, g in groupby(num):
        group = list(g)
        ret += str(len(group)) + group[0]
    return ret

for i in range(50):    
    num = look_and_say(num)

print(len(num))