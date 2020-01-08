import re
from collections import namedtuple

Wire = namedtuple('Wire', ['in1', 'in2', 'op'])


class Circuit:
    def __init__(self):
        assign_regex = re.compile(r"^([0-9a-z]+) -> ([a-z]+)$")
        and_regex = re.compile(r"^([0-9a-z]+) AND ([0-9a-z]+) -> ([a-z]+)$")
        lshift_regex = re.compile(r"^([0-9a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)$")
        not_regex = re.compile(r"^NOT ([0-9a-z]+) -> ([a-z]+)$")
        or_regex = re.compile(r"^([0-9a-z]+) OR ([0-9a-z]+) -> ([a-z]+)$")
        rshift_regex = re.compile(r"^([0-9a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)$")

        self.cache = dict()
        self.wires = dict()

        with open('input.txt') as data:
            for line in data:
                if 'AND' in line:
                    regex = and_regex
                    op = 'and'
                elif 'LSHIFT' in line:
                    regex = lshift_regex
                    op = 'lshift'
                elif 'NOT' in line:
                    regex = not_regex
                    op = 'not'
                elif 'OR' in line:
                    regex = or_regex
                    op = 'or'
                elif 'RSHIFT' in line:
                    regex = rshift_regex
                    op = 'rshift'
                else:
                    regex = assign_regex
                    op = 'assign'

                groups = regex.match(line).groups()

                if len(groups) == 2:
                    in1, out = groups
                    in2 = None
                else:
                    in1, in2, out = groups

                wire = Wire(in1, in2, op)
                self.wires[out] = wire

    def value_of(self, w):
        if w in self.cache:
            pass

        elif type(w) == int or w.isdigit():
            self.cache[w] = int(w)

        else:
            wire = self.wires[w]
            if wire.op == 'assign':
                value = self.value_of(wire.in1)
            elif wire.op == 'and':
                value = self.value_of(wire.in1) & self.value_of(wire.in2)
            elif wire.op == 'lshift':
                value = self.value_of(wire.in1) << int(wire.in2)
            elif wire.op == 'not':
                value = 65536 + ~self.value_of(wire.in1)
            elif wire.op == 'or':
                value = self.value_of(wire.in1) | self.value_of(wire.in2)
            elif wire.op == 'rshift':
                value = self.value_of(wire.in1) >> int(wire.in2)
            self.cache[w] = value

        return self.cache[w]

    def get_signal(self, part_two=False):
        if part_two:
            self.wires['b'] = Wire(self.value_of('a'), None, 'assign')
            self.cache.clear()

        return self.value_of('a')
