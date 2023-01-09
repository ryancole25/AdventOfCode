# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
binary = []
for item in contents:
    binary.append(item.strip('\n'))

# Function to convert binary into decimal
def binary_to_dec(number):
    decimal = 0
    power = len(number) - 1
    for char in number:
        decimal += int(char) * (2 ** power)
        power -= 1
    return decimal

# Main function to find the most common bit in each corresponding position
def main():
    gamma = ''
    epsilon = ''
    j = 0
    while j < len(binary[0]):
        sum_digit = 0
        for i in range(len(binary)):
            sum_digit += int(binary[i][j])
        if sum_digit > len(binary) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        j += 1

    gamma_dec = binary_to_dec(gamma)
    epsilon_dec = binary_to_dec(epsilon)

    print(f'Part 1: gamma x epsilon = {gamma_dec * epsilon_dec}')

main()

# ----------------------------------------------------------------------------------------
# PART 2

# binary = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

def oxygen_generator(binary, j):
    # Find the most common number
    digit = ''

    sum_digit = 0
    for i in range(len(binary)):
        sum_digit += int(binary[i][j])
    if sum_digit > len(binary) / 2:
        digit += '1'
    elif sum_digit < len(binary) / 2:
        digit += '0'
    else:
        digit += '1'

    # Eliminate the elements that do not have the most common number
    new_binary = []
    for number in binary:
        if number[j] == digit:
            new_binary.append(number)

    if len(new_binary) == 1:
        return binary_to_dec(new_binary[0])
    else:
        j += 1
        return oxygen_generator(new_binary, j)

def CO2_generator(binary, j):
    # Find the least common number
    digit = ''

    sum_digit = 0
    for i in range(len(binary)):
        sum_digit += int(binary[i][j])
    if sum_digit > len(binary) / 2:
        digit += '0'
    elif sum_digit < len(binary) / 2:
        digit += '1'
    else:
        digit += '0'

    # Eliminate the elements that do not have the most common number
    new_binary = []
    for number in binary:
        if number[j] == digit:
            new_binary.append(number)

    if len(new_binary) == 1:
        return binary_to_dec(new_binary[0])
    else:
        j += 1
        return CO2_generator(new_binary, j)

def main2():
    oxygen = oxygen_generator(binary, 0)
    CO2 = CO2_generator(binary, 0)
    print(f'Part 2: oxygen x CO2 = {oxygen * CO2}')


main2()