from calculator_art import logo
print(logo)
def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

operations = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
def calculation():
  is_continue = True
  first = int(input("Enter the first number: "))
  while is_continue:
    for operation in operations:
      print(operation)
    operand = input("select an operation: ")
    second = int(input("Enter the next number: "))


    answer = operations[operand](first,second)
    print(f"{first} {operand} {second} = {answer}")

    check = input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation: ")
    if check == "y":
      first = answer
    else:
      calculation()

calculation()

