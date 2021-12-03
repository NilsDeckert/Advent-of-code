def main(file: str) -> int:
    with open(file, "r") as f:
        nums = [str(line).strip() for line in f]

    bits = len(nums[0])
    gamma, epsilon = "", ""

    for i in range(bits):
        count = 0
        for number in nums:
            if number[i] == "1":
                count += 1

        if count > len(nums) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon


if __name__ == '__main__':
    print(main('input.txt'))
