import random

number_to_guess = random.randint(1, 10)
max_attempts = 10
attempts = 0

print("Welcome to the number gussing game")
print("I have selected a number between 1 and 100")
print("You have {max_attempts} attempts to guess that number")

for i in range(max_attempts):
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low! Try again")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        attempts += 1
        print(f"Congratulations. "
        f"you've guessed the correct number in {attempts} attempts")
        break