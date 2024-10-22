# https://school.programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    result = [1] * (n + 1)
    result[0:2] = [0, 0]

    for idx in range(2, n):
        mul = 2
        current = idx * mul
        while current <= n:
            if result[current] == 1:
                result[current] = 0
            mul = mul + 1
            current = idx * mul

    return sum(result)


inputs_and_outputs = [
    # n, result
    (10, 4),
    (5, 3),
]
