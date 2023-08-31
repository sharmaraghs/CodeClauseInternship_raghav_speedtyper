import random
import time


def get_random_word():
    word_list = ["python", "programming", "keyboard", "challenge", "developer", "typing", "practice", "speed",
                 "accuracy", "computer"]
    return random.choice(word_list)


def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")

    word = get_random_word()
    print("Your word is:", word)

    start_time = time.time()
    user_input = input("Type the word and press Enter: ")
    end_time = time.time()

    if user_input == word:
        time_taken = end_time - start_time
        words_per_minute = len(word) / (time_taken / 60)
        print(f"Congratulations! You typed the word correctly in {time_taken:.2f} seconds.")
        print(f"Your typing speed: {words_per_minute:.2f} words per minute")
    else:
        print("Oops! You typed the word incorrectly. Try again.")


if __name__ == "__main__":
    main()
