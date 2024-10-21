import math


def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result = [0, 0, 0]

    for idx, student in enumerate([student1, student2, student3]):
        if len(student) < len(answers):
            extended = student * math.ceil(len(answers) / len(student))
        else:
            extended = student

        for answer, studentAnswer in zip(answers, extended):
            if answer == studentAnswer:
                result[idx] = result[idx] + 1

    maxValue = max(result)

    return [idx + 1 for idx, x in enumerate(result) if x == maxValue]


inputs_and_outputs = [
    ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [1]),
    ([1, 2, 3, 4, 5], [1]),
    ([1, 3, 2, 4, 2], [1, 2, 3]),
    ([1, 1, 5, 5, 1], [1, 2]),
]
