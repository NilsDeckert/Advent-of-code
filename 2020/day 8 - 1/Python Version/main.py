lines = []

with open("input.txt", "r") as file:
    for line in file:
        lines.append(line.split(" "))

global accumulator
accumulator = 0
check = [0 for x in lines]
def work(line_num):
    if check[line_num] != 0:
        return 0
    check[line_num] = 1
    global accumulator
    print("acc: {}".format(accumulator))
    line = lines[line_num]
    print(line)
    command = line[0]
    arg = int(line[1])
    if command == "acc":
        accumulator += arg
        work(line_num+1)
    elif command == "jmp":
        work(line_num+arg)
    elif command == "nop":
        work(line_num+1)


work(0)
print(accumulator)
