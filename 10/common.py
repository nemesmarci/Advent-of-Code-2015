from itertools import groupby


def look_and_say(iterations=40):
    with open('input.txt') as data:
        num = data.read()

    for i in range(iterations):
        num = "".join(str(len(list(g))) + k for k, g in groupby(num))

    return(len(num))
