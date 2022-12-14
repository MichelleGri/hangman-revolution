"""
module and file imports
"""

import random
import sys
from hangman_movies import movies_list
from hangman_stages import stages
from hangman_logo import LOGO


def random_movie():
    """
    function to choose a random movie from movies_list

    Returns: random movie in all uppercase letters
    """
    movie = random.choice(movies_list)
    return movie.upper()


def play_game(movie):
    """
    function to play game

    Arg:
    - movie (str) : random movie chosen from the random_movie function

    set initial variables and values
    display underscores for number of letters in movie

    create while loop to run while player is guessing letters:

        ask player to guess a letter

            Validation:
                check if input is valid - an alphabet
                    if valid - check if letter is in movie
                    if invalid - ask player to input only one letter A-Z
                check if letter has already been guessed
                    if already guessed - ask player to guess a different letter

            Game play:
                check if guessed letter is in movie title
                    if yes - replace underscore with guessed letter
                    if no - guess is wrong, decrease lives, draw hangman
                check if game over
                    if there are no more underscores in display - game is won
                    if number of lives is 0 - game is lost
    """
    print(LOGO)
    print("  Let's play Hangman! \U0001F929")
    print("  Guess the movie! \U0001F3AC")
    player_lives = 6
    print(stages[player_lives])
    game_over = False
    guessed_letters = []
    display = []
    movie_length = len(movie)

    for letter in movie:
        if letter == " ":
            display += " "
        else:
            display += "_"
    print(' '.join(display))
    print("\n")

    while not game_over and player_lives > 0:
        guess = input("  Please guess a letter:\n\n").upper().strip()
        print("  \n")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(LOGO)
                print(f"  You already guessed the letter {guess},\n  guess another letter! \U0001F913")
                print("\n")
                print(' '.join(display))

            elif guess not in movie:
                print("/n")
                print(LOGO)
                print(f"  The letter {guess} is not in this movie! \U0001F60A")
                print("\n")
                player_lives -= 1
                guessed_letters += guess
                print(' '.join(display))
            else:
                for position in range(movie_length):
                    letter = movie[position]
                    if letter == guess:
                        display[position] = letter
                print("\n")
                print(LOGO)
                print(f"  Well done! The letter {guess} is in the movie! \U0001F389")
                print("\n")
                print(' '.join(display))
                guessed_letters += guess

                if "_" not in display:
                    game_over = True
                    print(LOGO)
                    print("  Congratulations! You guessed the correct movie! \U0001F3C6")
                    print("\n")
                    print(f"  {movie}")
                    print("\n")
            if player_lives == 0:
                game_over = True
                print(LOGO)
                print(f"  You lost the game! \U0001F4A5\n\n  The movie was {movie}! \U0001F39E")
                print("\n")
            print(stages[player_lives])

        else:
            print(LOGO)
            print("  Invalid guess, please enter one letter from A to Z only! \U0001F610")
            print("\n")


def restart_game():
    """
    function to restart game

    ask player is they want to play again
        if yes - while loop to start game, continues until player enters N
        if no - exit system
        validation - if input is not Y or N, ask player to enter valid input
    """
    game_over = True
    while game_over:
        play_again = input("  Do you want to play again? Y/N:\n").upper().strip()
        print("  \n")
        while play_again == "Y":
            main()
        if play_again == "N":
            print("  Thank you for playing Hangman Revolution! \U0001F601")
            print("\n")
            sys.exit()
        else:
            print("  Invalid input ... enter Y to play again or N to exit")
            print("  \n")


def main():
    """
    main function to start the game
    """
    movie = random_movie()
    play_game(movie)
    restart_game()


main()
