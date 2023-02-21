from random import choice
from art import logo
from art import vs
from game_data import data
import os


def clear_console():
    # This line sets the 'command' variable to the string 'clear'
    command = 'clear'
    
    # This line checks if the current operating system is 'nt' (Windows) or 'dos' (MS-DOS)
    if os.name in ('nt', 'dos'):
        # If the operating system is Windows or MS-DOS, change the value of 'command' to 'cls'
        command = 'cls'
    
    # This line runs the system command specified in the 'command' variable
    os.system(command)


def compare(A, B):
    # This line compares the 'follower_count' values of two dictionaries A and B
    if A['follower_count'] > B['follower_count']:
        # If the 'follower_count' of A is greater than B, return 'A'
        return "A"
    elif A['follower_count'] < B['follower_count']:
        # If the 'follower_count' of B is greater than A, return 'B'
        return 'B'

def compare_dict(A, B):
    # This line compares the 'follower_count' values of two dictionaries A and B
    if A['follower_count'] > B['follower_count']:
        # If the 'follower_count' of A is greater than B, return dictionary A
        return A
    elif A['follower_count'] < B['follower_count']:
        # If the 'follower_count' of B is greater than A, return dictionary B
        return B


def score_count(guess, answer, score):
    # This line compares the 'guess' and 'answer' values
    if guess == answer:
        # If the values are equal, return the updated score value (score + 1)
        return score + 1
    else:
        # If the values are not equal, return the original score value
        return score


def game():
    A = choice(data)
    B = choice(data)
    score = 0
    print(logo)
    print(f"Cormpare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    answer = compare(A, B)
    answer_dict = compare_dict(A, B)
    guess = input('Who has more followers? Type \'A\' or \'B\': ')
    score = score_count(guess, answer, score)
    while guess == answer:
        clear_console()
        dynamic_variable = choice(data)
        if dynamic_variable == answer_dict:
            dynamic_variable = choice(data)
        print(f'{logo}\nYou\'re right! Current score: {score}')
        print(f"Cormpare A: {answer_dict['name']}, a {answer_dict['description']}, from {answer_dict['country']}.")
        print(vs)
        print(f"Against B: {dynamic_variable['name']}, a {dynamic_variable['description']}, from {dynamic_variable['country']}.")
        guess = input('Who has more followers? Type \'A\' or \'B\': ')
        answer = compare(answer_dict, dynamic_variable)
        score = score_count(guess, answer, score)
        answer_dict = compare_dict(answer_dict, dynamic_variable)
    print(f'Sorry, that\'s wrong. Final score {score}')

game()
