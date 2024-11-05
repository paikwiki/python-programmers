# https://school.programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    answerPoint = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "N": 0, "A": 0}
    mbtiPair = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]

    for question, answer in zip(survey, choices):
        [left, right] = [x for x in question]
        offset = answer - 4
        if offset > 0:
            answerPoint[right] += offset
        elif offset < 0:
            answerPoint[left] += offset * -1

    mbti = ""
    for first, second in mbtiPair:
        if answerPoint[first] == answerPoint[second]:
            mbti += first
            continue
        mbti += first if answerPoint[first] > answerPoint[second] else second

    return mbti


inputs_and_outputs = [
    # survey, choices, result
    (["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5], "TCMA"),
    (["TR", "RT", "TR"], [7, 1, 3], "RCJA"),
]
