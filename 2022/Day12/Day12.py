# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
grid = []
for item in contents:
    grid.append(item.strip('\n'))

print(grid)

# Find the starting point and the finishing point
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            starting_point = [y, x]
        if grid[y][x] == 'E':
            finishing_point = [y, x]

print(starting_point)
print(finishing_point)

# Make sure you do not go back to the same square you have already been at
already_been = [starting_point]

def move():
    
