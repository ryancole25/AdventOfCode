# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
rucksacks = []
for bag in contents:
    rucksacks.append(bag.strip())

# search for duplicates in first half that are in second half
sum = 0
for bag in rucksacks:
    duplicates = []
    # Go through each bag and find the duplicates
    for char in bag[0:(len(bag)//2)]:
        if char in bag[(len(bag)//2):len(bag)]:
            # Makes sure you are only counting the duplicates once
            if char not in duplicates:
                duplicates.append(char)
    # Add the priority value for the duplicates -- ASCII for 'a' is 97 -- ASCII for 'A' is 65
    if len(duplicates) > 0:
        if duplicates[0].isupper():
            sum += ord(duplicates[0]) - 38
        elif duplicates[0].islower():
            sum += ord(duplicates[0]) - 96
    # print(duplicates)

print(sum)

# ----------------------------------------------------------------------------------------
# PART 2

# Create a while loop that looks at three lines at a time
duplicates2 = []
sum2 = 0
i = 0
while i < len(rucksacks):
    duplicates2 = []
    for char in rucksacks[i]:
        if char in rucksacks[i + 1]:
            if char in rucksacks[i + 2]:
                if char not in duplicates2:
                    duplicates2.append(char)
    print(duplicates2)

    # Add the priority value for the duplicates -- ASCII for 'a' is 97 -- ASCII for 'A' is 65
    if len(duplicates2) > 0:
        if duplicates2[0].isupper():
            sum2 += ord(duplicates2[0]) - 38
        elif duplicates2[0].islower():
            sum2 += ord(duplicates2[0]) - 96
    i += 3

print(sum2)