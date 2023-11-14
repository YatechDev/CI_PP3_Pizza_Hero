# run.py

import ascii_art
from game import Player, start_game, show_rules, clear_screen

def print_menu():
    # Function to print the main menu
    print("************ PIZZA HERO: THE MUSHROOM QUEST ************")
    print("-------------------------------------------------------")
    print("                 1. Start Game")
    print("                 2. Rules")
    print("                 3. Exit")
    print("-------------------------------------------------------")

def main():
    clear_screen()
    print(ascii_art.title_art)
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        print_menu()
        choice = input("Please type the number: ")

        if choice == "1":
            start_game(player)
        elif choice == "2":
            show_rules()
            start_game(player)  # Added starting the game after displaying rules
        elif choice == "3":
            print("Exiting the game...")
            break
        else:
            print("Error: Invalid command. Please try again.")

if __name__ == "__main__":
    main()
