# my_mordl is a game where you guess a word and the code give you a feedback whethert you guessed it correctly or you misplace some of the letteracter
import random
import pathlib


def menu():
    print("Hello World")


word_list = pathlib.Path("word_list.txt")
word = random.choice(
    [word.upper() for word in word_list.read_text(encoding="utf-8").strip().split("\n")]
)
print(word)
for guess_count in range(1, 7):
    user_guess = input(f"Guess No.{guess_count} : ").upper()

    if user_guess == word:
        print("You Win!")
        break
    print(f"Your guess is {6 - guess_count} more left")

    correct_letter = {
        letter for letter, correct in zip(user_guess, word) if letter == correct
    }

    misplaced_letter = set(user_guess) & set(word) - correct_letter
    wrong_letter = set(user_guess) - set(word)  # type: ignore

    print("Correct Letters :", ", ".join(sorted(correct_letter)))
    print("Misplaced letter : ", ",".join(sorted(misplaced_letter)))
    print("Wrong Letter : ", ", ".join(sorted(wrong_letter)))
else:
    print(f"{word} is the correct word")
