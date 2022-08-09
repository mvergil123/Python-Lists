#computer comes up with a number
import random
computer_number = random.randint(0,10)
attempts = 0
#while loop and ask for a number
while True:
    user_number = int(input("Guess a number: "))


#compare it to the computer's number
    if computer_number == user_number:
        print("You guessed the correct number!")
        print(f"It took you {attempts} attempts")
        if attempts > 3:
            print("Sorry, you failed!")
        else:
            print("You won!!!")
        break
    else:
        print("You did not guess the correct number.")
        attempts += 1

#if correct, user won and print the number of attempts