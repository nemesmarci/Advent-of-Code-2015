from collections import defaultdict


def get_data():
    replacements = defaultdict(set)

    with open('input.txt') as data:
        for line in data:
            if '=>' in line:
                a, b = line.strip().split(" => ")
                replacements[a].add(b)
            elif line.strip() != "":
                molecule = line.strip()

    return replacements, molecule
