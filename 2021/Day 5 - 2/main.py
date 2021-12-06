import numpy as np
from collections import Counter


def parse_input(file: str) -> list[tuple]:
    lines = []
    with open(file, "r") as f:
        for line in f:
            num_a, num_b = line.strip().split(" -> ")
            a = np.array([int(a) for a in num_a.split(",")])
            b = np.array([int(b) for b in num_b.split(",")])

            lines.append((a, b))
    return lines


def count_occurrences(l: list) -> int:
    res = Counter(l)
    new_dict = dict(filter(lambda elem: elem[1] > 1, res.items()))  # Filter arrays that occur more than once
    return len(new_dict)


def main(file: str) -> int:
    lines = parse_input(file)
    hit = []
    # returns 1 if a < b; -1 if a > b; 0 else
    f = lambda a, b: int(a < b) - int(a > b)
    for line in lines:

        (x_a, y_a), (x_b, y_b) = line

        # Either x or y value is the same, so use range() for the other value to get all points inbetween
        a, b = [(y_a, y_b), (x_a, x_b)][int(y_a == y_b)]
        z = range(a, b + f(a, b), f(a, b))

        if x_a == x_b:
            hit += [(x_a, y_i) for y_i in z]
        elif y_a == y_b:
            hit += [(x_i, y_a) for x_i in z]
        else:  # 45 Degree angle

            y = range(y_a, y_b + f(y_a, y_b), f(y_a, y_b))
            x = range(x_a, x_b + f(x_a, x_b), f(x_a, x_b))

            hit += [(x_i, y_i) for x_i, y_i in zip(x, y)]

    return count_occurrences(hit)


if __name__ == '__main__':
    print(main('input.txt'))
