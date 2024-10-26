# https://school.programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    counts = {}
    for stage in stages:
        if stage in counts:
            counts[stage] = counts[stage] + 1
        else:
            counts[stage] = 1

    total = len(stages)

    rates = {}
    current = 0
    prev = {"total": total, "rest": 0}
    while current <= N + 1:
        currentStage = current
        if current in counts:
            currentRest = counts[current]
        else:
            currentRest = 0
        currentTotal = prev["total"] - prev["rest"]

        if currentTotal > 0:
            rates[currentStage] = currentRest / currentTotal
        else:
            rates[currentStage] = 0
        prev["total"] = currentTotal
        prev["rest"] = currentRest
        current = current + 1

    return list(
        map(
            lambda x: x[0],
            filter(
                lambda x: 0 < x[0] < N + 1,
                sorted(list(rates.items()), key=lambda x: x[1], reverse=True),
            ),
        )
    )


inputs_and_outputs = [
    # N, stages, result
    (5, [2, 1, 2, 6, 2, 4, 3, 3], [3, 4, 2, 1, 5]),
    (4, [4, 4, 4, 4, 4], [4, 1, 2, 3]),
    (3, [1, 1, 1], [1, 2, 3]),
    (3, [2, 2, 2], [2, 1, 3]),
    (3, [3, 3, 3], [3, 1, 2]),
    (1, [2, 2, 2], [1]),
    (1, [1, 1, 1], [1]),
    (1, [1, 1, 2], [1]),
    (2, [1, 1, 2, 2], [2, 1]),
    (2, [1, 1, 3, 3], [1, 2]),
]
