all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

user_input = input()
count = 0
for char in user_input:
    if char in all_digits:
        count+=1
print(count)