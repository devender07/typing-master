import random
import time
import json

# Global variables
leaderboard_file = "leaderboard.json"

def update_leaderboard(username, wpm):
    # Load current leaderboard from JSON file
    try:
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    # Add or update user's entry
    user_entry = {'username': username, 'wpm': wpm}
    leaderboard.append(user_entry)

    # Sort the leaderboard based on WPM in descending order
    def get_wpm(entry):
        return entry['wpm']
    leaderboard.sort(key=get_wpm, reverse=True)

    # Save the updated leaderboard back to the JSON file
    with open(leaderboard_file, 'w') as file:
        json.dump(leaderboard, file, indent=2)

def show_leaderboard():
    try:
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        print("Leaderboard is empty.")
        return

    print("\nLeaderboard:")
    print("{:<15} {:<10}".format("Username", "WPM"))
    print("-" * 25)
    for entry in leaderboard:
        print("{:<15} {:<10}".format(entry['username'], entry['wpm']))
    print()

def load_words_from_json(category):
    # Assuming words.json contains categories as keys and lists of words as values
    try:
        with open('words.json', 'r') as file:
            words_dict = json.load(file)
            return words_dict.get(category, [])
    except FileNotFoundError:
        print("Error: words.json not found.")
        return []

def get_user_input():
    user_input = input("\nEnter the words as shown. Press 'Ctrl + C' to quit.\n")
    return user_input

def display_words(words):
    print("\nType the following words:")
    print(" ".join(words))

def show_categories():
    try:
        with open('words.json', 'r') as file:
            words_dict = json.load(file)
            categories = list(words_dict.keys())
            print("\nAvailable Categories:")
            print(", ".join(categories))
    except FileNotFoundError:
        print("Error: words.json not found.")

def main():
    print("Welcome to Terminal Typing Master!")

    username = input("Enter your username: ")

    while True:
        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            show_categories()
            category = input("Enter the typing category: ")
            words = load_words_from_json(category)

            if not words:
                print("Invalid category. Please choose a different category.")
                continue

            display_words(words)
            start_time = time.time()
            user_input = get_user_input()
            end_time = time.time()

            words_typed = len(user_input.split())
            time_taken = end_time - start_time
            wpm = int((words_typed / time_taken) * 60)

            update_leaderboard(username, wpm)
            show_leaderboard()

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            print("Exiting Terminal Typing Master. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
