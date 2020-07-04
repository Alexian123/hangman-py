import time
import os
from getpass import getpass

end = False
word: str
found: dict = {}
discarded: set = set()
mistake_count: int = 0


def clear_screen():
    return os.system('cls')  # only for windows


def pause(seconds: int, msg=""):
    print(msg)
    time.sleep(seconds)


def get_word() -> str:
    word = getpass("Type the word: ").strip().lower()
    confirm = getpass("Re-type it: ").strip().lower()
    print()  # new line
    if word == confirm and word != "":
        for c in confirm:
            if not str(c).isalpha() and str(c) != ' ':
                print("The word can't contain numbers, symbols or spaces!\n")
                return get_word()
        return word
    print("The words do not match!\n")
    return get_word()


def display_figure(mistakes=0):
    if mistakes == 0:
        print("""____________
|/          |
|
|
|
|______\n\n""")
    elif mistakes == 1:
        print("""____________
|/          |
|           0
|
|
|______\n\n""")
    elif mistakes == 2:
        print("""____________
|/          |
|           0
|           |
|
|______\n\n""")
    elif mistakes == 3:
        print("""____________
|/          |
|           0
|          /|
|
|______\n\n""")
    elif mistakes == 4:
        print("""____________
|/          |
|           0
|          /|\\
|
|______\n\n""")
    elif mistakes == 5:
        print("""____________
|/          |
|           0
|          /|\\
|          /
|______\n\n""")
    else:
        print("""____________
|/          |
|           0
|          /|\\
|          /\\
|______\n\n""")
        print("GAME OVER\n")
        pause(2, "The word was: " + word)


def register_letters():
    discarded.clear()
    found.clear()
    for letter in word:
        found[letter] = False


def display_discarded():
    if len(discarded) > 0:
        print("Discarded letters:", end=" ")
        for letter in discarded:
            print(letter, end=" ")
        print("\n")


def guess_next():
    global mistake_count
    try:
        letter: str = input("\n\nEnter a letter: ").strip().upper()
        if not letter.isalpha() or len(letter) > 1:
            raise TypeError
        if letter not in found and letter not in discarded:
            mistake_count += 1
            discarded.add(letter)
        else:
            found[letter] = True
    except TypeError:
        print("\n\"" + letter + "\" is not a letter!\n")
        guess_next()


def is_win() -> bool:
    for letter in word:
        if not found[letter]:
            return False
    return True


def play():
    while mistake_count < 7:
        clear_screen()
        display_figure(mistake_count)
        display_discarded()
        if mistake_count == 6:
            break
        print("\t\t", end=" ")
        for letter in word:
            if found[letter]:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        guess_next()
        if is_win():
            clear_screen()
            print("\nCongratulatinos! You Won!\n")
            pause(2, "The word was: " + word)
            break


def initiate_game():
    global word, mistake_count
    mistake_count = 0
    word = get_word().upper()
    register_letters()
    play()


def get_command():
    global end
    command: str = input(
        "\nType \"start\" to play the game or \"exit\" to close the game: ").strip().lower()
    if command == "start":
        clear_screen()
        initiate_game()
    elif command == "exit":
        pause(1, "\nExiting...")
        end = True
    else:
        print("\nUnrecognised command: " + command)
        get_command()


def main():
    while not end:
        clear_screen()
        print("\nHangman Py  -  By Alexian Hentiu")
        get_command()


if __name__ == "__main__":
    main()
