# https://school.programmers.co.kr/learn/courses/30/lessons/160586


def solution(keymap, targets):
    key_counts = {}
    for keys in keymap:
        for idx, key in enumerate(keys, 1):
            if key in key_counts:
                key_counts[key] = min(key_counts[key], idx)
            else:
                key_counts[key] = idx

    total = []
    for message in targets:
        count = 0
        for chr in message:
            if not chr in key_counts:
                count = -1
                break
            count += key_counts[chr]
        total.append(count)

    return total


inputs_and_outputs = [
    # keymap, targets, result
    (["ABACD", "BCEFD"], ["ABCD", "AABB"], [9, 4]),
    (["AA"], ["B"], [-1]),
    (["AGZ", "BSSS"], ["ASA", "BGZ"], [4, 6]),
]
