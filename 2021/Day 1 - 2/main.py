def main(file: str) -> int:
    with open(file, 'r') as f:
        nums = [int(l) for l in f.readlines()]

    last = sum(nums[0:3])
    counter = 0

    for i in range(len(nums) - 2):
        s = sum(nums[i:i + 3])
        if s > last:
            counter += 1

        last = s

    return counter


if __name__ == '__main__':
    print(main('input.txt'))
