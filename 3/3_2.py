from common import instructions

coordinates = {'santa': (0, 0), 'robo': (0, 0)}
houses = {coordinates['santa']}

for i, (cx, cy) in enumerate(instructions()):
    who = 'santa' if i % 2 else 'robo'
    x, y = coordinates[who]

    coordinates[who] = x + cx, y + cy
    houses.add(coordinates[who])

print(len(houses))
