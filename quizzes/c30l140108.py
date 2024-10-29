# https://school.programmers.co.kr/learn/courses/30/lessons/140108


def solution(s):
    count = 0
    idx = 0

    while idx < len(s):
        first = s[idx]
        first_count = 1
        other_count = 0
        idx = idx + 1

        while idx < len(s) and first_count != other_count:
            if s[idx] == first:
                first_count = first_count + 1
            else:
                other_count = other_count + 1
            idx = idx + 1

        count = count + 1

    return count


# # 알파벳 별로 각각 카운트 하는 solution()
# def solution(s):
#     result = 0
#     count_dict = {}
#     target = None
#     for chr in s:
#         if target is None:
#             target = chr

#         if chr in count_dict:
#             count_dict[chr] = count_dict[chr] + 1
#         else:
#             count_dict[chr] = 1
#         for key, value in count_dict.items():
#             if target != key and count_dict[target] == value:
#                 result = result + 1
#                 count_dict = {}
#                 target = None
#                 break

#     if count_dict:
#         result = result + 1

#     return result


inputs_and_outputs = [
    # s, result
    ("banana", 3),
    ("abracadabra", 6),
    ("aaabbaccccabba", 3),
    ("a", 1),
    ("ab", 1),
    ("abc", 2),
    ("aaabbcccdd", 2),
    ("aabbcddd", 3),
    ("aaaaaa", 1),
    ("aaaaabc", 1),
    ("aaabbcccab", 2),
    ("aaabbcccabc", 3),
    ("abcdefgh", 4),
    ("abcdefggabbc", 5),
    ("aaabbaccccabba", 3),
    ("aaabcdea", 1),  # 🚨 제출한 코드의 정답: 2
]
