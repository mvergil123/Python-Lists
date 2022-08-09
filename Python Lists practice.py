user_input = input("Please type a sentence: ")
letter = input("Which letter would you like to count? ")
count = 0
for letter_input in user_input:
    if letter_input == letter:
        count += 1


s = ""
if count > 1:
    s = "'s"
print(f"There are {count} {letter}{s} in your sentence.")