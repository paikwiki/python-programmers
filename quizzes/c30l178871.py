# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    positions = {player: i for i, player in enumerate(players)}
    for calling in callings:
        idx = positions[calling]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        positions[players[idx]] = idx
        positions[players[idx - 1]] = idx - 1

    return players


inputs_and_outputs = [
    # players, callings, result
    (
        ["mumu", "soe", "poe", "kai", "mine"],
        ["kai", "kai", "mine", "mine"],
        ["mumu", "kai", "mine", "soe", "poe"],
    ),
    (
        ["a", "b", "c"],
        ["b", "c", "a", "c", "a"],
        ["b", "a", "c"],
    ),
]
