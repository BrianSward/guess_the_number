## MY CODE BELOW, HERS VERY BOTTOM USES FUNCTIONS
#Number Guessing Game Objectives:

import random
# print("Welcome to a Number Guessing Game")
# print("The number will be between 1 - 100.")

# response = input("Choose a difficulty. Type 'easy' or 'hard': ")
# if response == "hard":
#     lives = 5
# else:
#     lives = 10
# print(f"You have {lives} lives remaining")

 
# target = random.randint(1,100)
# print(target)
# guess = int(input("Make a guess: "))
# while guess != target and lives > 1:
#     if guess > target:
#         lives -= 1
#         print(f"too high, guess again, you have {lives} guesses remaining")
#         guess = int(input("Make a guess (GT): "))
#     elif guess < target:
#         lives -=1
#         print(f"too low, guess again, you have {lives} guesses remaining")
#         guess = int(input("Make a guess(LT): "))
        
# if lives == 0:
#     print(f"you lose, the number was {target}")
# else:
#     print(f"You win, the number was {target}")

## HER CODE BELOW, MINE ABOVE, BOTH WORK


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"You win!, it was {answer}")

def set_difficulty():
    response = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if response == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS

def guessing_game():
    print("Welcome to a Number Guessing Game")
    print("The number will be between 1 - 100.")
    answer = random.randint(1,100)
    turns = set_difficulty()
    # print(f"Hint: {answer}")
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} guesses remaining")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You're out of turns, you lose.")
            return

guessing_game()
