# https://school.programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False

    return sum(sieve)


inputs_and_outputs = [
    # n, result
    (10, 4),
    (5, 3),
]
