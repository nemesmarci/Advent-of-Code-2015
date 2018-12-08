import sys

code_chars = 0
mem_chars = 0
for line in sys.stdin.readlines():
    mem_chars += len(line)
    code_chars += len(line.replace("\\", "\\\\").replace("\"", "\\\"")) + 2

print(code_chars - mem_chars)