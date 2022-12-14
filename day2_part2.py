# A/X = ROCK = 1
# B/Y = PAPER = 2
# C/Z = SCISSORS = 3
# LOSE(X) = 0
# DRAW(Y) = 3
# WIN(Z) = 6

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
        if p2 == "A": # need loss
            if p1 == "A": #scissors loses to rock
                match_points += 3
            elif p1 == "B": #rock loses to paper
                match_points += 1
            else: #paper loses to scissors
                match_points += 2
        elif p2 == "B": #need draw
            match_points += 3
            if p1 == "A":
                match_points += 1
            elif p1 == "B":
                match_points += 2
            else:
                match_points += 3
        else: #need win
            match_points += 6
            if p1 == "A": #paper beats rock
                match_points += 2
            elif p1 == "B": #scissors beats paper
                match_points += 3
            else: #rock beats scissors
                match_points += 1

        # add match points to points total
        points_total += match_points

print(points_total)
