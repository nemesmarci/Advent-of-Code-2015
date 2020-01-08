def diff(replace):
    with open('input.txt') as data:
        return abs(sum(len(line) - len(replace(line)) for line in data))
