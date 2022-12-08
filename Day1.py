# PART 1
# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
list = []
for word in contents:
    list.append(word.strip())

# Convert the string list into integers with zeros separating the different elves
number_list = []
for number in list:
    if number == '':
        number_list.append(0)
    else:
        number_list.append(int(number))

# Count the total calories for each elf and store in a list (index represents elf number)
calories = []
count = 0

for number in number_list:
    count += number
    if number == 0:
        calories.append(count)
        count = 0

print(max(calories))

# ----------------------------------------------------------------------------------------
# PART 2

# Make a copy of the list and reverse sort in descending order
sorted_cals = calories.copy()
sorted_cals.sort(reverse=True)

# Sum the top 3
print(sum(sorted_cals[0:3]))



