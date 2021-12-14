print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size=="S" or size=="s":
  if add_pepperoni == "Y" or add_pepperoni == "y":
    bill = 17
  else:
    bill = 15

if size=="M" or size=="m":
  if add_pepperoni == "Y" or add_pepperoni == "y":
    bill = 23
  else:
    bill = 20
else:
  if add_pepperoni == "Y" or add_pepperoni == "y":
    bill = 28
  else:
    bill = 25

if(extra_cheese == "Y" or extra_cheese == "y"):
  bill+=1

print(f"Your final bill is: {bill}.")   

