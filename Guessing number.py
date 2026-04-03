import random

secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

attempts = 0

print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break