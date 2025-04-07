"""Wordle Exercise"""

__author__: str = "730807114"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # create a new varible to display the number of turns
    guess: str = ""  # create a new varibale for users to input their guess word
    while turn <= 6:
        print("=== Turn " + str(turn) + "/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print("You won in " + str(turn) + "/6 turns !")
            turn = 8  # exit the function when the guess is correct & within 6 times
        turn = turn + 1  # repeat the while loop
    if turn == 7:  # when guessing exceeds 6 times
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Prompt the user to guess a word of the desired length"""
    word: str = input(
        "Enter a " + str(secret_word_len) + " character word:"
    )  # 1st guess
    while len(word) != secret_word_len:
        word = input(
            "That wasn't " + str(secret_word_len) + " chars! Try again:"
        )  # wrong length, promt second guess
    return word  # return the word that satisfied the expected length


def contains_char(secret_word: str, character: str) -> bool:
    """Check for a certain character"""
    assert len(character) == 1, f"len('{character}') is not 1"
    index: int = 0  # set a new variable for iterate, idx starts with 0 in python
    while index < len(secret_word):  # must be < because idx starts with 0 in python
        if secret_word[index] == character:  # if there is a matching character
            return True
        else:
            index = index + 1  # continue to process the while loop
    return False


def emojified(guess: str, secret: str) -> str:
    """Use emojis to visually represent the accuracy of a guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # three situations might occur
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0  # create a new variable for iterate, idx starts with 0
    emoji: str = ""  # create a new variable to display the emojis
    while index < len(secret):
        if secret[index] == guess[index]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret_word=secret, character=guess[index]):
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        index = index + 1
    return emoji


if __name__ == "__main__":
    main(secret="codes")
