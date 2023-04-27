import random
import pathlib
from string import ascii_letters

from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:fire: {headline} :fire:[/]\n")


def get_random_word():
    with open("word_list.txt", "r", encoding="utf-8") as f:
        words = [
            word.upper()
            for word in f.read().splitlines()
            if len(word) == 5 and all(letter in ascii_letters for letter in word)
        ]
    return random.choices(words)[0]


def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")

        console.print("".join(styled_guess), justify="center")


def game_over(guesses, word):
    refresh_page(headline="Game Over")

    show_guesses(guesses, word)

    if guesses[-1] == word:
        console.print(f"\n[bold white on green]Correct, the Word is {word}[/]")
    else:
        console.print(f"[bold white on red]Sorry, The Word was {word}[/]")


def main():
    word = get_random_word()
    guess = ["_" * 5] * 6

    for idx in range(6):
        refresh_page(headline=f"Guess No{idx + 1}")
        show_guesses(guess, word)

        guess[idx] = input(f"\nGuess no.{idx + 1} : ").upper()

        if guess[idx] == word:
            break

    game_over(guess, word)


if __name__ == "__main__":
    main()
