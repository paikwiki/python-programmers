# https://school.programmers.co.kr/learn/courses/30/lessons/67256


def dist(pos_x, pos_y):
    return abs(pos_x[0] - pos_y[0]) + abs(pos_x[1] - pos_y[1])


def get_hand(hands, target, hand, keypad):
    left_dist = dist(keypad[hands["L"]], keypad[target])
    right_dist = dist(keypad[hands["R"]], keypad[target])

    if left_dist == right_dist:
        return hand

    return "L" if left_dist < right_dist else "R"


def solution(numbers, hand):
    keypad = {
        # fmt: off
         1 : [0,0],  2 : [0,1],  3 : [0,2],
         4 : [1,0],  5 : [1,1],  6 : [1,2],
         7 : [2,0],  8 : [2,1],  9 : [2,2],
        888: [3,0],  0 : [3,1], 999: [3,2],
    }
    converted_hand = "L" if hand == "left" else "R"
    hands = {"L": 888, "R": 999}

    result = ""
    for num in numbers:
        if num in [1, 4, 7]:
            h = "L"
        elif num in [3, 6, 9]:
            h = "R"
        else:
            h = get_hand(hands, num, converted_hand, keypad)
        result += h
        hands[h] = num

    return result


inputs_and_outputs = [
    # numbers, hand, result
    ([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"),
    ([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left", "LRLLRRLLLRR"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right", "LLRLLRLLRL"),
]
