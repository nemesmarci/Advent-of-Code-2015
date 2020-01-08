def boxes():
    with open('input.txt') as data:
        return [sorted(int(side) for side in line.split('x')) for line in data]
