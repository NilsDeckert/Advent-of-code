def filter_bits(nums: list[str], b: bool) -> int:
    bits = len(nums[0])
    for i in range(bits):
        temp = []
        count = 0

        for number in nums:
            if number[i] == "1":
                count += 1

        if count >= len(nums) / 2:  # Mehrheit 1
            for n in nums:
                if (b and n[i] == "1") or (not b and n[i] == "0"):
                    temp.append(n)

        else:  # Mehrheit 0
            for n in nums:
                if (b and n[i] == "0") or (not b and n[i] == "1"):
                    temp.append(n)

        nums = temp
        if len(nums) == 1:
            return int(nums[0], 2)


def main(file: str) -> int:
    with open(file, "r") as f:
        nums = [str(line).strip() for line in f]

    oxygen = filter_bits(nums, True)
    c02 = filter_bits(nums, False)
    return oxygen * c02


if __name__ == '__main__':
    print(main('input.txt'))
