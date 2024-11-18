# https://school.programmers.co.kr/learn/courses/30/lessons/340213


def time_to_format(time: int):
    def pad(num: int):
        return f"{num}".rjust(2, "0")

    sec = time % 60
    min = int((time - sec) / 60)
    return f"{pad(min)}:{pad(sec)}"


def format_to_time(formatted: str):
    min, sec = [int(num) for num in formatted.split(":")]

    return min * 60 + sec


def move(time: int, move_value: int):
    return time + move_value


def solution(video_len, pos, op_start, op_end, commands):
    def get_move_value(video_len: int, pos: int, op_start: int, op_end: int, cmd):
        if cmd == "next":
            if op_start <= pos < op_end:
                return op_end - pos
            return 10 if video_len - pos > 10 else video_len - pos
        if cmd == "prev":
            return -10 if pos - 10 > 0 else -pos

    video_len, pos, op_start, op_end = [
        format_to_time(formatted)
        for formatted in [
            video_len,
            pos,
            op_start,
            op_end,
        ]
    ]

    if op_start <= pos < op_end:
        pos = op_end

    for command in commands:
        move_value = get_move_value(video_len, pos, op_start, op_end, command)
        pos = move(pos, move_value)
        if op_start <= pos < op_end:
            pos = op_end

    if op_start <= pos < op_end:
        pos = op_end

    return time_to_format(pos)


inputs_and_outputs = [
    # # video_len, pos, op_start, op_end, commands, result
    ("34:33", "13:00", "00:55", "02:55", ["next", "prev"], "13:00"),
    ("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"], "06:55"),
    ("07:22", "04:05", "00:15", "04:07", ["next"], "04:17"),
    ("59:59", "00:01", "00:05", "00:15", ["next"], "00:15"),
    ("59:59", "01:01", "00:05", "00:15", ["prev"], "00:51"),
    ("59:59", "59:59", "00:05", "00:15", ["prev", "prev", "next"], "59:49"),
    ("30:00", "15:00", "15:10", "15:30", ["next", "next"], "15:40"),
]
