import re
import sys

code_chars = 0
mem_chars = 0
for line in sys.stdin.readlines():
    code_chars += len(line)
    mem_chars += len(re.sub(r"\\x[0-9a-f]{2}", "_",
                            line[1:-1].replace(r"\\", "_")
                                      .replace(r"\"", "_")))

print(code_chars - mem_chars)