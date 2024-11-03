# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    dolls = {}
    previous_bucket = []
    result = 0
    for row in board:
        for item_num, item in enumerate(row, 1):
            if item == 0:
                continue
            if item_num in dolls:
                dolls[item_num].append(item)
            else:
                dolls[item_num] = [item]
    print(f"{dolls}")
    for move in moves:
        if dolls[move]:
            current = dolls[move].pop(0)
            if previous_bucket and current == previous_bucket[-1]:
                result += 2
                previous_bucket.pop()
            else:
                previous_bucket.append(current)

    return result


inputs_and_outputs = [
    # board, moves, result
    (
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
        4,
    ),
]
