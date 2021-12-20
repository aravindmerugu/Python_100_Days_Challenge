from replit import clear
from silent_auction_art import logo

print(logo)
print("Welcome to the secret auction program")
max_bid = 0
bid_dic = {}
def add_bidding(name,bid):
  bid_dic[name]=bid  

is_other_bidder = True
while is_other_bidder:
  name = input("what is your name?: ")
  bid = int(input("what's your bid?: $"))
  add_bidding(name,bid)
  other_bidders = input("are there any other bidders? Type 'YES' or 'NO': ").lower()
  if other_bidders == "no":
    is_other_bidder = False
  else:
    clear()

for name in bid_dic:
  if bid_dic[name]>max_bid:
    max_bid = bid_dic[name]
    winner = name
  
print(f"The winner is {winner} with a bid of ${max_bid}")