import random
import sys

class NumberGuessingGame:
    def __init__(self):
        self.min_num = 1
        self.max_num = 100
        self.max_attempts = 7
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def play_game(self):
        while self.attempts < self.max_attempts:
            guess = input(f"Guess a number between {self.min_num} and {self.max_num} (or 'exit' to quit): ")
            if guess.lower() == 'exit':
                sys.exit("Exiting the game.")

            guess = int(guess)
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Try a higher number.")
            else:
                print("Try a lower number.")

        if self.attempts >= self.max_attempts:
            print(f"Sorry, you have used all {self.max_attempts} attempts. The secret number was {self.secret_number}.")

class Menu:
    @staticmethod
    def display_menu():
        print("Welcome to the Number Guessing Game!")
        print("1. Play with default settings")
        print("2. Set custom range and maximum attempts")
        print("3. Exit")

    @staticmethod
    def get_choice():
        return input("Enter your choice (1, 2, or 3): ")

def main():
    menu = Menu()
    while True:
        menu.display_menu()
        choice = menu.get_choice()
        
        game = NumberGuessingGame()
        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.min_num = int(input("Enter the minimum number for the range: "))
            game.max_num = int(input("Enter the maximum number for the range: "))
            game.max_attempts = int(input("Enter the maximum number of attempts allowed: "))
            game.secret_number = random.randint(game.min_num, game.max_num)
            game.attempts = 0
            game.play_game()
        elif choice == '3':
            sys.exit("Exiting the game.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Start the game
if __name__ == "__main__":
    main()