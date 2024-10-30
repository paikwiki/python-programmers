# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# Accessing dict_keys element by index in Python3
#  - https://stackoverflow.com/a/27638751/9908741


def solution(participant, completion):
    player_map = {}
    for player in participant:
        if player in player_map:
            player_map[player] += 1
        else:
            player_map[player] = 1

    for completed_player in completion:
        if player_map[completed_player] == 1:
            del player_map[completed_player]
        else:
            player_map[completed_player] -= 1

    return next(iter(player_map))


inputs_and_outputs = [
    # participant, completion, return
    (["leo", "kiki", "eden"], ["eden", "kiki"], "leo"),
    (
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["josipa", "filipa", "marina", "nikola"],
        "vinko",
    ),
    (["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"], "mislav"),
]
