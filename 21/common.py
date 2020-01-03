import math
from itertools import combinations


def calculate_damage(attack, defense):
    return(max(attack - defense, 1))


def rounds_to_kill(damage, hp):
    return math.ceil(hp / damage)


def outfits():
    weapons = [
        {'cost': 8, 'atk': 4},
        {'cost': 10, 'atk': 5},
        {'cost': 25, 'atk': 6},
        {'cost': 40, 'atk': 7},
        {'cost': 74, 'atk': 8}
    ]

    armors = [
        {'cost': 0, 'def': 0},
        {'cost': 13, 'def': 1},
        {'cost': 31, 'def': 2},
        {'cost': 53, 'def': 3},
        {'cost': 75, 'def': 4},
        {'cost': 102, 'def': 5}
    ]

    rings = [
        {'cost': 0, 'atk': 0, 'def': 0},
        {'cost': 0, 'atk': 0, 'def': 0},
        {'cost': 25, 'atk': 1, 'def': 0},
        {'cost': 50, 'atk': 2, 'def': 0},
        {'cost': 100, 'atk': 3, 'def': 0},
        {'cost': 20, 'def': 1, 'atk': 0},
        {'cost': 40, 'def': 2, 'atk': 0},
        {'cost': 80, 'def': 3, 'atk': 0}
    ]

    rings = [{'cost': ring_a['cost'] + ring_b['cost'],
              'atk': ring_a['atk'] + ring_b['atk'],
              'def': ring_a['def'] + ring_b['def']}
             for ring_a, ring_b in combinations(rings, 2)]

    return sorted(
        ({'cost': weapon['cost'] + armor['cost'] + ring['cost'],
          'atk': weapon['atk'] + ring['atk'],
          'def': armor['def'] + ring['def']}
         for weapon in weapons for armor in armors for ring in rings),
        key=lambda outfit: outfit['cost'])


def find_cost(part_two=False):
    with open('input.txt') as data:
        stats = data.readlines()

    boss = {'hp': int(stats[0].split(': ')[1]),
            'atk': int(stats[1].split(': ')[1]),
            'def': int(stats[2].split(': ')[1])}

    for outfit in outfits():
        player = {'hp': 100, 'atk': outfit['atk'], 'def': outfit['def']}
        player_damage = calculate_damage(player['atk'], boss['def'])
        boss_damage = calculate_damage(boss['atk'], player['def'])
        rounds_to_kill_boss = rounds_to_kill(player_damage, boss['hp'])
        rounds_to_kill_player = rounds_to_kill(boss_damage, player['hp'])
        if rounds_to_kill_boss > rounds_to_kill_player:
            max_fail_cost = outfit['cost']
        elif not part_two:
            return outfit['cost']

    return max_fail_cost
