def main(file: str) -> int:
    horizontal, depth, aim = 0, 0, 0

    with open(file, "r") as f:
        for line in f:
            (direction, value) = line.split(" ")
            value = int(value)
            if direction == "down":
                aim += value
            elif direction == "up":
                aim -= value
            else:
                horizontal += value
                depth += aim * value

    return horizontal * depth


if __name__ == '__main__':
    print(main('input.txt'))
