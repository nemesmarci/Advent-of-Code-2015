import re
import sys

regex = re.compile(r"^([\w]+): capacity ([0-9-]+), durability ([0-9-]+), flavor ([0-9-]+), texture ([0-9-]+), calories ([0-9-]+)$")

ingredients = dict()

for line in sys.stdin.readlines():
    name, capacity, durability, flavor, texture, calories = regex.match(line).groups()
    capacity, durability, flavor, texture, calories = [int(i) for i in [capacity, durability, flavor, texture, calories]]
    ingredients[name] = [capacity, durability, flavor, texture, calories]

recipes = dict()

for i in range(0, 100 + 1):
    for j in range(0, 100 + 1 - i):
        for k in range(0, 100 + 1 - i - j):
            for l in range(100 - (i + j + k), 100 + 1 - i - j - k):

                total_capacity = total_durability = total_flavor = total_texture = total_calories = 0
                amounts = [i, j, k, l]

                for n, name in enumerate(ingredients):
                    total_capacity += ingredients[name][0] * amounts[n]
                    total_durability += ingredients[name][1] * amounts[n]
                    total_flavor += ingredients[name][2] * amounts[n]
                    total_texture += ingredients[name][3] * amounts[n]
                    total_calories += ingredients[name][4] * amounts[n]

                total_durability = 0 if total_durability < 0 else total_durability
                total_flavor = 0 if total_flavor < 0 else total_flavor
                total_texture = 0 if total_texture < 0 else total_texture

                if total_calories == 500:
                    recipes[(i, j, k, l)] = total_capacity * total_durability * total_flavor * total_texture

print(max(recipes.values()))