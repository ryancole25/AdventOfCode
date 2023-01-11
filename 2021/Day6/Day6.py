# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# Make each fish an element in the list and convert into int
fish = contents[0].split(',')
for i in range(len(fish)):
    fish[i] = int(fish[i])

# fish = [3,4,3,1,2]

def main():
    day = 0
    while day < 80:
        day += 1
        new_day(fish)
        # print(f'After {day} days: {fish}')

    print(f'Part 1: {len(fish)}')

# Create more fish
def new_day(fish):
    temp_fish = []
    for i in range(len(fish)):
        if fish[i] != 0:
            fish[i] += -1
        else:
            fish[i] += 6
            temp_fish.append(8)
    if temp_fish != []:
        for number in temp_fish:
            fish.append(number)
    return fish

main()

# Part 2 -------------------------------------------------------------------------------------------------------------------------------------------------

# Reset the fish variable to the input
fish = contents[0].split(',')
for i in range(len(fish)):
    fish[i] = int(fish[i])

def main2():
    # Get starting fish counts
    day = 0
    fish_dict = {}
    for i in range(9):
        fish_dict[i] = fish.count(i)

    # Iterate new days
    while day < 256:
        day += 1
        fish_dict = new_day2(fish_dict)

    # Count the fish
    num_of_fish = 0
    for i in range(9):
        num_of_fish += fish_dict[i]
    print(f'Part 2: {num_of_fish}')

# Count the fish instead of making a new list every time
def new_day2(fish_dict):
    # Create a temporary dictionary to move values into
    new_fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    # Every fish value subtracts by 1 (count of the fish 1 day younger increases by 1)
    for i in range(8):
        new_fish_dict[i] = fish_dict[i + 1]

    # 0s become 6s and make new 8s
    new_fish_dict[8] += fish_dict[0]
    new_fish_dict[6] += fish_dict[0]

    return new_fish_dict

main2()