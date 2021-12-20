#PRIME_NUMBER

def prime_checker(number):
  is_prime = True
  for i in range(3,int(number/2)+1):
    if number % i == 0:
      is_prime = False
      print(f"{number} is not a prime number")
      break
  if is_prime:
    print(f"{number} is a prime number")


n = int(input("Check this number: "))
if n % 2 == 0 or n==2 or n==1:
  print(f"{n} is not a prime number")    
else:
  prime_checker(number=n)