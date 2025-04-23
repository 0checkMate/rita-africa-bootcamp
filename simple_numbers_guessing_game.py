import random

# Generate random number between 0-5
target_number = random.randint(0, 5)
guess = None

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 5...")

while guess != target_number:
    try:
        guess = int(input("Enter your guess: "))
        if guess < 0 or guess > 5:
            print("Please guess a number between 0 and 5!")
        elif guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly!")
    except ValueError:
        print("Please enter a valid number!")
