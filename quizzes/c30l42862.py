# https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    result = 0
    rented = {}

    for current in range(1, n + 1):
        if current not in lost:
            result += 1
        elif current in reserve:
            result += 1
        elif (
            current - 1 in reserve
            and current - 1 not in lost
            and current - 1 not in rented
        ):
            rented[current - 1] = True
            result += 1
        elif (
            current + 1 in reserve
            and current + 1 not in lost
            and current + 1 not in rented
        ):
            rented[current + 1] = True
            result += 1

    return result


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
