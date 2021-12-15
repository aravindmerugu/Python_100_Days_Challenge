import random

a = int(input("Choose 0 for Heads or 1 for Tails: "))

b = random.randint(0,1)
print(b)

if a==0:
  if b ==0:
    print("computer chooses heads, you won")
  else:
    print("computer chooses Tails, you lose")
if a==1: 
  if b ==1:
    print("computer chooses Tails, you won")
  else:
    print("computer chooses heads, you lose")











