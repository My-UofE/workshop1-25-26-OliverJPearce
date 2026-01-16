import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    delta = next_val - current_val
    guessed_higher = user_input == "h"

    if delta > 0 and guessed_higher:
        return True
    
    if delta < 0 and not guessed_higher:
        return True

    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    pass
