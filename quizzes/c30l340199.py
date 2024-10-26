# https://school.programmers.co.kr/learn/courses/30/lessons/340199


import math


def solution(wallet, bill):
    answer = 0

    wallet.sort()
    bill.sort()
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        if bill[0] > bill[1]:
            bill[0] = math.floor(bill[0] / 2)
        else:
            bill[1] = math.floor(bill[1] / 2)
        bill.sort()
        answer = answer + 1

    return answer


inputs_and_outputs = [
    # wallet, bill, result
    ([30, 15], [26, 17], 1),
    ([50, 50], [100, 241], 4),
]
