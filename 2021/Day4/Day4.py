# PART 1/2

called_numbers = [90,4,2,96,46,1,62,97,3,52,7,35,50,28,31,37,74,26,59,53,82,47,83,80,19,40,68,95,34,55,54,73,12,78,30,63,57,93,72,77,56,91,23,67,64,
                  79,85,84,76,10,58,0,29,13,94,20,32,25,11,38,89,21,98,92,42,27,14,99,24,75,86,51,22,48,9,33,49,18,70,8,87,61,39,16,66,71,5,69,15,43,88,45,6,81,60,36,44,17,41,65]

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# strip the \n character and store in a list
boards = []
for item in contents:
    boards.append(item.strip('\n'))

# Main function for the bingo cards
def main():
    index_of_winning_numbers = []
    winning_numbers = []
    unmarked_sum = []

    # Make a 5x5 board (Iterate to parse the input for all of the boards)
    x = 0
    y = 5
    while y < len(boards) + 1:
        player_board = []
        row_scoreboard = {0: [], 1: [], 2: [], 3: [], 4: []}
        column_scoreboard = {0: [], 1: [], 2: [], 3: [], 4: []}
        for i in range(x,y):
            row = []
            nums = ''
            for j in range(len(boards[i])):
                if boards[i][j].isnumeric():
                    nums += boards[i][j]
                if boards[i][j] == ' ' and boards[i][j + 1] != ' ' and j != 0:
                    row.append(nums)
                    nums = ''
                if j == len(boards[i]) - 1:
                    row.append(nums)
            player_board.append(row)

        # Score the board for bingo and find the winning called number
        winning_numbers.append(scoring(player_board, row_scoreboard, column_scoreboard))

        # Find the sum of all the unmarked numbers
        unmarked_sum.append(sum_of_unmarked(player_board, row_scoreboard, column_scoreboard))

        x += 6
        y += 6

    # find the index of the winning number in the called numbers
    for number in winning_numbers:
        index_of_winning_numbers.append(called_numbers.index(number))

    # find the winning/losing number that was called
    winning_number = called_numbers[min(index_of_winning_numbers)]
    losing_number = called_numbers[max(index_of_winning_numbers)]

    # find the board that has the winning/losing number
    winning_board = winning_numbers.index(called_numbers[min(index_of_winning_numbers)])
    losing_board = winning_numbers.index(called_numbers[max(index_of_winning_numbers)])

    # find the unmarked score of the winning/losing board
    unmarked_winning_score = unmarked_sum[winning_board]
    unmarked_losing_score = unmarked_sum[losing_board]

    print(f'Part 1: {winning_number * unmarked_winning_score}')
    print(f'Part 2: {losing_number * unmarked_losing_score}')


# Score the bingo card
def scoring(player_board, row_scoreboard, column_scoreboard):
    # Go through each called number and search if the number is on the bingo card
    # Save the x,y coordinates of matches in a row_scoreboard and column_scoreboard to check for bingo
    for num in called_numbers:
        for i in range(len(player_board)):
            for j in range(len(player_board[i])):
                if player_board[i][j] == str(num):
                    row_scoreboard[i].append(j)
                    column_scoreboard[j].append(i)
                # If there is a bingo, stop checking
                if len(row_scoreboard[i]) == 5 or len(column_scoreboard[j]) == 5:
                    winning_num = num
                    return winning_num

def sum_of_unmarked(player_board, row_scoreboard, column_scoreboard):
    # Sum of all numbers
    total_sum = 0
    for row in player_board:
        for number in row:
            total_sum += int(number)

    # Subtract of all the marked numbers
    marked_sum = 0
    for i in range(5):
        for j in row_scoreboard[i]:
            marked_sum += int(player_board[i][j])

    return total_sum - marked_sum

main()