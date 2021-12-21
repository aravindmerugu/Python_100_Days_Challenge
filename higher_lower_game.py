from higher_lower_game_data import data
import random
from higher_lower_art import logo, vs
from replit import clear

print(logo)

inf_data = data
compareA = inf_data[random.randint(0,len(inf_data)-1)]
inf_data.remove(compareA)
score = 0

def print_info(user_info):
  return f'{user_info["name"]}, a {user_info["description"]}, from {user_info["country"]}.'

def score_count(compareA,score):
  print("You're Right")
  score+=1
  clear()
  print(logo)
  game(compareA,score)

def game(compareA,score):
  compA_score = compareA["follower_count"]
  print(f'Compare A: {print_info(compareA)}')
  print(vs)
  compareB = inf_data[random.randint(0,len(inf_data)-1)]
  compB_score = compareB["follower_count"]
  print(f'Compare B: {print_info(compareB)}')
  inf_data.remove(compareB)

  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if answer == "a" and compA_score >= compB_score:
    score_count(compareB,score)
  elif answer == "b" and compB_score >= compA_score:
    score_count(compareB,score)
  else:
    clear()
    print(logo)
    print(f"sorry that's wrong final score is {score}")  

game(compareA,score)