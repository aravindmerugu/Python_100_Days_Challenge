import random
from replit import clear
from blackJack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
to_play = True
def play_blackjack():
  h_first = random.choice(cards)
  h_second = random.choice(cards)
  human_list = [h_first,h_second]
  c_first = random.choice(cards)
  c_list = [c_first]
  print(logo)
  print(f"your cards: {human_list}, current score: {sum(human_list)}")
  print(f"computer's first card: {c_list}")

  def print_score():
    if len(c_list) == 1 and sum(human_list) >=21:
      nextt = random.choice(cards)
      c_list.append(nextt)
    print(f"your Final cards are: {human_list}, current score: {sum(human_list)}")
    print(f"computer's cards are: {c_list}, current score: {sum(c_list)}")

  def blackJack_fun():
    def human_fun():  
      nextt = random.choice(cards)
      human_list.append(nextt)
      if nextt == 11 and sum(human_list) > 21:
        human_list.remove(11)
        human_list.append(1)
      if sum(human_list)>21:
        print_score()
        print("you went over. you lose")
        return
      elif sum(human_list) == 21:
        print_score()
        print("you won")
        return
      print_score()  
      blackJack_fun()   

    def computer_fun():
      nextt = random.choice(cards)
      c_list.append(nextt)
      if nextt == 11 and sum(human_list) > 21:
        human_list.remove(11)
        human_list.append(1)    
      if len(c_list) == 2:
        print(f"computer's first two cards are {c_list}, current score {sum(c_list)}")
      if sum(c_list)>21:
        print_score()
        print("computer went over. you won")
        return
      elif sum(c_list) == 21:
        print_score()
        print("computer wins")
        return
      elif sum(c_list) < 17:
        computer_fun()
      else:
        if sum(c_list) > sum(human_list):
          print_score()
          print("computer score higher. computer wins")      
          return
        elif sum(c_list) == sum(human_list):
          print_score()
          print("both score's equal it's a draw")
          return  
        else:
          print_score()
          print("you score higher! you won")
          return    
    select = input("Type 'y' to continue or 'n' to pass: ")
    if select == 'y':
      human_fun()
    else:
      computer_fun()
  blackJack_fun()

while to_play:
  check = input("Do you want to play a game of BlackJack type 'y' or 'n': ")
  clear()
  human_list = []
  c_list = []
  if check == 'y':
    play_blackjack()
  else:
    to_play = False  