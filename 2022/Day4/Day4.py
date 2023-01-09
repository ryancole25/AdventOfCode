# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
list = []
for item in contents:
    list.append(item.strip('\n'))

# Split by the commas to make a list of lists
list2 = []
for line in list:
    list2.append(line.split(','))

# print(list2)


# Split the numbers from the '-'
list3 = []
for i in range(0,len(list2)):
    for j in range(0,2):
        list3.append((list2[i][j].split('-')))

# print(list3)

# Find the times where the one list completely covers the other list
fully_contains = 0
for i in range(0,len(list3) - 1, 2):
    if int(list3[i][0]) <= int(list3[i + 1][0]) and int(list3[i][1]) >= int(list3[i + 1][1]):
        fully_contains += 1
    elif int(list3[i][0]) >= int(list3[i + 1][0]) and int(list3[i][1]) <= int(list3[i + 1][1]):
        fully_contains += 1

print(f'Part one answer: {fully_contains}')

# ----------------------------------------------------------------------------------------
# PART 2

# How many pairs overlap at all?

overlap = 0
for i in range(0,len(list3) - 1, 2):
    if int(list3[i][0]) >= int(list3[i + 1][0]) and int(list3[i][0]) <= int(list3[i + 1][1]):
        overlap += 1
    elif int(list3[i][1]) >= int(list3[i + 1][0]) and int(list3[i][1]) <= int(list3[i + 1][1]):
        overlap += 1
    elif int(list3[i + 1][0]) >= int(list3[i][0]) and int(list3[i + 1][0]) <= int(list3[i][1]):
        overlap += 1
    elif int(list3[i + 1][1]) >= int(list3[i][0]) and int(list3[i + 1][1]) <= int(list3[i][1]):
        overlap += 1


print(f'Part two answer: {overlap}')