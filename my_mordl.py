# my_mordl is a game where you guess a word and the code give you a feedback whethert you guessed it correctly or you misplace some of the letteracter
import random
import pathlib
from string import ascii_letters


def get_random_word():
    word_list = pathlib.Path("word_list.txt")
    words = [
        word.upper()
        for word in word_list.read_text(encoding="utf-8").split("\n")
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def show_guess(user_guess, word):
    correct_letter = {
        letter for letter, correct in zip(user_guess, word) if letter == correct
    }

    misplaced_letter = set(user_guess) & set(word) - correct_letter
    wrong_letter = set(user_guess) - set(word)  # type: ignore

    print("Correct Letters :", ", ".join(sorted(correct_letter)))
    print("Misplaced letter : ", ",".join(sorted(misplaced_letter)))
    print("Wrong Letter : ", ", ".join(sorted(wrong_letter)))


def game_over(word):
    print(f"{word} is the correct word")


def main():
    # Pre Process
    # get the random word
    word = get_random_word()
    print(word)
    # main process when user playing the game
    for guess_count in range(1, 7):
        user_guess = input(f"Guess no.{guess_count} : ").upper()

        show_guess(user_guess, word)
        if user_guess == word:
            break
    else:
        game_over(word)

    # post procress when user get the result of the game


if __name__ == "__main__":
    main()
