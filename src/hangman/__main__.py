from src.hangman.HangmanGame import Hangman


def main(args=None):
    print("Welcome to Hangman game")
    secret_word = input("Please provide secret word for a player to guess: ")
    Hangman().main(secret_word)


if __name__ == '__main__':
    main()
