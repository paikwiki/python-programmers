# https://school.programmers.co.kr/learn/courses/30/lessons/131128


from itertools import zip_longest


def solution(X, Y):
    template_map = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "0": 0,
    }
    x_map = template_map.copy()
    y_map = template_map.copy()
    for x_item, y_item in zip_longest(X, Y):
        if x_item is not None:
            x_map[x_item] += 1
        if y_item is not None:
            y_map[y_item] += 1

    total_map = template_map.copy()
    for key in x_map.keys():
        total_map[key] = min(x_map[key], y_map[key])

    digits = [
        item
        for item in sorted(total_map.items(), key=lambda x: x[0], reverse=True)
        if item[1] > 0
    ]

    if len(digits) == 0:
        return "-1"

    if digits[0][0] == "0":
        return "0"

    result = ""
    for digit, count in digits:
        result += digit * count

    return result


inputs_and_outputs = [
    # X, Y, result
    ("100", "2345", "-1"),
    ("100", "203045", "0"),
    ("100", "123450", "10"),
    ("12321", "42531", "321"),
    ("5525", "1255", "552"),
]
