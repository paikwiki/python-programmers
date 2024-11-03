# https://school.programmers.co.kr/learn/courses/30/lessons/133502


def solution(ingredient):
    stack = []
    result = 0
    for item in ingredient:
        stack.append(item)
        if stack[-4:] == [1, 2, 3, 1]:
            result += 1
            del stack[-4:]

    return result


inputs_and_outputs = [
    # ingredient, result
    ([2, 1, 1, 2, 3, 1, 2, 3, 1], 2),
    ([1, 3, 2, 1, 2, 1, 3, 1, 2], 0),
    ([1, 2, 3, 1, 1, 2, 3, 1], 2),
    ([1], 0),
    ([1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1], 3),
]
