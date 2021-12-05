import numpy as np
from collections import Counter


def parse_input(file: str) -> list[tuple]:
    lines = []
    with open(file, "r") as f:
        for line in f:
            num_a, num_b = line.strip().split(" -> ")
            x_a, y_a = int(num_a.split(",")[0]), int(num_a.split(",")[1])
            x_b, y_b = int(num_b.split(",")[0]), int(num_b.split(",")[1])
            a = np.array([x_a,
                          y_a])
            b = np.array([x_b,
                          y_b])

            lines.append((a, b))
    return lines


def count_occurrences(l: list) -> int:
    res = Counter(l)
    new_dict = dict(filter(lambda elem: elem[1] > 1, res.items()))  # Filter arrays that occur more than once
    print(new_dict)
    return len(new_dict)


def main(file: str) -> int:
    lines = parse_input(file)
    hit = []
    for line in lines:
        start = line[0]
        end = line[1]

        if start[0] == end[0]:  # x_a == x_b
            if end[1] > start[1]:
                y = np.arange(start[1], end[1] + 1, 1, dtype=int)
            else:
                y = np.arange(end[1], start[1] + 1, 1, dtype=int)

            for y_i in y:
                hit.append((start[0], y_i))

        elif start[1] == end[1]:  # y_a == y_b
            if end[0] > start[0]:
                x = np.arange(start[0], end[0] + 1, 1, dtype=int)
            else:
                x = np.arange(end[0], start[0] + 1, 1, dtype=int)

            for x_i in x:
                hit.append((x_i, start[1]))
        else:  # 45 Degree angle

            if end[1] > start[1]:
                y = np.arange(start[1], end[1] + 1, 1, dtype=int)
            else:
                y = np.arange(end[1], start[1] + 1, 1, dtype=int)
                y = y[::-1]

            if end[0] > start[0]:
                x = np.arange(start[0], end[0] + 1, 1, dtype=int)
            else:
                x = np.arange(end[0], start[0] + 1, 1, dtype=int)
                x = x[::-1]

            for i in range(len(x)):
                hit.append((x[i], y[i]))

    return count_occurrences(hit)


if __name__ == '__main__':
    print(main('input.txt'))
