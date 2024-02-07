# guess_number
# COMP 3081-001 SA4 Activity #3
    # by dev chrysalis

number = 10
print("I'm thinking of a number...")

guesses_left = 3
while guess := input("What number am I thinking of? "):
    if guesses_left > 1:
        if guess.strip() == str(number):
            print("Congratulations! You guessed the right number.")
        elif guess == "q":
            print(f"Game quit; number was {number}")
        else:
            guesses_left -= 1
            print(f"{guesses_left} guesses left! Please try again (or q to quit)")
            continue
    else:
        print(f"You ran out of guesses! The number was {number}.")
    break
