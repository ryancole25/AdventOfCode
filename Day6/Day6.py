# PART 1

# Open the input txt file
with open('input.txt') as file:
    contents = file.readlines()

# Store the text as a string
text = contents[0]
# print(text)

# Loop through the string to get the answer
for i in range(0,len(text) - 4):
    # print(f'i: {i}')
    # print(f'{text[(i): (i + 4)]}')

    # Check if first char is in the next 3
    if text[i] in text[i + 1: i + 4]:
        # print("STEP 1")
        continue
    # Check if second char is in the next 2
    elif text[i + 1] in text[i + 2: i + 4]:
        # print("STEP 2")
        continue
    # Check if third char is in the next 1
    elif text[i + 2] in text[i + 3]:
        # print("STEP 3")
        continue
    # No duplicates in 4 chars
    else:
        print(f"Part 1 Answer: {i + 4}")
        break

# ----------------------------------------------------------------------------------------
# PART 2

# 14 consecutive distinct characters

# Loop through the string to get the answer
for i in range(0,len(text) - 14):
    # print(f'i: {i}')
    # print(f'{text[(i): (i + 14)]}')

    if text[i] in text[i + 1: i + 14]:
        # print("STEP 1")
        continue
    elif text[i + 1] in text[i + 2: i + 14]:
        # print("STEP 2")
        continue
    elif text[i + 2] in text[i + 3: i + 14]:
        # print("STEP 3")
        continue
    elif text[i + 3] in text[i + 4: i + 14]:
        # print("STEP 4")
        continue
    elif text[i + 4] in text[i + 5: i + 14]:
        # print("STEP 5")
        continue
    elif text[i + 5] in text[i + 6: i + 14]:
        # print("STEP 6")
        continue
    elif text[i + 6] in text[i + 7: i + 14]:
        # print("STEP 7")
        continue
    elif text[i + 7] in text[i + 8: i + 14]:
        # print("STEP 8")
        continue
    elif text[i + 8] in text[i + 9: i + 14]:
        # print("STEP 9")
        continue
    elif text[i + 9] in text[i + 10: i + 14]:
        # print("STEP 10")
        continue
    elif text[i + 10] in text[i + 11: i + 14]:
        # print("STEP 11")
        continue
    elif text[i + 11] in text[i + 12: i + 14]:
        # print("STEP 12")
        continue
    elif text[i + 12] in text[i + 13]:
        # print("STEP 13")
        continue
    # No duplicates in 14 chars
    else:
        print(f"Part 2 Answer: {i + 14}")
        break

