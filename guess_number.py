# guess_number
# COMP 3081-001 SA4 Activity #3
    # by dev chrysalis

number = 10
print("I'm thinking of a number...")
    
while guess := input("What number am I thinking of? "):
    if guess.strip() == str(number):
        print("Congratulations! You guessed the right number.")
    elif guess == "q":
        print(f"Game quit; number was {number}")
    else:
        print(f"Sorry! Please try again (or q to quit)")
        continue
    break
