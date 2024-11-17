# https://school.programmers.co.kr/learn/courses/30/lessons/340198


def solution(mats, park):
    mats.sort(reverse=True)
    park_height = len(park)
    park_width = len(park[0])

    def can_place(mat_size, x, y):
        if x + mat_size > park_height or y + mat_size > park_width:
            return False
        for i in range(x, x + mat_size):
            for j in range(y, y + mat_size):
                if park[i][j] != "-1":
                    return False
        return True

    for mat_size in mats:
        for i in range(park_height):
            for j in range(park_width):
                if can_place(mat_size, i, j):
                    return mat_size
    return -1


# ❌ Wrong
# def solution(mats, park):
#     mats.sort()
#     mats.reverse()

#     park_width = len(park[0])
#     park_heigth = len(park)

#     current_max = -1
#     for h, row in enumerate(park):
#         if park_heigth - h < mats[-1]:
#             break
#         is_started = False
#         start = 0
#         availables = []
#         for w, item in enumerate(row):
#             if park_width - w < mats[-1]:
#                 break

#             if item == "-1" and not is_started:
#                 start = w
#                 is_started = True
#             elif item != "-1" and is_started:
#                 availables.append((start, w - 1))
#                 is_started = False

#         if is_started:
#             availables.append((start, w))
#             is_started = False

#         for w_start, w_end in availables:
#             for mat in mats:
#                 if mat == 1:
#                     current_max = max(current_max, mat)
#                     break
#                 elif mat <= (w_end - w_start + 1) and current_max == -1:
#                     rest_height = min(mat + h, park_heigth) - h - 1
#                     if rest_height < mat - 1:
#                         continue
#                     else:
#                         is_found = False
#                         for idx in range(w_start, w_end):
#                             is_unavailable = False
#                             for line in range(h + 1, min(mat + h, park_heigth)):
#                                 if is_unavailable == False and park[line][idx] != "-1":
#                                     is_unavailable = True
#                                     break
#                             if is_unavailable == False:
#                                 current_max = max(current_max, mat)
#                                 is_found = True
#                         if is_found == True:
#                             break
#     return current_max if current_max > 0 else -1


inputs_and_outputs = [
    # mats, park, result
    (
        [5, 3, 2],
        [
            ["A", "A", "-1", "B", "B", "B", "B", "-1"],
            ["A", "A", "-1", "B", "B", "B", "B", "-1"],
            ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
            ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
            ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ],
        3,
    ),
    (
        [1, 2, 3],
        [
            ["A", "-1", "-1"],
            ["-1", "-1", "B"],
            ["-1", "-1", "-1"],
        ],
        2,
    ),
    (
        [3],
        [
            ["-1", "-1", "-1"],
            ["-1", "-1", "-1"],
            ["-1", "-1", "A"],
        ],
        -1,
    ),
    (
        [3],
        [
            ["-1", "-1", "A"],
            ["-1", "-1", "-1"],
            ["-1", "-1", "-1"],
        ],
        -1,
    ),
]
