# https://school.programmers.co.kr/learn/courses/30/lessons/250121


def solution(data, ext, val_ext, sort_by):
    dataMap = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    items = [i for i in data if i[dataMap[ext]] < val_ext]
    items.sort(key=lambda x: x[dataMap[sort_by]])

    return items


inputs_and_outputs = [
    # data, ext, val_ext, sort_by, result
    (
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "date",
        20300501,
        "remain",
        [[3, 20300401, 10, 8], [1, 20300104, 100, 80]],
    ),
]
