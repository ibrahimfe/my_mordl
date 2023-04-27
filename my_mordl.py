# my_mordl is a game where you guess a word and the code give you a feedback whethert you guessed it correctly or you misplace some of the letteracter
import random  # to randomize secret word
import pathlib
from string import ascii_letters

# Styling The output with rich
from rich.console import Console
from rich.theme import Theme

# using width 40 and a warning
console = Console(width=40, theme=Theme({"warning": "red on yellow"}))


# a function to showing a headline
def refresh_page(
    headline,
):  # headline argument is changing based on the process of the game
    console.clear()  # clearing the console
    console.rule(
        f"[bold blue]:fire: {headline} :fire:[/]\n"
    )  # showing a blue line and a headline in the middle


def get_random_word():
    word_list = pathlib.Path(
        "word_list.txt"
    )  # melampirkan word_list.txt sebagai list dari kata yang akan digunakan
    words = [
        word.upper()
        for word in word_list.read_text(encoding="utf-8").split(
            "\n"
        )  # mengiterasi kata yang ada di file lalu di split berdasarkan \n
        if len(word) == 5
        and all(
            letter in ascii_letters for letter in word
        )  # hanya memilih kata yang memiliki panjang 5
    ]
    return random.choice(
        words
    )  # kata yang sudah menjadi list akan dipilih secara random


# function untuk menampilkan catatan tebakan user
def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []  # list kosong untuk memasukkan guess user
        for letter, correct in zip(guess, word):
            # jika char di posisi tepat dan benar stye berwarna hijau
            if letter == correct:
                style = "bold white on green"
            # jika char benar namun berada di posisi yang salah style berwarna kuning
            elif letter in word:
                style = "bold white on yellow"
            # jika char salah maka akan berwarna abu abu
            elif letter in ascii_letters:
                style = "white on #666666"
            # default hanya akan menampilkan "_"
            else:
                style = "dim"
            # memasukkan style kedalam template rich.console yang ditutup dengan [/]
            styled_guess.append(f"[{style}]{letter}[/]")

        # menggabungkan kata yang sudah di beri style menjadi sebuah string di tengah console
        console.print("".join(styled_guess), justify="center")


# function untuk menampilkan hasil dari permainan
def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over")  # mengganti headline menjadi game over

    show_guesses(guesses, word)  # memanggil kembali catatan dari tebakan user

    # guessed_correctly bernilai true jika user menebak dengan benar
    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the Word is {word}[/]")
    else:
        console.print(f"[bold white on red]Sorry, The Word was {word}[/]")


def main():
    word = (
        get_random_word()
    )  # memamnggil function random untuk memilih secret word secara acak

    guess = ["_" * 5] * 6  # membuat sebuah list untuk mencata tebakan user

    # user bisa menebak hingga 6 kali
    for idx in range(6):
        refresh_page(
            headline=f"Guess No{idx + 1}"
        )  # mengubah headline menjadi tebakan ke n ketika user menebak

        show_guesses(guess, word)

        guess[idx] = input(f"\nGuess no.{idx + 1} : ").upper()

        if guess[idx] == word:
            break
    game_over(guess, word, guessed_correctly=guess[idx] == word)


if __name__ == "__main__":
    main()
