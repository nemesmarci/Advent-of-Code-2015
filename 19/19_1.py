import re
from common import get_data

replacements, molecule = get_data()


def possible(start):
    results = set()
    for replacement, variants in replacements.items():
        matches = re.finditer(replacement, start)
        for match in matches:
            for variant in variants:
                results.add(start[:match.start()] +
                            variant +
                            start[match.start() + len(replacement):])
    return len(results)


print(possible(molecule))
