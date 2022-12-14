calorie_totals = {}

with open('input.txt') as f:
    counter = 0
    index = 0
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        if line == '':
            calorie_totals[index] = counter
            counter = 0
            index += 1
            continue

        counter += int(line)

max = 0
top_3 = [0, 0, 0]
for total in calorie_totals:
    if calorie_totals[total] > max:
        max = calorie_totals[total]
    for i in range(len(top_3)):
        if calorie_totals[total] > top_3[i]:
            temp = top_3[i]
            top_3[i] = calorie_totals[total]
            if i != 2:
                top_3[i+1] = temp
            break


print(top_3)
print(sum(top_3))
