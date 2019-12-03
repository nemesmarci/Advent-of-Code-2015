from lights import Lights

lights = Lights()

for corner in ((0, 0), (0, 99), (99, 0), (99, 99)):
    lights.state[corner] = 'X'

for i in range(100):
    lights.iterate()

print(lights.count_on())
