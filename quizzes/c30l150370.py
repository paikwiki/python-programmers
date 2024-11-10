# https://school.programmers.co.kr/learn/courses/30/lessons/150370


def get_current_custom_day(date_str):
    Y, M, D = date_str.split(".")

    return ((28 * 12) * (int(Y) - 2020)) + 28 * (int(M) - 1) + int(D)


def solution(today, terms, privacies):
    custom_today = get_current_custom_day(today)

    termsMap = {}
    for term in terms:
        key, value = term.split(" ")
        termsMap[key] = int(value) * 28

    result = []
    for idx, privacy in enumerate(privacies, 1):
        date, key = privacy.split(" ")
        custom_date = get_current_custom_day(date)
        if termsMap[key] <= custom_today - custom_date:
            result.append(idx)

    return result


inputs_and_outputs = [
    # today, terms, privacies, result
    (
        "2022.05.19",
        ["A 6", "B 12", "C 3"],
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        [1, 3],
    ),
    (
        "2020.01.01",
        ["Z 3", "D 5"],
        [
            "2019.01.01 D",
            "2019.11.15 Z",
            "2019.08.02 D",
            "2019.07.01 D",
            "2018.12.28 Z",
        ],
        [1, 4, 5],
    ),
]
