import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("1. for rock\n2. for paper\n3. scissors\nchoose: "))
#system_choice = random.randint(1,3)
def play_game():
  game = [rock,paper,scissors]
  print(f"you chose {game[user_choice-1]}")
  system_choice = random.choice(game)
  print(f"system chose {system_choice}")

  if(game[user_choice-1]==system_choice):
    print("it's a draw")
    
  elif (user_choice-1==0 and game.index(system_choice)==2) or (user_choice-1==2 and game.index(system_choice)==1)or (user_choice-1==1 and game.index(system_choice)==0):
    print("you wins!")
  else:
    print("you lose")

if user_choice >=4 or user_choice <=0:
  print("invalid choice")
else:
  play_game()  