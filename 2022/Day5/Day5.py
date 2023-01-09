# PART 1

# [S]                 [T] [Q]
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9

# Create a function that will move the boxes
def movement(times, from_stack, to_stack):
    t = 0
    while t < times:
        stack[to_stack].append(stack[from_stack].pop())
        t += 1

# Create the stack as a dictionary
stack = {1: ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'], 2: ['T', 'B', 'M', 'Z', 'R'], 3: ['Z', 'L', 'C', 'H', 'N', 'S'], 4: ['S', 'C', 'F', 'J'],
         5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'], 6: ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'], 7: ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
         8: ['M', 'Z', 'R'], 9: ['M', 'C', 'L', 'G', 'V', 'R', 'T']}

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# Parse the instructions for the numbers
instructions = []
for row in contents:
    nums = ''
    for char in row:
        if char.isnumeric():
            nums += char
    instructions.append(nums[::-1])

# print(instructions)

for number in instructions:
    to_stack = number[0]
    from_stack = number[1]
    times = number[2:]
    # print(times[::-1], from_stack, to_stack)
    movement(int(times[::-1]), int(from_stack), int(to_stack))

print(stack)

# Return top character from each stack
print(f'Part 1 Answer: {stack[1][-1]}{stack[2][-1]}{stack[3][-1]}{stack[4][-1]}{stack[5][-1]}{stack[6][-1]}{stack[7][-1]}{stack[8][-1]}{stack[9][-1]}')

# ----------------------------------------------------------------------------------------
# PART 2

# Create the stack as a dictionary
stack2 = {1: ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'], 2: ['T', 'B', 'M', 'Z', 'R'], 3: ['Z', 'L', 'C', 'H', 'N', 'S'], 4: ['S', 'C', 'F', 'J'],
         5: ['P', 'G', 'H', 'W', 'R', 'Z', 'B'], 6: ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'], 7: ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
         8: ['M', 'Z', 'R'], 9: ['M', 'C', 'L', 'G', 'V', 'R', 'T']}


# Create a function that will move the boxes
def movement2(times, from_stack, to_stack):
    while times > 0:
        stack2[to_stack].append(stack2[from_stack].pop(len(stack2[from_stack]) - times))
        times += -1

# Get the numeric numbers from the instructions
for number in instructions:
    to_stack = number[0]
    from_stack = number[1]
    times = number[2:]
    # print(times[::-1], from_stack, to_stack)
    movement2(int(times[::-1]), int(from_stack), int(to_stack))

print(stack2)

# Return top character from each stack
print(f'Part 2 Answer: {stack2[1][-1]}{stack2[2][-1]}{stack2[3][-1]}{stack2[4][-1]}{stack2[5][-1]}{stack2[6][-1]}{stack2[7][-1]}{stack2[8][-1]}{stack2[9][-1]}')