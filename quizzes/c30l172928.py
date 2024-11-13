# https://school.programmers.co.kr/learn/courses/30/lessons/172928


def parse_map(park):
    park_map = []
    start_pos = (0, 0)
    for h, row in enumerate(park):
        row_data = []
        for w in range(0, len(row)):
            if row[w] == "X":
                row_data.append(False)
            elif row[w] == "O":
                row_data.append(True)
            elif row[w] == "S":
                row_data.append(True)
                start_pos = (h, w)
        park_map.append(row_data)
    return (park_map, start_pos)


def is_possible(to_pos, park_map, len_height, len_width):
    if (
        to_pos[0] < 0
        or to_pos[1] < 0
        or len_height <= to_pos[0]
        or len_width <= to_pos[1]
        or not park_map[to_pos[0]][to_pos[1]]
    ):
        return False
    return True


def solution(park, routes):
    (park_map, current) = parse_map(park)
    len_height = len(park_map)
    len_width = len(park_map[0])

    for route in routes:
        direction, distance = route.split(" ")
        distance = int(distance)
        h, w = current
        if direction == "N":
            to_pos = (h - distance, w)
        elif direction == "S":
            to_pos = (h + distance, w)
        elif direction == "E":
            to_pos = (h, w + distance)
        elif direction == "W":
            to_pos = (h, w - distance)

        if not is_possible(to_pos, park_map, len_height, len_width):
            continue

        flag = True
        if direction == "N":
            for move_h in range(to_pos[0], h):
                if flag and not park_map[move_h][w]:
                    flag = False
        elif direction == "S":
            for move_h in range(h, to_pos[0]):
                if flag and not park_map[move_h][w]:
                    flag = False
        elif direction == "E":
            for move_w in range(w, to_pos[1]):
                if flag and not park_map[h][move_w]:
                    flag = False
        elif direction == "W":
            for move_w in range(to_pos[1], w):
                if flag and not park_map[h][move_w]:
                    flag = False
        if flag:
            current = to_pos

    return list(current)


inputs_and_outputs = [
    # park, routes, result
    (["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"], [2, 1]),
    (["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"], [0, 1]),
    (["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"], [0, 0]),
]
