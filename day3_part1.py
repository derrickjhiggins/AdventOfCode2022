priority = 0

with open("day3_input.txt") as f:
    lines = f.readlines()

    for line in lines:
        compartment_1, compartment_2 = line[0:len(line)//2], line[len(line)//2:]
        for char in compartment_1:
            if char in compartment_2:
                if char.isupper():
                    priority += (ord(char) - 38)
                    break
                else:
                    priority += (ord(char) - 96)
                    break

print(priority)