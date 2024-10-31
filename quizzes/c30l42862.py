# https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)

    for r in reserve_only:
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)

    return n - len(lost_only)


inputs_and_outputs = [
    # n, lost, reserve, return
    (5, [2, 4], [1, 3, 5], 5),
    (5, [2, 4], [3], 4),
    (3, [3], [1], 2),
    (5, [1, 2], [2, 3, 4, 5], 4),
    (5, [2, 3], [2, 3], 5),
    (5, [3, 5], [2, 4], 5),
    (5, [2, 4], [3, 5], 5),
]
