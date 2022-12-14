priority = 0

with open("day3_input.txt") as f:
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()

        for char in line1:
            if char in line2 and char in line3:
                if char.isupper():
                    priority += (ord(char) - 38)
                    break
                else:
                    priority += (ord(char) - 96)
                    break

        if line3 == "":
            break

print(priority)

testing push