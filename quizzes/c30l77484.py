# https://school.programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    lost_count = 0
    wrong_count = 0
    for num in lottos:
        if num == 0:
            lost_count = lost_count + 1
        elif not num in win_nums:
            wrong_count = wrong_count + 1

    if lost_count == 6:
        return [1, 6]
    elif wrong_count == 6:
        return [6, 6]
    else:
        max_rank = wrong_count + 1
        return [max_rank, max_rank + lost_count]


inputs_and_outputs = [
    # lottos, win_nums, result
    ([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19], [3, 5]),
    ([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25], [1, 6]),
    ([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35], [1, 1]),
    ([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [6, 6]),
]
