# https://school.programmers.co.kr/learn/courses/30/lessons/133499


def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]

    count = 0
    for babble in babbling:
        idx = 0
        previous = available = None
        while idx < len(babble) and available is None:
            for word in words:
                if babble[idx:].startswith(word):
                    if previous == word:
                        available = False
                    else:
                        previous = word
                        idx = idx + len(word)
                        if idx == len(babble):
                            available = True
                    break
            else:
                break

        if available == True:
            count = count + 1

    return count


inputs_and_outputs = [
    # babbling, result
    (["aya", "yee", "u", "maa"], 1),
    (["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"], 2),
]
