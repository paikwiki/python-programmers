# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    lux = luy = 51
    rdx = rdy = 0
    for x_idx in range(0, len(wallpaper)):
        for y_idx in range(0, len(wallpaper[0])):
            if wallpaper[x_idx][y_idx] == "#":
                lux, rdx = min(lux, x_idx), max(rdx, x_idx)
                luy, rdy = min(luy, y_idx), max(rdy, y_idx)

    return [lux, luy, rdx + 1, rdy + 1]


inputs_and_outputs = [
    # wallpaper, result
    ([".#...", "..#..", "...#."], [0, 1, 3, 4]),
    (
        ["..........", ".....#....", "......##..", "...##.....", "....#....."],
        [1, 3, 5, 8],
    ),
    (
        [
            ".##...##.",
            "#..#.#..#",
            "#...#...#",
            ".#.....#.",
            "..#...#..",
            "...#.#...",
            "....#....",
        ],
        [0, 0, 7, 9],
    ),
    (["..", "#."], [1, 0, 2, 1]),
]
