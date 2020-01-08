import re


def solve(part_two=False):
    range_regex = re.compile(r"([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)")
    action_regex = re.compile(r"on|off|toggle")

    lights = [0] * 1000 * 1000

    with open('input.txt') as data:
        for line in data:
            action = action_regex.search(line).group(0)
            x0, y0, x1, y1 = map(int, range_regex.search(line).groups())
            for x in range(x0, x1 + 1):
                for y in range(y0, y1 + 1):
                    index = x * 1000 + y
                    current = lights[index]
                    if action == "on":
                        lights[index] = current + 1 if part_two else 1
                    elif action == "off":
                        lights[index] = current - 1 if part_two and \
                            current > 0 else 0
                    else:
                        lights[index] = current + 2 if part_two \
                            else 1 - current

    return(sum(lights))
