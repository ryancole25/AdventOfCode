# Part 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
instructions = []
for item in contents:
    instructions.append(item.strip('\n'))

# Test instructions
# instructions = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']


# Get the numbers from the instructions to determine the distance the head needs to move
distance = []
placeholder = ''
for item in instructions:
    placeholder = ''
    for char in item:
        if char.isnumeric():
            placeholder += char
    distance.append(int(placeholder))


# Loop through the instructions
# Coordinate system with x and y will determine which direction the head moves
def main():
    head_position = [0, 0]
    tail_position = [0, 0]
    tail_locations = []

    for i in range(len(instructions)):
        x = 0
        y = 0
        if instructions[i][0] == 'R':
            x = 1
        elif instructions[i][0] == 'L':
            x = -1
        elif instructions[i][0] == 'U':
            y = 1
        elif instructions[i][0] == 'D':
            y = -1

        tail_locations += move_head(head_position,tail_position, distance[i], x, y)

    formatted_tail_locations = []
    for i in range(0, len(tail_locations)-1, 2):
        formatted_tail_locations.append(tail_locations[i:i+2])
    # print(formatted_tail_locations)

    duplicates = []
    for coordinates in formatted_tail_locations:
        if coordinates not in duplicates:
            duplicates.append(coordinates)
    print(f'Tail unique locations: {duplicates}')
    print(f'Part 1 Answer: {len(duplicates)}')

# Moves the head one step at a time
def move_head(head_position, tail_position, distance, x, y):
    locations = []
    while distance > 0:
        distance += -1
        head_position[0] += x
        head_position[1] += y
        # print(f'Head Pos: {head_position}')
        tail_position = move_tail(tail_position, head_position, x, y)
        # print(f'Tail Pos: {tail_position}')
        locations += tail_position
    # print(f'Head: {head_position}')
    # print(f'Tail: {tail_position}')
    # print(f'Tail locations: {locations}')
    return locations

# The tail moves after the head and follows one step behind
def move_tail(tail_position, head_position, x, y):
    # Deal with diagonal
    if head_position[0] != tail_position[0] and head_position[1] != tail_position[1]:

        if head_position[0] == tail_position[0] + (2 * x):
            tail_position[0] += x
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            elif head_position[1] < tail_position[1]:
                tail_position[1] -= 1

        elif head_position[1] == tail_position[1] + (2 * y):
            tail_position[1] += y
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            elif head_position[0] < tail_position[0]:
                tail_position[0] -= 1

    # Deal with head 2 spaces away in either x or y direction
    elif head_position[0] == tail_position[0] + (2 * x) and x != 0:
        tail_position[0] += x
    elif head_position[1] == tail_position[1] + (2 * y) and y != 0:
        tail_position[1] += y
    return tail_position

main()

# ----------------------------------------------------------------------------------------
# PART 2
# 10 knots in the string

# Test 2 instructions
# instructions = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']

# Main function that takes in the instructions and prints the answer
def main2():
    head2_position = [0, 0]
    tail_position_1 = [0, 0]
    tail_position_2 = [0, 0]
    tail_position_3 = [0, 0]
    tail_position_4 = [0, 0]
    tail_position_5 = [0, 0]
    tail_position_6 = [0, 0]
    tail_position_7 = [0, 0]
    tail_position_8 = [0, 0]
    tail_position_9 = [0, 0]

    tail_locations_9 = []

    for i in range(len(instructions)):
        x = 0
        y = 0
        if instructions[i][0] == 'R':
            x = 1
        elif instructions[i][0] == 'L':
            x = -1
        elif instructions[i][0] == 'U':
            y = 1
        elif instructions[i][0] == 'D':
            y = -1
        # print(f'\n{instructions[i]}')

        tail_locations_9 += move2_head(head2_position, tail_position_1, tail_position_2, tail_position_3, tail_position_4, tail_position_5, tail_position_6, tail_position_7, tail_position_8, tail_position_9, distance[i], x, y)

    formatted_tail_locations2 = []
    for i in range(0, len(tail_locations_9)-1, 2):
        formatted_tail_locations2.append(tail_locations_9[i:i+2])
    # print(formatted_tail_locations)

    duplicates2 = []
    for coordinates in formatted_tail_locations2:
        if coordinates not in duplicates2:
            duplicates2.append(coordinates)
    print(f'Tail 9 unique locations: {duplicates2}')
    print(f'Part 2 Answer: {len(duplicates2)}')

def move2_head(head2_position, tail_position_1, tail_position_2, tail_position_3, tail_position_4, tail_position_5, tail_position_6, tail_position_7, tail_position_8, tail_position_9, distance, x, y):
    locations2 = []
    while distance > 0:
        distance += -1
        head2_position[0] += x
        head2_position[1] += y
        # print(f'Head Pos: {head2_position}')
        move2_tail(tail_position_1, head2_position, x, y)
        # print(f'Tail Pos 1: {tail_position_1}')
        move2_tail(tail_position_2, tail_position_1, x, y)
        # print(f'Tail Pos 2: {tail_position_2}')
        move2_tail(tail_position_3, tail_position_2, x, y)
        # print(f'Tail Pos 3: {tail_position_3}')
        move2_tail(tail_position_4, tail_position_3, x, y)
        # print(f'Tail Pos 4: {tail_position_4}')
        move2_tail(tail_position_5, tail_position_4, x, y)
        # print(f'Tail Pos 5: {tail_position_5}')
        move2_tail(tail_position_6, tail_position_5, x, y)
        # print(f'Tail Pos 6: {tail_position_6}')
        move2_tail(tail_position_7, tail_position_6, x, y)
        # print(f'Tail Pos 7: {tail_position_7}')
        move2_tail(tail_position_8, tail_position_7, x, y)
        # print(f'Tail Pos 8: {tail_position_8}')
        tail_positions_9 = move2_tail(tail_position_9, tail_position_8, x, y)
        # print(f'Tail Pos 9: {tail_position_9}')

        locations2 += tail_positions_9
    # print(f'Head: {head2_position}')
    # print(f'Tail locations: {locations}')
    return locations2

 # The tail moves after the head and follows one step behind
def move2_tail(tail_position, head_position, x, y):
    # Deal with diagonal
    if head_position[0] != tail_position[0] and head_position[1] != tail_position[1]:

        # positive x direction
        if head_position[0] == tail_position[0] + 2:
            tail_position[0] += 1
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            elif head_position[1] < tail_position[1]:
                tail_position[1] -= 1
        # negative x direction
        elif head_position[0] == tail_position[0] - 2:
            tail_position[0] += -1
            if head_position[1] > tail_position[1]:
                tail_position[1] += 1
            elif head_position[1] < tail_position[1]:
                tail_position[1] -= 1

        # positive y direction
        elif head_position[1] == tail_position[1] + 2:
            tail_position[1] += 1
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            elif head_position[0] < tail_position[0]:
                tail_position[0] -= 1

        # negative y direction
        elif head_position[1] == tail_position[1] -2:
            tail_position[1] += -1
            if head_position[0] > tail_position[0]:
                tail_position[0] += 1
            elif head_position[0] < tail_position[0]:
                tail_position[0] -= 1

    # Deal with head 2 spaces away in either x or y direction

    # positive x
    elif head_position[0] == tail_position[0] + 2:
        tail_position[0] += 1
    # negative x
    elif head_position[0] == tail_position[0] - 2:
        tail_position[0] += -1
    # positive y
    elif head_position[1] == tail_position[1] + 2:
        tail_position[1] += 1
    # negative y
    elif head_position[1] == tail_position[1] - 2:
        tail_position[1] += -1
    return tail_position

main2()