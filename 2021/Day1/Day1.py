# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
depths = []
for item in contents:
    depths.append(item.strip('\n'))

# Main function to count when depth increased or decreased
def main():
    increased = 0
    decreased = 0
    for i in range(len(depths) - 1):
        if int(depths[i]) < int(depths[i + 1]):
            increased += 1
        elif int(depths[i]) < int(depths[i + 1]):
            decreased += 1
    print(f'Part 1: {increased} increases')

main()

# ----------------------------------------------------------------------------------------
# PART 2

def main2():
    increased = 0
    decreased = 0
    for i in range(len(depths) - 3):
        if int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2]) < int(depths[i + 1]) + int(depths[i + 2]) + int(depths[i + 3]):
            increased += 1
        elif int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2]) < int(depths[i + 1]) + int(depths[i + 2]) + int(depths[i + 3]):
            decreased += 1
    print(f'Part 2: {increased} increases')

main2()