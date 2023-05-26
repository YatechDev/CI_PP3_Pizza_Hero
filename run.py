import ascii_art
import os

print(ascii_art.title_art)


def print_menu():
    print("************ PIZZA HERO: THE MUSHROOM QUEST ************")
    print("-------------------------------------------------------")
    print("                 1. Start Game")
    print("                 2. Rules")
    print("                 3. Exit")
    print("-------------------------------------------------------")


def start_game():
    """
    Function to start the game
    """
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear actual terminal screen
    print(ascii_art.pizza_art)  # Print ascii art of pizza
    print("Are you ready?")
    choice = input("Please answer Yes / No?: ")
    print("Starting the game...")



def show_rules():
    """
       Function to show the game rules
       """
    print("Pizza Hero: The Mushroom Quest")
    print("------------------------------")
    print("Game Instructions:")
    print("This is a text adventure game where you will play as the hero/heroine Bob/Bobina.")
    print("Your task is to prepare a magical pizza using your great-grandfather's recipe.")
    print("Throughout the game, you will follow the story, make decisions, and solve puzzles.")
    print("To make choices, enter the corresponding option numbers.")
    print("Good luck!")
    print()

    while True:
        choice = input("Please choose an option (1: Start, 2: Exit): ")

        if choice == "1":
            start_game()
            break
        elif choice == "2":
            print("Exiting the game...")
            return
        else:
            print("Error: Invalid command. Please try again.")

def main():
    print_menu()

    while True:
        choice = input("Please type the number: ")

        if choice == "1":
            start_game()
            break
        elif choice == "2":
            show_rules()
            break
        elif choice == "3":
            print("Exiting the game...")
            return
        else:
            print("Error: Invalid command. Please try again.")


if __name__ == "__main__":
    main()