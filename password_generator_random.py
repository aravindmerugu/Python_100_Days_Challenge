#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
for number in range(0,nr_symbols):
  password+=random.choice(symbols)
for number in range(0,nr_numbers):
  password+=random.choice(numbers)
for number in range(0,nr_letters-nr_numbers-nr_symbols):
  password+=random.choice(letters)
res_pwd = list(password)
random.shuffle(res_pwd)
pwd_str = ''.join([str(element) for element in res_pwd])

#str_pwd = ' '.join([str(element) for element in res_pwd])
print(f"Your password is {pwd_str}")
