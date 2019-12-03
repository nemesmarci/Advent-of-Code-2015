from copy import deepcopy


class Lights:
    def __init__(self):
        state = {}
        with open('input.txt') as data:
            for x, line in enumerate(data):
                for y, char in enumerate(line.strip()):
                    state[(x, y)] = char
        self.state = state

    def neighbours(self, point):
        px, py = point
        return [(x, y) for x in (px - 1, px, px + 1)
                for y in (py - 1, py, py + 1)
                if (x, y) in self.state and (x, y) != point]

    def count_on(self, target=None):
        if target is None:
            target = self.state
        return sum(1 for p in target if self.state[p] in '#X')

    def iterate(self):
        new_lights = deepcopy(self.state)
        for p in self.state:
            on_count = self.count_on(self.neighbours(p))
            if self.state[p] == '#' and on_count not in (2, 3):
                new_lights[p] = '.'
            elif self.state[p] == '.' and on_count == 3:
                new_lights[p] = '#'
        self.state = new_lights
