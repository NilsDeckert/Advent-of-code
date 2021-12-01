def main(file: str) -> int:
    with open(file, 'r') as f:
        nums = [int(l) for l in f.readlines()]

    last = nums[0]
    counter = 0

    for i in nums:
        if i > last:
            counter += 1
        last = i

    return counter


if __name__ == '__main__':
    print(main('input.txt'))
