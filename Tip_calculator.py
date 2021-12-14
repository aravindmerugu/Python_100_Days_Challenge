#tip_calculator
original_bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
tip = int(input("What percentage would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

final_bill = (original_bill+(tip/100)*original_bill)/people

print(f"Each person should pay ${round(final_bill,2)}")