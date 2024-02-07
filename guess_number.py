# guess_number
# COMP 3081-001 SA4 Activity #3
    # by dev chrysalis

number = 10
print("I'm thinking of a number...")

while guess := input("What number am I thinking of? "):
    if guess != "q":
        if (guess := int(guess)) == number:
            print("Congratulations! You guessed the right number.")
        else:
            print(f"Try again! You guessed too {'low' if guess < number else 'high'}.")
            continue
    else:
        print(f"Game quit; number was {number}")
    break