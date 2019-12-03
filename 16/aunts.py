from collections import defaultdict

RESULTS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def read_data():
    aunts = defaultdict(dict)
    with open('input.txt') as data:
        for i, line in enumerate(data):
            tokens = [token.strip() for token in line.split(',')]
            tokens[0] = tokens[0][6 + len(str(i + 1)):]
            for token in tokens:
                key, value = token.split(':')
                aunts[i + 1][key] = int(value)
    return aunts
