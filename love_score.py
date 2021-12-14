print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

l_name = name1.lower()+name2.lower()

trueL = l_name.count("t") + l_name.count("r") + l_name.count("u") + l_name.count("e")

lovet = l_name.count("l") + l_name.count("o") + l_name.count("v") + l_name.count("e")

score = int(str(trueL)+str(lovet))

if score < 10 or score > 90:
 print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
 print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")   