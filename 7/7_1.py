import re
import sys
from collections import namedtuple

assign_regex = re.compile(r"^([0-9a-z]+) -> ([a-z]+)$")
and_regex = re.compile(r"^([0-9a-z]+) AND ([0-9a-z]+) -> ([a-z]+)$")
lshift_regex = re.compile(r"^([0-9a-z]+) LSHIFT ([0-9]+) -> ([a-z]+)$")
not_regex = re.compile(r"^NOT ([0-9a-z]+) -> ([a-z]+)$")
or_regex = re.compile(r"^([0-9a-z]+) OR ([0-9a-z]+) -> ([a-z]+)$")
rshift_regex = re.compile(r"^([0-9a-z]+) RSHIFT ([0-9]+) -> ([a-z]+)$")

Wire = namedtuple('Wire', ['in1', 'in2', 'op'])
wires = dict()

for line in sys.stdin.readlines():
    if assign_regex.match(line):
        in1, out = assign_regex.match(line).groups()
        wires[out] = Wire(in1, None, 'assign')
    elif and_regex.match(line):
        in1, in2, out = and_regex.match(line).groups()
        wires[out] = Wire(in1, in2, 'and')
    elif lshift_regex.match(line):
        in1, in2, out = lshift_regex.match(line).groups()
        wires[out] = Wire(in1, int(in2), 'lshift')
    elif not_regex.match(line):
        in1, out = not_regex.match(line).groups()
        wires[out] = Wire(in1, None, 'not')
    elif or_regex.match(line):
        in1, in2, out = or_regex.match(line).groups()
        wires[out] = Wire(in1, in2, 'or')
    elif rshift_regex.match(line):
        in1, in2, out = rshift_regex.match(line).groups()
        wires[out] = Wire(in1, int(in2), 'rshift')

cache = dict()

def value_of(w):
    if w in cache:
        return cache[w]
    try:
        value = int(w)
        cache[w] = value
        return value
    except ValueError:
        pass
    wire = wires[w]
    if wire.op == 'assign':
        value = value_of(wire.in1)
    elif wire.op == 'and':
        value = value_of(wire.in1) & value_of(wire.in2)
    elif wire.op == 'lshift':
        value = value_of(wire.in1) << wire.in2
    elif wire.op == 'not':
        value = 65536 + ~value_of(wire.in1) 
    elif wire.op == 'or':
        value = value_of(wire.in1) | value_of(wire.in2)
    elif wire.op == 'rshift':
        value = value_of(wire.in1) >> wire.in2
    cache[w] = value
    return value

print(value_of('a'))