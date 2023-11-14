import ascii_art
import os

def center_text(text):
    """
    Center the text in the terminal window.
    """
    columns, _ = os.get_terminal_size()
    padding = (columns - len(text)) // 2
    centered_text = " " * padding + text
    return centered_text

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def print_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print(f"- {item}")


def clear_screen():
    # Function to clear the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')


def print_menu():
    # Function to print the main menu
    print("************ PIZZA HERO: THE MUSHROOM QUEST ************")
    print("-------------------------------------------------------")
    print("                 1. Start Game")
    print("                 2. Rules")
    print("                 3. Exit")
    print("-------------------------------------------------------")


def start_game(player):
    # Function to start the game
    clear_screen()
    print(ascii_art.pizza_art)
    print(f"Welcome, {player.name}! Are you ready for an adventure?")
    input("Press Enter to continue...")

    print(
        "\nYou find yourself in the small town of Mushroomville. Your great-grandfather's recipe for the magical pizza is hidden somewhere here.")
    input("Press Enter to explore...")

    print("\nAs you walk through the town, you encounter a friendly mushroom named Funghi.")
    input("Press Enter to talk to Funghi...")

    print(
        "\nFunghi: Hello, brave adventurer! I heard you're on a quest for the magical pizza. I can help you, but first, you must prove yourself.")
    input("Press Enter to continue...")

    # Loop for the riddle question
    while True:
        clear_screen()
        print("\nFunghi: To prove your bravery, you need to solve a riddle. Here it is:")
        print(
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")

        # Options for the player to choose
        options = ["An echo", "A tree", "A river"]

        # Display options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Player's choice
        while True:
            try:
                choice = int(input("Your choice (enter the number): "))
                if 1 <= choice <= len(options):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(options))
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check the player's answer
        if options[choice - 1] == "An echo":
            print(
                "\nFunghi: Correct! You're truly a hero. Take this map; it will guide you to the ingredients for the magical pizza.")
            player.add_to_inventory("Map")
            break
        else:
            print("\nFunghi: That's not the correct answer. Think again!")
            input("Press Enter to try the riddle again...")


def show_rules():
    # Function to display game rules
    clear_screen()
    print("Pizza Hero: The Mushroom Quest")
    print("------------------------------")
    print("Game Instructions:")
    print("This is a text adventure game where you will play as the hero/heroine Bob/Bobina.")
    print("Your task is to prepare a magical pizza using your great-grandfather's recipe.")
    print("Throughout the game, you will follow the story, make decisions, and solve puzzles.")
    print("To make choices, enter the corresponding option numbers.")
    print("Good luck!")
    input("Press Enter to go back to the main menu...")


def explore_map(player):
    # Function to explore the map
    clear_screen()
    print("You take out the map and see the following:")
    print("Map Information:")
    print("1. A drawn forest")
    print("2. A small building behind the forest")

    input("Press Enter to continue...")

    print("\nYou decide to head towards the forest.")
    input("Press Enter to continue...")

    print("\nAs you enter the forest, you hear mysterious sounds and feel a magical aura.")
    input("Press Enter to explore further...")

    print("\nAfter some time, you find yourself in front of a small building.")
    print("This must be the place mentioned on the map!")
    input("Press Enter to continue...")

    print(
        "\nCongratulations, you've found the secret building. Inside, you discover the ancient recipe for the magical pizza.")
    player.add_to_inventory("Ancient Pizza Recipe")
    input("Press Enter to continue...")


def main():
    # Main function to run the game
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
        elif choice == "3":
            print("Exiting the game...")
            break
        else:
            print("Error: Invalid command. Please try again.")

        if "Map" in player.inventory:
            # If the player has the map, give them the option to explore it
            explore_choice = input("Would you like to explore the map? (yes/no): ").lower()
            if explore_choice == "yes":
                explore_map(player)
                player.print_inventory()


if __name__ == "__main__":
    main()
