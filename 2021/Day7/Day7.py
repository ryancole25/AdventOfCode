# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# Make each fish an element in the list and convert into int
crabs = contents[0].split(',')
for i in range(len(crabs)):
    crabs[i] = int(crabs[i])

# crabs = [16,1,2,0,4,2,7,1,2,14]

def main():
    # Sort the crabs
    crabs.sort()
    # Find the approximate median of the numbers
    median_index = len(crabs) // 2

    fuel = 0
    for numbers in crabs:
        fuel += abs(numbers - crabs[median_index])

    # Check the right of the median until the fuel starts increasing
    i = 1
    while True:
        temp_fuel = 0
        for numbers in crabs:
            temp_fuel += abs(numbers - crabs[median_index] + i)

        if temp_fuel <= fuel:
            fuel = temp_fuel
            i += 1
            continue
        else:
            break

    # Check the left of the median until the fuel starts increasing
    i = -1
    while True:
        temp_fuel = 0
        for numbers in crabs:
            temp_fuel += abs(numbers - crabs[median_index] + i)

        if temp_fuel <= fuel:
            fuel = temp_fuel
            i += -1
            continue
        else:
            break
    print(f'Part 1: {fuel}')

main()

# Part 2 -------------------------------------------------------------------------------------------------------------------------------------------------

def main2():
    # Sort the crabs
    crabs.sort()
    # Find the approximate median of the numbers
    median_index = len(crabs) // 2

    fuel = 0
    for numbers in crabs:
        fuel += fuel_factor(abs(numbers - crabs[median_index]))

    # Check the right of the median until the fuel starts increasing
    i = 1
    while True:
        temp_fuel = 0
        for numbers in crabs:
            temp_fuel += fuel_factor(abs(numbers - crabs[median_index] + i))

        if temp_fuel <= fuel:
            fuel = temp_fuel
            i += 1
            continue
        else:
            break

    # Check the left of the median until the fuel starts increasing
    i = -1
    while True:
        temp_fuel = 0
        for numbers in crabs:
            temp_fuel += fuel_factor(abs(numbers - crabs[median_index] + i))

        if temp_fuel <= fuel:
            fuel = temp_fuel
            i += -1
            continue
        else:
            break
    print(f'Part 2: {fuel}')

# Each step takes one more fuel
def fuel_factor(horizontal_steps):
    fuel_amount = 0
    for i in range(1, horizontal_steps + 1):
        fuel_amount += i
    return fuel_amount

main2()