# guess_number
# COMP 3081-001 SA4 Activity #3
    # by dev chrysalis

number = 10
print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

if guess == number:
    print("Congratulations! You guessed the right number.")
else:
    print(f"Sorry! The number was {number}")
