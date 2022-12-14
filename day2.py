# A/X = ROCK = 1
# B/Y = PAPER = 2
# C/Z = SCISSORS = 3
# LOSE = 0
# DRAW = 3
# WIN = 6

with open("day2_input.txt") as f:
    lines = f.readlines()
    points_total = 0

    # iterate through file lines
    # set
    for line in lines:
        match_points = 0
        line = line.strip().replace(" ", "")
        line = line.replace("X", "A").replace("Y", "B").replace("Z", "C")
        p1 = line[0]
        p2 = line[1]

        # add points for letter chosen by p2
        if p2 == "A":
            match_points += 1
        elif p2 == "B":
            match_points += 2
        else:
            match_points += 3



        # check for draw
        if p1 == p2:
            match_points += 3
        # check for p2 win
        elif (p2 == 'A' and p1 == 'C') or (p2 == 'B' and p1 == 'A') or (p2 == 'C' and p1 == 'B'):
            match_points += 6

        # add match points to points total
        points_total += match_points


print(points_total)
