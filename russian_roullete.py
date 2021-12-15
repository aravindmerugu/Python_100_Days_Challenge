#sol_1
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
index = random.randint(0,len(names))

print(f"{names[index]} has to pay the bill")

#sol_2
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{random.choice(names)} has to pay the bill")