from common import read_data, traverse

cities = read_data()[0]
print(max(traverse(cities, city, sort=max) for city in cities))
