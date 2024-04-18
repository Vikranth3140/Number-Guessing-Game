import random

def guess_number(min_num=1, max_num=100, max_attempts=7):
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

def main():
    print("Welcome to the Number Guessing Game!")
    print("1. Play with default settings (Range: 1-100, Maximum Attempts: 7)")
    print("2. Set custom range and maximum attempts")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        guess_number()
    elif choice == '2':
        min_num = int(input("Enter the minimum number for the range: "))
        max_num = int(input("Enter the maximum number for the range: "))
        max_attempts = int(input("Enter the maximum number of attempts allowed: "))
        guess_number(min_num, max_num, max_attempts)
    else:
        print("Invalid choice. Please enter either 1 or 2.")

# Start the game
main()