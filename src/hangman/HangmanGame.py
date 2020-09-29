from dataclasses import dataclass


@dataclass
class SecretWord:
    word: str
    status: list

    def __init__(self, word: str):
        self.word = word
        self.status = [False] * len(word)


class Hangman():
    """
    Main class for Hangman game, oversees game actions.

    See `Wikipedia article on Hangman <https://en.wikipedia.org/wiki/Hangman_(game)>`_
    """

    _word_to_guess = SecretWord("Akcja")

    def main(self):
        letter = input("Please guess one letter")
        self.display_word_to_user()

    def verify_letter(self, letter):
        """
        Verifies if provided letter is part of the word being guessed.
        :param letter: Letter which player provided.
        :return: True or False
        """
        pass

    def display_word_to_user(self):
        """
        Displays word with current guessed/not guessed status to the player.
        :return:
        """
        to_display = []
        for idx, value in enumerate(self._word_to_guess.status):
            if value:
                to_display.append(self._word_to_guess.word(idx))
            else:
                to_display.append("_")
        print(to_display)

    def is_over(self):
        """
        Checks whether game should end now. Game end means either of two:
            #. Player guessed the word properly
            #. Player exceed maximum number of guesses (since version 1.1)

        :return: True or False
        """
