# guess_number
# COMP 3081-001 SA4 Activity #3
    # by dev chrysalis

number = 10
print("I'm thinking of a number...\n")

guesses_left = 3
while guess := input("What number am I thinking of? "):
    if guess != "q":
        guesses_left -= 1
        es = "es" if guesses_left > 1 else ""
        if (guess := int(guess)) == number:
            print("Congratulations! You guessed the right number.")
        elif guesses_left > 0:
            print(f"You guessed too {'low' if guess < number else 'high'}.\n"
            + f"Please try again! You have {guesses_left} guess{es} left (q to quit)\n")
            continue
        else:
            print(f"You ran out of guesses! The number was {number}")
    else:
        print(f"Game quit. The number was {number}")
    break
