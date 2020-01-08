def count_nice(is_nice):
    with open('input.txt') as data:
        return sum(map(is_nice, data))
