# https://school.programmers.co.kr/learn/courses/30/lessons/17682


import re


def solution(dartResult):
    shots = re.findall(r"(\d+)([SDT][*#]?)", dartResult)

    computed_points = []
    for idx, (point, option) in enumerate(shots):
        computed = 0
        if option[0] == "S":
            computed = int(point)
        elif option[0] == "D":
            computed = int(point) ** 2
        elif option[0] == "T":
            computed = int(point) ** 3

        if len(option) == 2:
            if option[1] == "#":
                computed = computed * -1
            elif option[1] == "*":
                computed = computed * 2
                if idx > 0:
                    computed_points[idx - 1] = computed_points[idx - 1] * 2

        computed_points.append(computed)

    return sum(computed_points)


inputs_and_outputs = [
    # dartResult, answer
    ("1S2D*3T", 37),
    ("1D2S#10S", 9),
    ("1D2S0T", 3),
    ("1S*2T*3S", 23),
    ("1D#2S*3S", 5),
    ("1T2D3D#", -4),
    ("1D2S3T*", 59),
]
