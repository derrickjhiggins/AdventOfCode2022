fully_contained = 0

with open("day4_part1_input.txt") as f:
    lines = f.readlines()

    # for each line in line:
        # strip new line character
        # set variables for first start/end index and second start/end index

    for line in lines:
        line = line.strip("\n")
        first_pair, second_pair = line.split(",")
        first_start_index, first_end_index = first_pair.split("-")
        second_start_index, second_end_index = second_pair.split("-")

        # if first pair fully contains second pair:
            # increment fully_contained sum by 1
        # elif second pair fully contains first pair:
            # increment fully_contained sum by 1
        if int(first_start_index) <= int(second_start_index) <= int(second_end_index) <= int(first_end_index):
            fully_contained += 1
        elif int(second_start_index) <= int(first_start_index) <= int(first_end_index) <= int(second_end_index):
            fully_contained += 1

print(fully_contained)