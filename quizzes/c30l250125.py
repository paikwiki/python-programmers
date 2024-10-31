# https://school.programmers.co.kr/learn/courses/30/lessons/250125


def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(0, 4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count


inputs_and_outputs = [
    # board, h, w, result
    (
        [
            ["blue", "red", "orange", "red"],
            ["red", "red", "blue", "orange"],
            ["blue", "orange", "red", "red"],
            ["orange", "orange", "red", "blue"],
        ],
        1,
        1,
        2,
    ),
    (
        [
            ["yellow", "green", "blue"],
            ["blue", "green", "yellow"],
            ["yellow", "blue", "blue"],
        ],
        0,
        1,
        1,
    ),
]
