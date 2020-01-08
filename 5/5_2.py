from common import count_nice


def is_nice(line):
    return (
        any(line[i:i + 2] in line[i + 2:] for i in range(len(line) - 1)) and
        any(line[i] == line[i + 2] for i in range(len(line) - 2)))


print(count_nice(is_nice))
