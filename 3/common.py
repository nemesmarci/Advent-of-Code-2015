def instructions():
    with open('input.txt') as data:
        return (parse_instruction(c) for c in data.read())


def parse_instruction(c):
    return (-1 if c == '<' else 1 if c == '>' else 0,
            -1 if c == 'v' else 1 if c == '^' else 0)
