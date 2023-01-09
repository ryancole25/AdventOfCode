# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
instructions = []
for item in contents:
    instructions.append(item.strip('\n'))

# Split the text of the instructions from the numbers
numbers = []
texts = []
for line in instructions:
    text, number = line.split()
    texts.append(text)
    numbers.append(number)

# Main function for evaluating depth and horizontal position
def main():
    x, y = 0, 0
    for i in range(len(texts)):
        if texts[i] == 'forward':
            x += int(numbers[i])
        elif texts[i] == 'up':
            y -= int(numbers[i])
        elif texts[i] == 'down':
            y += int(numbers[i])
        # print(f'{texts[i]} {numbers[i]}')
        # print(f'x: {x}  y: {y}')

    print(f'Part 1: Horizontal x Vertical = {x * y}')


main()

# ----------------------------------------------------------------------------------------
# PART 2

def main2():
    x, y, aim = 0, 0, 0
    for i in range(len(texts)):
        if texts[i] == 'forward':
            x += int(numbers[i])
            y += aim * int(numbers[i])
        elif texts[i] == 'up':
            aim -= int(numbers[i])
        elif texts[i] == 'down':
            aim += int(numbers[i])

    print(f'Part 2: Horizontal x Vertical = {x * y}')

main2()