# game.py

import ascii_art
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

def clear_screen():
    # Function to clear the terminal screen
    os.system('clear' if os.name == 'posix' else 'cls')

def show_rules():
    clear_screen()
    print("Pizza Hero: The Mushroom Quest")
    print("------------------------------")
    print("Game Instructions:\n")
    print("This is a text adventure game where you will play as the fantasy hero.")
    print("Your task is to prepare a magical pizza using your great-grandfather's recipe.")
    print("Throughout the game, you will follow the story, make decisions, and solve puzzles.")
    print("To make choices, enter the corresponding option numbers.")
    print("Good luck!\n")
    input("Press Enter to start your adventure...")

def start_game(player):
    clear_screen()
    print(ascii_art.pizza_art)
    print(f"Welcome, {player.name}! Are you ready for an adventure?\n")
    input("Press Enter to continue...")

    print(
        "\nYou find yourself in the small town of Mushroomville. Your great-grandfather's recipe for the magical pizza "
        "is hidden somewhere here.\n")
    input("Press Enter to explore...")

    print("\nAs you walk through the town, you encounter a friendly mushroom named Funghi.\n")
    input("Press Enter to talk to Funghi...")

    print(
        "\nFunghi: Hello, brave adventurer! I heard you're on a quest for the magical pizza. I can help you, but first, "
        "you must prove yourself.\n")
    input("Press Enter to continue...")

    # Loop for the riddle question
    while True:
        clear_screen()
        print("\nFunghi: To prove your bravery, you need to solve a riddle. Here it is:")
        print(
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\n")

        # Options for the player to choose
        options = ["An echo", "A tree", "A river"]

        # Display options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        # Player's choice
        while True:
            try:
                choice = int(input("\nYour choice (enter the number): "))
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
            print("\nFunghi: That's not the correct answer. Think again!\n")
            input("Press Enter to try the riddle again...")
