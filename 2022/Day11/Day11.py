# Part 1

# Put the items in a dictionary --> monkey number: items
monkey_items = {0: [59, 65, 86, 56, 74, 57, 56], 1: [63, 83, 50, 63, 56], 2: [93, 79, 74, 55], 3: [86, 61, 67, 88, 94, 69, 56, 91], 4: [76, 50, 51], 5: [77, 76], 6: [74], 7: [86, 85, 52, 86, 91, 95]}

# [Operation, number]
monkey_operations = {0: ['*', 17], 1: ['+', 2], 2: ['+', 1], 3: ['+', 7], 4: ['*', 'itself'], 5: ['+', 8], 6: ['*', 2], 7: ['+', 6]}

# [Divisible by, True, False]
monkey_test = {0: [3, 3, 6], 1: [13, 3, 0], 2: [2, 0, 1], 3: [11, 6, 7], 4: [19, 2, 5], 5: [17, 2, 1], 6: [5, 4, 7], 7: [7, 4, 5]}

# How many things each monkey inspected
monkey_inspections = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

# # TESTS
# monkey_items = {0: [79, 98], 1: [54, 65, 75, 74], 2: [79, 60, 97], 3: [74]}
# monkey_operations = {0: ['*', 19], 1: ['+', 6], 2: ['*', 'itself'], 3: ['+', 3]}
# monkey_test = {0: [23, 2, 3], 1: [19, 2, 0], 2: [13, 1, 3], 3: [17, 0, 1]}
# monkey_inspections = {0: 0, 1: 0, 2: 0, 3: 0}

def main():
    round = 1
    while round <= 20:
        for i in range(len(monkey_items)):
            while len(monkey_items[i]) > 0:
                # Perform the operation on each item
                monkey_inspections[i] += 1
                if monkey_operations[i][0] == '+':
                    monkey_items[i][0] += monkey_operations[i][1]
                elif monkey_operations[i][0] == '*':
                    if type(monkey_operations[i][1]) is int:
                        monkey_items[i][0] *= monkey_operations[i][1]
                    else:
                        monkey_items[i][0] *= monkey_items[i][0]
                # Divide by 3 and round down
                monkey_items[i][0] = monkey_items[i][0] // 3

                # Check the monkey test
                # If true, append to the other monkey and remove from the list
                if monkey_items[i][0] % monkey_test[i][0] == 0:
                    monkey_items[monkey_test[i][1]].append(monkey_items[i][0])
                    monkey_items[i].pop(0)
                # if False, append to the other monkey and remove from the list
                else:
                    monkey_items[monkey_test[i][2]].append(monkey_items[i][0])
                    monkey_items[i].pop(0)
        # print(f'Round: {round}')
        # print(f'Monkey items: {monkey_items}')
        round += 1


    monkey_business = []
    for i in range(len(monkey_inspections)):
        monkey_business.append(monkey_inspections[i])
    monkey_business.sort(reverse=True)
    print(f'Part 1 Answer: {monkey_business[0] * monkey_business[1]}')

main()

# ----------------------------------------------------------------------------------------
# PART 2

# Put the items in a dictionary --> monkey number: items
monkey_items = {0: [59, 65, 86, 56, 74, 57, 56], 1: [63, 83, 50, 63, 56], 2: [93, 79, 74, 55], 3: [86, 61, 67, 88, 94, 69, 56, 91], 4: [76, 50, 51], 5: [77, 76], 6: [74], 7: [86, 85, 52, 86, 91, 95]}

# [Operation, number]
monkey_operations = {0: ['*', 17], 1: ['+', 2], 2: ['+', 1], 3: ['+', 7], 4: ['*', 'itself'], 5: ['+', 8], 6: ['*', 2], 7: ['+', 6]}

# [Divisible by, True, False]
monkey_test = {0: [3, 3, 6], 1: [13, 3, 0], 2: [2, 0, 1], 3: [11, 6, 7], 4: [19, 2, 5], 5: [17, 2, 1], 6: [5, 4, 7], 7: [7, 4, 5]}

# How many things each monkey inspected
monkey_inspections = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

# # TESTS
# monkey_items = {0: [79, 98], 1: [54, 65, 75, 74], 2: [79, 60, 97], 3: [74]}
# monkey_operations = {0: ['*', 19], 1: ['+', 6], 2: ['*', 'itself'], 3: ['+', 3]}
# monkey_test = {0: [23, 2, 3], 1: [19, 2, 0], 2: [13, 1, 3], 3: [17, 0, 1]}
# monkey_inspections = {0: 0, 1: 0, 2: 0, 3: 0}

def main2():
    # Create a common factor by multiplying all of the values together
    common_factor = 3 * 13 * 2 * 11 * 19 * 17 * 5 * 7
    round = 1
    while round <= 10000:
        for i in range(len(monkey_items)):
            while len(monkey_items[i]) > 0:
                # Perform the operation on each item
                monkey_inspections[i] += 1
                if monkey_operations[i][0] == '+':
                    monkey_items[i][0] += monkey_operations[i][1]
                elif monkey_operations[i][0] == '*':
                    if type(monkey_operations[i][1]) is int:
                        monkey_items[i][0] *= monkey_operations[i][1]
                    else:
                        monkey_items[i][0] *= monkey_items[i][0]

                monkey_items[i][0] = monkey_items[i][0] % common_factor

                # Check the monkey test
                # If true, append to the other monkey and remove from the list
                if monkey_items[i][0] % monkey_test[i][0] == 0:
                    monkey_items[monkey_test[i][1]].append(monkey_items[i][0])
                    monkey_items[i].pop(0)
                # if False, append to the other monkey and remove from the list
                else:
                    monkey_items[monkey_test[i][2]].append(monkey_items[i][0])
                    monkey_items[i].pop(0)
        # print(f'Round: {round}')
        # print(f'Monkey items: {monkey_items}')
        round += 1

    monkey_business = []
    for i in range(len(monkey_inspections)):
        monkey_business.append(monkey_inspections[i])
    monkey_business.sort(reverse=True)
    print(f'Part 2 Answer: {monkey_business[0] * monkey_business[1]}')

main2()