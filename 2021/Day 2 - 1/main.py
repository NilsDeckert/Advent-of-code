def main(file: str) -> int:
    horizontal, depth = 0, 0

    with open(file, "r") as f:
        for line in f:
            (direction, value) = line.split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
            elif direction == "down":
                depth += value
            else:
                depth -= value

    return horizontal * depth


if __name__ == '__main__':
    print(main('input.txt'))
