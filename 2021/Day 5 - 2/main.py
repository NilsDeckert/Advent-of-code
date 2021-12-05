import numpy as np
from collections import Counter


def parse_input(file: str) -> list[tuple]:
    lines = []
    with open(file, "r") as f:
        for line in f:
            num_a, num_b = line.strip().split(" -> ")
            x_a, y_a = [int(a) for a in num_a.split(",")]
            x_b, y_b = [int(b) for b in num_b.split(",")]

            a = np.array([x_a, y_a])
            b = np.array([x_b, y_b])

            lines.append((a, b))
    return lines


def count_occurrences(l: list) -> int:
    res = Counter(l)
    new_dict = dict(filter(lambda elem: elem[1] > 1, res.items()))  # Filter arrays that occur more than once
    return len(new_dict)


def main(file: str) -> int:
    lines = parse_input(file)
    hit = []
    for line in lines:

        x_a, y_a = line[0][0], line[0][1]
        x_b, y_b = line[1][0], line[1][1]

        # Either x or y value is the same, so use np.arange for the other value to get all points inbetween
        if x_a == x_b:
            a, b = y_a, y_b
        elif y_a == y_b:
            a, b = x_a, x_b

        # Make sure np.arange works properly
        if b < a:
            b, a = a, b

        z = np.arange(a, b + 1, 1, dtype=int)

        if x_a == x_b:
            hit += [(x_a, y_i) for y_i in z]
        elif y_a == y_b:
            hit += [(x_i, y_a) for x_i in z]
        else:  # 45 Degree angle

            # flip 'direction' if x/y value of b is smaller than x/y of a
            x_n, y_n = 1, 1
            if y_b < y_a:
                y_n = -1
            if x_b < x_a:
                x_n = -1

            y = range(y_a, y_b + y_n, y_n)
            x = range(x_a, x_b + x_n, x_n)

            hit += [(x_i, y_i) for x_i, y_i in zip(x, y)]

    return count_occurrences(hit)


if __name__ == '__main__':
    print(main('input.txt'))
