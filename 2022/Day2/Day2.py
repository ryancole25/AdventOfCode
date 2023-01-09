# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
list = []
for game in contents:
    list.append(game.strip())

print(list)

# Create the game

# A, X- ROCK
# B, Y- PAPER
# C, Z - SCISSORS

score = 0
for game in list:
    # I choose rock
    if game[2] == 'X':
        score += 1
        if game[0] == 'A':
            score += 3
        if game[0] == 'C':
            score += 6

    # I choose paper
    if game[2] == 'Y':
        score += 2
        if game[0] == 'A':
            score += 6
        if game[0] == 'B':
            score += 3

    # I choose scissors
    if game[2] == 'Z':
        score += 3
        if game[0] == 'B':
            score += 6
        if game[0] == 'C':
            score += 3

print(score)

# ----------------------------------------------------------------------------------------
# PART 2

# A - ROCK
# B - PAPER
# C - SCISSORS

# X - LOSE
# Y - DRAW
# Z - WIN

score2 = 0
for game in list:
    # Need to lose the game
    if game[2] == 'X':
        score2 += 0
        if game[0] == 'A':
            score2 += 3
        if game[0] == 'B':
            score2 += 1
        if game[0] == 'C':
            score2 += 2

    # Need to tie the game
    if game[2] == 'Y':
        score2 += 3
        if game[0] == 'A':
            score2 += 1
        if game[0] == 'B':
            score2 += 2
        if game[0] == 'C':
            score2 += 3

    # Need to win the game
    if game[2] == 'Z':
        score2 += 6
        if game[0] == 'A':
            score2 += 2
        if game[0] == 'B':
            score2 += 3
        if game[0] == 'C':
            score2 += 1

print(score2)