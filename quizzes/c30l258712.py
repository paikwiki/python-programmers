# https://school.programmers.co.kr/learn/courses/30/lessons/258712

# ChatGPT 개선 코드
from collections import defaultdict


def solution(friends, gifts):
    given = defaultdict(int)
    received = defaultdict(int)
    pair_gift_count = defaultdict(lambda: defaultdict(int))

    for gift in gifts:
        giver, receiver = gift.split()
        given[giver] += 1
        received[receiver] += 1
        pair_gift_count[giver][receiver] += 1

    next_month_received = defaultdict(int)

    for i, friend1 in enumerate(friends):
        for friend2 in friends[i + 1 :]:
            if pair_gift_count[friend1][friend2] > pair_gift_count[friend2][friend1]:
                next_month_received[friend1] += 1
            elif pair_gift_count[friend1][friend2] < pair_gift_count[friend2][friend1]:
                next_month_received[friend2] += 1
            else:
                score1 = given[friend1] - received[friend1]
                score2 = given[friend2] - received[friend2]
                if score1 > score2:
                    next_month_received[friend1] += 1
                elif score1 < score2:
                    next_month_received[friend2] += 1

    return max(next_month_received.values(), default=0)


# 제출 코드
# def solution(friends, gifts):
#     note = {friend: {} for friend in friends}
#     for friend in friends:
#         note[friend]["history"] = {item: 0 for item in friends if friend != item}
#         note[friend]["given"] = 0
#         note[friend]["recieved"] = 0
#     for gift in gifts:
#         giver, reciever = gift.split(" ")
#         note[giver]["history"][reciever] += 1
#         note[giver]["given"] += 1
#         note[reciever]["recieved"] += 1

#     new_note = {friend: {} for friend in friends}
#     for friend in friends:
#         new_note[friend]["history"] = {item: 0 for item in friends if friend != item}
#         new_note[friend]["given"] = 0
#         new_note[friend]["recieved"] = 0

#     for idx1, friend1 in enumerate(friends):
#         for idx2 in range(idx1 + 1, len(friends)):
#             friend2 = friends[idx2]
#             if note[friend1]["history"][friend2] > note[friend2]["history"][friend1]:
#                 giver, reciever = friend1, friend2
#             elif note[friend1]["history"][friend2] < note[friend2]["history"][friend1]:
#                 giver, reciever = friend2, friend1
#             else:
#                 gift_index_friend1 = note[friend1]["given"] - note[friend1]["recieved"]
#                 gift_index_friend2 = note[friend2]["given"] - note[friend2]["recieved"]
#                 if gift_index_friend1 == gift_index_friend2:
#                     continue
#                 elif gift_index_friend1 > gift_index_friend2:
#                     giver, reciever = friend1, friend2
#                 else:
#                     giver, reciever = friend2, friend1

#             new_note[reciever]["history"][giver] += 1
#             new_note[giver]["recieved"] += 1
#             new_note[reciever]["given"] += 1

#     if not new_note:
#         return 0

#     result = max([note["recieved"] for note in new_note.values()])

#     return result


inputs_and_outputs = [
    # friends, gifts, result
    (
        ["muzi", "ryan", "frodo", "neo"],
        [
            "muzi frodo",
            "muzi frodo",
            "ryan muzi",
            "ryan muzi",
            "ryan muzi",
            "frodo muzi",
            "frodo ryan",
            "neo muzi",
        ],
        2,
    ),
    (
        ["joy", "brad", "alessandro", "conan", "david"],
        [
            "alessandro brad",
            "alessandro joy",
            "alessandro conan",
            "david alessandro",
            "alessandro david",
        ],
        4,
    ),
    (["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"], 0),
]
