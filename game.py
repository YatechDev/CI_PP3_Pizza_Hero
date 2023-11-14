# game.py

import ascii_art
import os


class Player:
    def __init__(self, name):
        # Initialize the Player class with a name and an empty inventory
        self.name = name
        self.inventory = []


def clear_screen():
    # Function to clear the console screen
    os.system('clear' if os.name == 'posix' else 'cls')


def show_rules():
    # Function to display the game rules
    clear_screen()
    print(ascii_art.title_art)
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
    # Function to start the game and introduce the player to the initial scenario
    clear_screen()
    print(ascii_art.title_art)
    print(f"Welcome, {player.name}! Are you ready for an adventure?\n")
    input("Press Enter to continue...")

    clear_screen()
    print(ascii_art.title_art)
    print(
        "\nYou find yourself in the small town of Mushroomville. Your great-grandfather's recipe for the "
        "magical pizza "
        "is hidden somewhere here.\n")
    input("Press Enter to explore...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nAs you walk through the town, you encounter a friendly mushroom named Funghi.\n")
    input("Press Enter to talk to Funghi...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nFunghi: Hello, brave adventurer! I heard you're on a quest for the magical pizza. I can help you, "
          "but first, you must prove yourself.\n")
    input("Press Enter to continue...")

    while True:
        clear_screen()
        print(ascii_art.title_art)
        print("\nFunghi: To prove your bravery, you need to solve a riddle. Here it is:")
        print(
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. "
            "What am I?\n")

        options = ["An echo", "A tree", "A river"]

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("\nYour choice (enter the number): "))
                if 1 <= choice <= len(options):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(options))
            except ValueError:
                print("Invalid input. Please enter a number.")

        if options[choice - 1] == "An echo":
            print("\nFunghi: Amazing! You're truly a hero. Let me give you a hint.\n")
            input("Press Enter to continue...")

            clear_screen()
            print(ascii_art.title_art)
            print(
                "\nFunghi: Now, you should head to Dark Timmy's place on the edge of the town. He'll guide you "
                "further.\n")
            input("Press Enter to continue...")

            quest_1(player)
            break
        else:
            print("\nFunghi: That's not the correct answer. Think again!\n")
            input("Press Enter to try the riddle again...")


def quest_1(player):
    # Function for the first quest in the game
    clear_screen()
    print(ascii_art.title_art)
    print("You embark on a journey to Dark Timmy's place on the edge of the town.\n")
    input("Press Enter to continue...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nAfter a dark and mysterious path, you reach Dark Timmy's residence.\n")
    input("Press Enter to meet Dark Timmy...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nDark Timmy: Greetings, brave adventurer! Welcome to the gloomy side of Mushroomville.\n")
    input("Press Enter to continue...")

    clear_screen()
    print(ascii_art.title_art)
    print(
        "\nDark Timmy: I heard you're on a quest for the magical pizza. Before we proceed, would you like to "
        "hear a joke?\n")
    print("1. Yes, tell me the joke.")
    print("2. No, I'm not in the mood.")

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

        clear_screen()
        print(ascii_art.title_art)
        print(
            "\nDark Timmy: Because he couldn't make a good crust! Haha! Well, I find it amusing. Now, back "
            "to business.\n")
        input("Press Enter to continue...")

        clear_screen()
        print(ascii_art.title_art)
        print(
            "\nDark Timmy: The recipe you seek is indeed a valuable one. However, you can find it in Beatrix's shop "
            "at the central market.\n")
    else:
        print("\nDark Timmy: No worries. Let's get back to business.\n")
        input("Press Enter to continue...")
        print(
            "\nDark Timmy: The recipe you seek is indeed a valuable one. However, you can find it in Beatrix's "
            "shop at the central market.\n")

    input("Press Enter to continue your adventure...")

    encounter_strange_character(player)


def encounter_strange_character(player):
    # Function for encountering a strange character in the central market
    clear_screen()
    print(ascii_art.title_art)
    print("\nAs you make your way to the central market, you encounter a strange character.\n")
    input("Press Enter to initiate a conversation...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nZephyr: Greetings, adventurer! I am Zephyr, the wanderer of Mushroomville.\n")
    input("Press Enter to continue...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nZephyr: I sense you're on a quest. Would you like some guidance?")
    print("1. Attack!")
    print("2. Escape!")
    print("3. Negotiate.")

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
        print("\nZephyr: Surprised by your sudden attack, I'll make a swift escape.\n")
        input("Press Enter to continue...")
        clear_screen()
        print(ascii_art.title_art)

    elif choice == 2:
        print("\nZephyr: You flee from the encounter, leaving the bewildered Zephyr behind.\n")
        input("Press Enter to continue...")
        clear_screen()
        print(ascii_art.title_art)

    elif choice == 3:
        print("\nZephyr: Wise choice, adventurer. To reach your destination, head straight to the central market.\n")
        input("Press Enter to continue...")
        clear_screen()
        print(ascii_art.title_art)

    print("\nYou successfully navigate through the encounter and arrive at the central market.\n")
    input("Press Enter to meet Beatrix and start the next quest...")
    clear_screen()
    print(ascii_art.title_art)

    quest_3(player)


def quest_3(player):
    # Function for the third quest in the game
    clear_screen()
    print(ascii_art.title_art)
    print("You reach the central market and find Beatrix's magical pizza shop.\n")
    input("Press Enter to meet Beatrix...")

    clear_screen()
    print(ascii_art.title_art)
    print("\nBeatrix: Ah, you must be the brave adventurer seeking the magical pizza recipe. Welcome!\n")
    input("Press Enter to continue...")

    clear_screen()
    print(ascii_art.title_art)
    print("Beatrix hands you a slice of her famous magical pizza.\n")
    print("This is a pineapple pizza. Only the bravest of adventurers are courageous enough to try it!\n")
    input("Press Enter to make your choice...")

    clear_screen()
    print(ascii_art.title_art)
    print("\n1. Eat the pizza.")
    print("2. Refuse the pizza.")

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
        print("\nBeatrix: A wise choice! Enjoy the magical pizza.\n")
        input("Press Enter to savor the magical taste...")
        clear_screen()
        print(ascii_art.title_art)

        game_completed(player)
    else:
        print("\nBeatrix: A peculiar decision, but I respect it. Maybe next time...\n")
        input("Press Enter to proceed...")

        game_over(player)


def game_completed(player):
    # Function to display the game completion message
    clear_screen()
    print(ascii_art.title_art)
    print("Congratulations, " + player.name + "!")
    print("You have successfully completed the Pizza Hero: The Mushroom Quest.\n")
    print("Beatrix: You have proven yourself worthy of the magical pizza recipe.\n")
    print("As a reward, I present to you the secret recipe for the most magical pizza of all...\n")
    print("The Pineapple Paradise Pizza!\n")
    print("Thank you for playing the game. We hope you enjoyed your adventure!\n")
    print(ascii_art.game_completed_art)
    input("\nPress Enter to return to the main menu...")
    start_game(player)


def game_over(player):
    # Function to display the game over message
    clear_screen()
    print(ascii_art.game_over_art)
    input("\nPress Enter to return to the main menu...")
    start_game(player)
