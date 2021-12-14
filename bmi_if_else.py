#bmi_suggestions

w = int(input("Enter your weight "))
h = float(input("Enter your height "))
bmi = round(float(w/h**2),2)

if bmi < 18.5:
  print(f"your BMI is {bmi}, you are underweight")
elif bmi < 25:
  print(f"your BMI is {bmi}, you are normal")
elif bmi < 30:
  print(f"your BMI is {bmi}, you are overweight")
elif bmi <35:
  print(f"your BMI is {bmi}, you are obese")
else:
  print("clinically obese")      
