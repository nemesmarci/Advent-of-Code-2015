import re
from common import diff

print(diff(lambda line: re.sub(r"\\x[0-9a-f]{2}", "_",
                               line[1:-1].replace(r"\\", "_")
                                         .replace(r"\"", "_"))))
