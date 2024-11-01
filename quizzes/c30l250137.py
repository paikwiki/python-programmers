# https://school.programmers.co.kr/learn/courses/30/lessons/250137


def solution(bandage, health, attacks):

    max_time = 0
    max_damage = 0
    for time, damage in attacks:
        if max_time < time:
            max_time = time
        if max_damage < damage:
            max_damage = damage

    if health <= max_damage:
        return -1

    current_health = health
    heal_time = 0
    iter_attacks = iter(attacks)
    attack = next(iter_attacks)
    for current_time in range(1, max_time + 1):
        if current_time == attack[0]:
            current_health -= attack[1]
            heal_time = 0
            try:
                attack = next(iter_attacks)
            except:
                break
            continue

        if current_health < 1:
            return -1

        current_health = min(health, current_health + bandage[1])
        heal_time += 1

        if heal_time == bandage[0]:
            current_health = min(health, current_health + bandage[2])
            heal_time = 0

    if current_health == 0:
        return -1

    return current_health


inputs_and_outputs = [
    # bandage, health, attacks, result
    ([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]], 5),
    ([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]], -1),
    ([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]], -1),
    ([1, 1, 1], 5, [[1, 2], [3, 2]], 3),
    ([1, 1, 1], 5, [[1, 5]], -1),
]
