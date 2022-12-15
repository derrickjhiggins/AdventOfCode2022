import re

# stacks dict:
#   each key is stack #
#   bottom of stack is index [0], top of stack is index [-1]
# instructions = [move quantity, moving_from stack, moving_to stack]

# TODO: How can I read the input txt file to create stacks dict rather than manually creating

stacks = {
    1: ["F", "C", "J", "P", "H", "T", "W"],
    2: ["G", "R", "V", "F", "Z", "J", "B", "H"],
    3: ["H", "P", "T", "R"],
    4: ["Z", "S", "N", "P", "H", "T"],
    5: ["N", "V", "F", "Z", "H", "J", "C", "D"],
    6: ["P", "M", "G", "F", "W", "D", "Z"],
    7: ["M", "V", "Z", "W", "S", "J", "D", "P"],
    8: ["N", "D", "S"],
    9: ["D", "Z", "S", "F", "M"]
}

with open("day5_part1_input.txt") as f:
    # skip first lines of text file containing stack schematic
    lines = f.readlines()[10:]
    for line in lines:
        # search for integers in each line, storing as instructions list
        # set variables for move_from and move_to boxes from instructions list
        instructions = [int(box) for box in re.findall(r'\b\d+\b', line)]
        move_from = instructions[1]
        move_to = instructions[2]

        # move specified quantity from top of move from to top of move to
        for i in range(instructions[0]):
            stacks[move_to].append(stacks[move_from][-1])
            del stacks[move_from][-1]

# print resulting string containing top of each stack
final = ""
for stack in stacks:
    final += stacks[stack][-1]
print(final)