from math import inf
from copy import deepcopy


class State:
    def __init__(self, boss):
        self.boss = boss
        self.hp = 50
        self.mana = 500
        self.effects = dict()
        self.used = 0
        self.turn = 'Player'


def read_data():
    with open('input.txt') as data:
        stats = data.readlines()

    return int(stats[0].split(': ')[1]), int(stats[1].split(': ')[1])


def process_effects(state):
    if 'Poison' in state.effects:
        state.boss -= 3

    if 'Recharge' in state.effects:
        state.mana += 101

    for effect in list(state.effects):
        state.effects[effect] -= 1
        if state.effects[effect] == 0:
            del state.effects[effect]


def mana_cost(hard_mode=False):
    boss_hp, boss_atk = read_data()

    min_cost = inf
    queue = [State(boss=boss_hp)]

    while queue:
        state = queue.pop(-1)
        if min_cost < state.used:
            continue

        if state.turn == 'Player':
            if hard_mode:
                state.hp -= 1
                if state.hp <= 0:
                    continue

            process_effects(state)
            if state.boss <= 0:
                if min_cost > state.used:
                    min_cost = state.used
                continue

            for spell, mana, duration, damage, healing in (
                ('Missle', 53, 0, 4, 0),
                ('Drain', 73, 0, 2, 2),
                ('Shield', 113, 6, 0, 0),
                ('Poison', 173, 6, 0, 0),
                ('Recharge', 229, 5, 0, 0)
            ):
                if state.mana < mana:
                    break

                elif spell not in state.effects:
                    new_state = deepcopy(state)
                    new_state.mana -= mana
                    new_state.used += mana
                    new_state.turn = 'Boss'

                    if spell in ('Missle', 'Drain'):
                        new_state.boss -= damage
                        new_state.hp += healing

                        if new_state.boss <= 0:
                            if min_cost > new_state.used:
                                min_cost = new_state.used
                            continue

                    else:
                        new_state.effects[spell] = duration

                    queue.append(new_state)

        else:
            defense = 7 if 'Shield' in state.effects else 0
            process_effects(state)
            if state.boss <= 0:
                if min_cost > state.used:
                    min_cost = state.used
                continue

            state.hp -= max(boss_atk - defense, 1)
            if state.hp <= 0:
                continue

            state.turn = 'Player'
            queue.append(state)

    return min_cost
