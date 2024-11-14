# https://school.programmers.co.kr/learn/courses/30/lessons/92334

import copy


def solution(id_list, report, k):
    memo = {}
    report_dict = {id: copy.deepcopy([]) for id in id_list}
    for id in id_list:
        filtered = [_id for _id in id_list if _id != id]
        memo[id] = {k: v for k, v in zip(filtered, [False] * (len(filtered)))}

    for item in report:
        from_id, to_id = item.split(" ")
        if not memo[from_id][to_id]:
            report_dict[to_id].append(from_id)
            memo[from_id][to_id] = True

    result_dict = {k: v for k, v in zip(id_list, [0] * len(id_list))}
    for id in id_list:
        if k <= len(report_dict[id]):
            for _id in report_dict[id]:
                result_dict[_id] += 1

    result = []
    for id in id_list:
        result.append(result_dict[id])

    return result


inputs_and_outputs = [
    # id_list, report, k, result
    (
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
        [2, 1, 1, 0],
    ),
    (["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3, [0, 0]),
]
