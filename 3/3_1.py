from common import instructions

x, y = 0, 0
houses = {(x, y)}

for cx, cy in instructions():
    x, y = x + cx, y + cy
    houses.add((x, y))

print(len(houses))
