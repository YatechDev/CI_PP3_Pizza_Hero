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

    print("\nFunghi: Hello, brave adventurer! I heard you're on a quest for the magical pizza. I can help you, "
          "but first, you must prove yourself.\n")
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
            print("\nFunghi: Amazing! You're truly a hero. Let me give you a hint.")
            input("Press Enter to continue...")

            print(
                "\nFunghi: Now, you should head to Dark Timmy's place on the edge of the town. He'll guide you further.\n")
            input("Press Enter to continue...")

            # Start the first quest
            quest_1(player)
            break
        else:
            print("\nFunghi: That's not the correct answer. Think again!\n")
            input("Press Enter to try the riddle again...")


def quest_1(player):
    clear_screen()
    print("You embark on a journey to Dark Timmy's place on the edge of the town.\n")
    input("Press Enter to continue...")

    print("\nAfter a dark and mysterious path, you reach Dark Timmy's residence.\n")
    input("Press Enter to meet Dark Timmy...")

    print("\nDark Timmy: Greetings, brave adventurer! Welcome to the gloomy side of Mushroomville.")
    input("Press Enter to continue...")

    print(
        "\nDark Timmy: I heard you're on a quest for the magical pizza. Before we proceed, would you like to hear a joke?\n")
    print("1. Yes, tell me the joke.")
    print("2. No, I'm not in the mood.")

    # Player's choice
    while True:
        try:
            choice = int(input("\nYour choice (enter the number): "))
            if choice in [1, 2]:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        print("\nDark Timmy: Alright, here's a pizza joke for you:")
        print("Why did the pizza maker go to jail?\n")
        input("Press Enter to hear the punchline...")

        print(
            "\nDark Timmy: Because he couldn't make a good crust! Haha! Well, I find it amusing. Now, back to business.\n")
        input("Press Enter to continue...")
        print(
            "\nDark Timmy: The recipe you seek is indeed a valuable one. However, you can find it in Beatrix's shop at the central market.\n")
    else:
        print("\nDark Timmy: No worries. Let's get back to business.")
        input("Press Enter to continue...")
        print(
            "\nDark Timmy: The recipe you seek is indeed a valuable one. However, you can find it in Beatrix's shop at the central market.\n")

    # End of the quest
    input("Press Enter to continue your adventure...")

    # Start the encounter with a strange character
    encounter_strange_character(player)

def encounter_strange_character(player):
    clear_screen()
    print("As you make your way to the central market, you encounter a strange character.")
    input("Press Enter to initiate a conversation...")

    print("\n: Greetings, adventurer! I am Zephyr, the wanderer of Mushroomville.")
    input("Press Enter to continue...")

    print("\nZephyr: I sense you're on a quest. Would you like some guidance?")
    print("1. Attack!")
    print("2. Escape!")
    print("3. Negotiate.")

    # Player's choice
    while True:
        try:
            choice = int(input("\nYour choice (enter the number): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        print("\nZephyr: Surprised by your sudden attack, I'll make a swift escape.")
        input("Press Enter to continue...")

    elif choice == 2:
        print("\nZephyr: You flee from the encounter, leaving the bewildered Zephyr behind.")
        input("Press Enter to continue...")

    elif choice == 3:
        print("\nZephyr: Wise choice, adventurer. To reach your destination, head straight to the central market.")
        input("Press Enter to continue...")

    print("\nYou successfully navigate through the encounter and arrive at the central market.")
    input("Press Enter to meet Beatrix and start the next quest...")

    # # Start the third quest
    # quest3(player)