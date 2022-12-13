# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
list = []
for item in contents:
    list.append(item.strip('\n'))

# Test list
# list = ['00000','00000', '10000', '00000']

# Checks to see if the tree is on the edge
def check_edges(row, tree):
    if int(row) == 0 or int(row) == len(list) - 1:
        return True
    elif int(tree) == 0 or int(tree) == len(list[0]) - 1:
        return True
    else:
        return False

# Checks the trees to the left
def check_left(row, tree):
    t = -1
    while tree + t >= 0:
        if int(list[row][tree]) > int(list[row][tree + t]):
            t += -1
            continue
        else:
            return False
    return True

# Checks the trees to the right
def check_right(row, tree):
    t = 1
    while tree + t < len(list[0]):
        if int(list[row][tree]) > int(list[row][tree + t]):
            t += 1
            continue
        else:
            return False
    return True

# Checks the trees above
def check_above(row, tree):
    t = -1
    while row + t >= 0:
        if int(list[row][tree]) > int(list[row + t][tree]):
            t += -1
            continue
        else:
            return False
    return True

# Checks the trees below
def check_below(row, tree):
    t = 1
    while row + t < len(list):
        if int(list[row][tree]) > int(list[row + t][tree]):
            t += 1
            continue
        else:
            return False
    return True

# Main function that tests edges, then left, then right, then above, then below
def main(list):
    visible_trees = 0
    for i in range(0, len(list)):
        for j in range(0, len(list[0])):
            # Check for edges
            if check_edges(i, j):
                visible_trees += 1
                continue
            elif check_left(i,j):
                visible_trees += 1
                continue
            elif check_right(i,j):
                visible_trees += 1
                continue
            elif check_above(i,j):
                visible_trees += 1
                continue
            elif check_below(i,j):
                visible_trees += 1
                continue
    return print(f'Part 1: There are {visible_trees } visible trees')

main(list)

# ----------------------------------------------------------------------------------------
# PART 2
# Get a scenic score for each tree

def above_distance(row, tree):
    # Check if the tree is on the top row
    if row == 0:
        return 1
    else:
        distance = 1
        while int(list[row][tree]) > int(list[row - distance][tree]) and row - distance >= 0:
            # Check if you hit the edge
            if row - distance == 0:
                return distance
            distance += 1
        return distance

def below_distance(row, tree):
    # Check if the tree is on the top row
    if row == int(row) == len(list) - 1:
        return 1
    else:
        distance = 1
        while int(list[row][tree]) > int(list[row + distance][tree]) and row + distance < len(list):
            # Check if you hit the edge
            if row + distance == len(list) - 1:
                return distance
            distance += 1
        return distance

def left_distance(row, tree):
    # Check if the tree is on the left side
    if tree == 0:
        return 1
    else:
        distance = 1
        while int(list[row][tree]) > int(list[row][tree - distance]) and tree - distance >= 0:
            # Check if you hit the edge
            if tree - distance == 0:
                return distance
            distance += 1
        return distance

def right_distance(row, tree):
    # Check if the tree is on the left side
    if tree == len(list[0]) - 1:
        return 1
    else:
        distance = 1
        while int(list[row][tree]) > int(list[row][tree + distance]) and tree + distance < len(list[0]):
            # Check if you hit the edge
            if tree + distance == len(list[0]) - 1:
                return distance
            distance += 1
        return distance

def main2(list):
    tree_scores = []
    for i in range(0, len(list)):
        for j in range(0, len(list[0])):
            up = above_distance(i,j)
            # print(up)
            down = below_distance(i,j)
            # print(down)
            left = left_distance(i,j)
            # print(left)
            right =right_distance(i,j)
            #print(right)

            # Store the tree scores in a list
            tree_scores.append(up * down * left * right)
    return print(f'Part 2: The highest scenic score is {max(tree_scores)}')
main2(list)