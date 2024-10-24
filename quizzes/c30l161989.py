# https://school.programmers.co.kr/learn/courses/30/lessons/161989


def solution(n, m, section):
    idx = 0
    target = section[idx]
    next = target

    count = 0
    while next <= n:
        if idx >= len(section):
            break

        target = section[idx]
        if next <= target:
            count = count + 1
            next = target + m
        idx = idx + 1

    return count


inputs_and_outputs = [
    # n, m, section, result
    (8, 4, [2, 3, 6], 2),
    (5, 4, [1, 3], 1),
    (4, 1, [1, 2, 3, 4], 4),
]
