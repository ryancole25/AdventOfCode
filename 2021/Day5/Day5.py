# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
instructions = []
for item in contents:
    instructions.append(item.strip('\n'))

# Parse the instructions and convert into a usable form
temp_segment1 = []
temp_segment2 = []
for item in instructions:
    seg1, seg2  = item.split(' -> ')
    temp_segment1.append(seg1)
    temp_segment2.append(seg2)

# get usable segments and find the max values for the grid
segment1 = []
max_x = 0
max_y = 0
for item in temp_segment1:
    segx, segy = item.split(',')
    if max_x < int(segx):
        max_x = int(segx)
    if max_y < int(segy):
        max_y = int(segy)
    segment1.append([int(segx),int(segy)])

segment2 = []
for item in temp_segment2:
    segx, segy = item.split(',')
    if max_x < int(segx):
        max_x = int(segx)
    if max_y < int(segy):
        max_y = int(segy)
    segment2.append([int(segx),int(segy)])

# Make a grid of zeros to track the lines equal to the max coordinates from the input
grid = []
for i in range(max_y + 1):
    temp_grid = []
    for j in range(max_x + 1):
        temp_grid.append(0)
    grid.append(temp_grid)

def main():
    # Make the lines
    for i in range(len(segment1)):
        # Vertical line
        if segment1[i][0] == segment2[i][0]:
            vertical_line(segment1[i][0], segment2[i][0], segment1[i][1], segment2[i][1])
        elif segment1[i][1] == segment2[i][1]:
            horizontal_line(segment1[i][0], segment2[i][0], segment1[i][1], segment2[i][1])

    # Check for points with at least 2 overlap
    overlap = 0
    for i in range(len(grid)):
        # print(grid[i])
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                overlap += 1

    print(f'Part 1: {overlap}')


    # Check for points with at least 2 overlap
    overlap = 0

def vertical_line(x1, x2, y1, y2):
    if y2 > y1:
        grid[y1][x1] += 1
        while y2 > y1:
            y1 += 1
            grid[y1][x1] += 1
        return
    elif y2 < y1:
        grid[y1][x1] += 1
        while y2 < y1:
            y1 += -1
            grid[y1][x1] += 1
        return
    else:
        grid[y1][x1] += 1
        return

def horizontal_line(x1, x2, y1, y2):
    if x2 > x1:
        grid[y1][x1] += 1
        while x2 > x1:
            x1 += 1
            grid[y1][x1] += 1
        return
    elif x2 < x1:
        grid[y1][x1] += 1
        while x2 < x1:
            x1 += -1
            grid[y1][x1] += 1
        return
    else:
        grid[y1][x1] += 1
        return
main()

# Part 2 -------------------------------------------------------------------------------------------------------------------------------------------------

grid2 = []
for i in range(max_y + 1):
    temp_grid = []
    for j in range(max_x + 1):
        temp_grid.append(0)
    grid2.append(temp_grid)

def main2():
    # Make the lines
    for i in range(len(segment1)):
        # Vertical line
        if segment1[i][0] == segment2[i][0]:
            vertical_line2(segment1[i][0], segment2[i][0], segment1[i][1], segment2[i][1])
        elif segment1[i][1] == segment2[i][1]:
            horizontal_line2(segment1[i][0], segment2[i][0], segment1[i][1], segment2[i][1])
        elif segment1[i][0] != segment2[i][0] and segment1[i][1] != segment2[i][1]:
            diagonal_line2(segment1[i][0], segment2[i][0], segment1[i][1], segment2[i][1])

    # Check for points with at least 2 overlap
    overlap = 0
    for i in range(len(grid)):
        # print(grid2[i])
        for j in range(len(grid[i])):
            if grid2[i][j] > 1:
                overlap += 1

    print(f'Part 2: {overlap}')

# For diagonal lines (assume slope = +/- 1)
def diagonal_line2(x1, x2, y1, y2):
    # find if the slope is positive or negative
    slope = (y2 - y1) / (x2 - x1)

    if slope > 0:
        grid2[y1][x1] += 1
        if y2 - y1 < 0:
            while y2 < y1:
                y1 += -1
                x1 += -1
                grid2[y1][x1] += 1
            return
        elif y2 - y1 > 0:
            while y2 > y1:
                y1 += 1
                x1 += 1
                grid2[y1][x1] += 1
            return
    elif slope < 0:
        grid2[y1][x1] += 1
        if y2 - y1 < 0:
            while y2 < y1:
                y1 += -1
                x1 += 1
                grid2[y1][x1] += 1
            return
        elif y2 - y1 > 0:
            while y2 > y1:
                y1 += 1
                x1 += -1
                grid2[y1][x1] += 1
            return

def vertical_line2(x1, x2, y1, y2):
    if y2 > y1:
        grid2[y1][x1] += 1
        while y2 > y1:
            y1 += 1
            grid2[y1][x1] += 1
        return
    elif y2 < y1:
        grid2[y1][x1] += 1
        while y2 < y1:
            y1 += -1
            grid2[y1][x1] += 1
        return
    else:
        grid2[y1][x1] += 1
        return

def horizontal_line2(x1, x2, y1, y2):
    if x2 > x1:
        grid2[y1][x1] += 1
        while x2 > x1:
            x1 += 1
            grid2[y1][x1] += 1
        return
    elif x2 < x1:
        grid2[y1][x1] += 1
        while x2 < x1:
            x1 += -1
            grid2[y1][x1] += 1
        return
    else:
        grid2[y1][x1] += 1
        return

main2()