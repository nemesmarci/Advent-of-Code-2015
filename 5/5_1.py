from common import count_nice


def is_nice(line):
    return (
        sum(line.count(c) for c in "aeiou") >= 3 and
        any(line[i] == line[i + 1] for i in range(len(line) - 1)) and
        not any(bad in line for bad in ("ab", "cd", "pq", "xy")))


print(count_nice(is_nice))
