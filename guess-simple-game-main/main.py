def difficulty_executor(attempts_number):
    """The function that executes the game. 
    
    It takes a single argument, the number of attempts, and continues to ask the player to make a guess until they run out of attempts or they guess the correct answer.

    Args:
    attempts_number (int): the number of attempts the player has to guess the correct number.

    Returns:
    None
    """
    is_gameover = False
    while not is_gameover:
        # Prompt the player to make a guess
        guess = int(input('Please make a guess: '))
        if guess < number_to_guess:
            print('Too low.')
            attempts_number -= 1
            # Check if the player has run out of attempts
            if attempts_number == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = True
            else:
                # Let the player know how many attempts they have left
                print(f'You have {attempts_number} remaining to guess the number.\nGuess again.')
        elif guess > number_to_guess:
            print('Too high.')
            attempts_number -= 1
            # Check if the player has run out of attempts
            if attempts_number == 0:
                print('You\'ve run out of guesses, you lose.')
                is_gameover = True
            else:
                # Let the player know how many attempts they have left
                print(f'You have {attempts_number} remaining to guess the number.\nGuess again.')
        elif guess == number_to_guess:
            is_gameover = True
            print(f'You got it! The answer was {number_to_guess}')

def difficulty_adjuster(difficulty_level):
    """Adjusts the difficulty level of the game.
    
    It takes a single argument, the difficulty level, and sets the number of attempts the player has to guess the correct number accordingly.

    Args:
    difficulty_level (str): the difficulty level of the game, either 'easy' or 'hard'.

    Returns:
    None
    """
    if difficulty == 'easy':
        # Set the number of attempts for the 'easy' difficulty level
        attempts_number = 10
        print(f'You have {attempts_number} attempts remaining to guess the number')
        difficulty_executor(attempts_number)

    elif difficulty == 'hard':
        # Set the number of attempts for the 'hard' difficulty level
        attempts_number = 5
        print(f'You have {attempts_number} attempts remaining to guess the number')
        difficulty_executor(attempts_number)

        
# Import the logo for the game
from Graphics import logo

# Import the random module for generating random numbers
import random

# Show the game logo
print(logo)

# Welcome the player to the game
print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100')

# Ask the player if they want to play the game
answer = input('Do you want to play the Number Guessing Game!? Type \'yes\' or \'no\': ')

# Start the game
while answer == 'yes':
    # Generate a random number for the player to guess
    number_to_guess = random.randint(1, 100)
    print(f'Pssst, the correct answer is {number_to_guess}')

    # Ask the player to choose a difficulty level
    difficulty = input('Choose a difficulty level. Type \'easy\' or \'hard\': ')

    # Start the game with the chosen difficulty level
    difficulty_adjuster(difficulty)

    # Ask the player if they want to play again
    answer = input('Do you want to play again? Type \'yes\' or \'no\': ')

    # Continue playing if the player wants to
    while answer == 'yes':
        # Generate a new random number for the player to guess
        number_to_guess = random.randint(1, 100)
        print(f'Pssst, the correct answer is {number_to_guess}')

        # Ask the player to choose a new difficulty level
        difficulty = input('Choose a difficulty level. Type \'easy\' or \'hard\': ')

        # Start the game with the new chosen difficulty level
        difficulty_adjuster(difficulty)

        # Ask the player if they want to play again
        answer = input('Do you want to play again? Type \'yes\' or \'no\': ')
