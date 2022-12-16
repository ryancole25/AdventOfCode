# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and split the instruction from the number and store in a list
instructions = []
for item in contents:
    instructions.append(item.split())

# Test instructions
# instructions = [['noop'], ['addx', '3'], ['addx', '-5']]

def main():
    x = 1
    cycle = 0
    strength = 0
    for step in instructions:
        if step[0] == 'noop':
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                strength += cycle * x
        elif step[0] == 'addx':
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                strength += cycle * x
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                strength += cycle * x
            x += int(step[1])
        # print(f'Cycle: {cycle} \nx: {x} \nstrength: {strength}')

    print(f'Part 1 Answer: {strength}')
main()

# ----------------------------------------------------------------------------------------
# PART 2

# Draw a '#' when cycle and x overlap

# Go through each of the instructions
def main2():
    x = 1
    cycle = 0
    screen = '#'
    draw_screen(x, cycle, screen)

    for step in instructions:
        if step[0] == 'noop':
            cycle += 1
            screen = draw_screen(x, cycle, screen)
        elif step[0] == 'addx':
            cycle += 1
            screen = draw_screen(x, cycle, screen)
            cycle += 1
            x += int(step[1])
            screen = draw_screen(x, cycle, screen)

# Function for drawing either a '#' or a '.'
def draw_screen(x, cycle, screen):

    # Check for a new line and reset the screen for that line to be blank
    if cycle % 40 == 0 and cycle > 0:
        # print(f'{cycle}')
        print(screen)
        screen = ''

    # Check if the cycles are within 1 unit of x
    if cycle % 40 >= x - 1 and cycle % 40 <= x + 1:
        # print('HASH')
        screen += '#'

    # Cycles not within 1 unit of x and not a new line
    else:
        screen += '.'
        # print('DOT')
    return screen

print('Part 2 Answer:')
main2()