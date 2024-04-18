import random

def guess_number():
    # Get user input for range and maximum attempts
    min_num = int(input("Enter the minimum number for the range: "))
    max_num = int(input("Enter the maximum number for the range: "))
    max_attempts = int(input("Enter the maximum number of attempts allowed: "))
    
    # Generate a random number within the specified range
    secret_number = random.randint(min_num, max_num)
    
    # Track the number of attempts
    attempts = 0
    
    while attempts < max_attempts:
        # Ask the user to guess the number
        guess = int(input(f"Guess a number between {min_num} and {max_num}: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    
    if attempts >= max_attempts:
        print(f"Sorry, you have used all {max_attempts} attempts. The secret number was {secret_number}.")

# Play the game
guess_number()