import random
from guess_the_number_art import logo

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1,100)

def set_difficulty():
  level = input("choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def check_lives(attempts):
  if attempts == 0:
    print(f"You've run out of guesses, you lose. the number is {number}")
  else:
    guess_the_number(attempts)    

def guess_the_number(attempts):
  print(f"you have {attempts} attempts remaining to guess the number: ")
  choose = int(input("Make a guess: "))
  if choose == number:
    print("You Guessed it right! you won")
    return
  elif choose > number:
    print("Too High")
    attempts-=1
    check_lives(attempts)
  elif choose < number:
    print("Too low")
    attempts-=1
    check_lives(attempts)  

guess_the_number(set_difficulty())    