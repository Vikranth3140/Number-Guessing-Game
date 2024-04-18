import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Number of attempts
    attempts = 0
    
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess a number between 1 and 100: "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

# Play the game
guess_number()