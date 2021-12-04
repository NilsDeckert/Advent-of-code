import re

import numpy
import numpy as np

DUMMY = 0.1


def parse_input(file: str) -> (list, list):
    with open(file, "r") as f:
        b = f.readlines()
        nums = [int(num) for num in b[0].split(",")]
        a = np.zeros((5, 5))
        boards = []
        counter = 0
        for line in b[2:]:
            b = re.split(r" +", line.strip())
            if b[0] != "":
                c = [int(i) for i in b]
                a[counter] = c
                counter += 1
            else:
                boards.append(a)
                a = np.zeros((5, 5))
                counter = 0
        boards.append(a)
        return nums, boards


def win(board: numpy.ndarray, winning_number: int) -> int:
    board[board == DUMMY] = 0
    sum = board.sum()
    return int(sum * winning_number)


def main(file: str) -> int:
    nums, boards = parse_input(file)
    finished = np.zeros(len(boards))

    for i in nums:
        for j, board in enumerate(boards):
            # Board already won
            if finished[j] == 1:
                continue
            board[board == i] = DUMMY

            for row in board:
                if np.all(row == DUMMY):
                    finished[j] = 1
                    # Board is last one to finish
                    if np.count_nonzero(finished) == len(boards):
                        return win(board, i)
                    continue

            for column in board.T:
                if np.all(column == DUMMY):
                    finished[j] = 1
                    # Board is last one to finish
                    if np.count_nonzero(finished) == len(boards):
                        return win(board, i)
                    continue


if __name__ == '__main__':
    print(main('input.txt'))
