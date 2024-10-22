# https://school.programmers.co.kr/learn/courses/30/lessons/135808


def solution(k, m, score):
    score.sort(reverse=True)
    boxes = [
        min(score[i : i + m]) * m
        for i in range(0, len(score), m)
        if len(score[i : i + m]) == m
    ]

    return sum(boxes)


inputs_and_outputs = [
    # k, m, score, result
    (3, 4, [1, 2, 3, 1, 2, 3, 1], 8),
    (4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2], 33),
]
