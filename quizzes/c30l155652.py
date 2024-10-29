# https://school.programmers.co.kr/learn/courses/30/lessons/155652


def solution(s, skip, index):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for skip_chr in skip:
        alphabets = alphabets.replace(skip_chr, "")

    replaced_len = len(alphabets)
    result = ""
    for s_chr in s:
        result += alphabets[(alphabets.index(s_chr) + index) % replaced_len]

    return result


inputs_and_outputs = [
    # s, skip, index, result
    ("aukks", "wbqd", 5, "happy"),
]
