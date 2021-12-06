import numpy as np
from collections import Counter
from datetime import datetime
from functools import cache

DUMMY = 0.1


def parse_input(file: str) -> np.ndarray:
    with open(file, "r") as f:
        for line in f:
            nums = [int(num) for num in line.strip().split(",")]
            continue

    return np.array(nums)


@cache
def count_single(c: int, days: int) -> int:
    if c >= days:
        return 1

    for i in range(days):
        c -= 1
        days -= 1
        if c == -1:
            return count_fish(np.array([6, 8]), days)


def count_fish(fish: np.ndarray, days: int) -> int:
    s = 0
    counted: dict = Counter(fish)
    for i in counted:
        s += counted[i] * count_single(i, days)
    return s


def main(file: str) -> (int, int):
    nums: np.ndarray = parse_input(file)
    t1 = datetime.now()

    val1 = count_fish(nums, 80)
    val2 = count_fish(nums, 256)

    t2 = datetime.now()
    print(t2 - t1)
    return val1, val2


if __name__ == '__main__':
    r1, r2 = main("input.txt")
    print("Part 1:" + str(r1))
    print("Part 2:" + str(r2))
