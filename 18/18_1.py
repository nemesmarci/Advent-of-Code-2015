from lights import Lights

lights = Lights()

for i in range(100):
    lights.iterate()

print(lights.count_on())
