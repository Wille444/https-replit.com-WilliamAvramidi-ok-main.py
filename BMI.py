weight = float(input("What is your weight?"))
height = float(input("What is you height in m?"))

bmi = int(weight / height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi} and you are underweight")
elif bmi <= 25:
  print(f"Your BMI is {bmi} and you have a normal weight")
elif bmi <=30:
  print(f"Your BMI is {bmi} and you are slightly overweight")
elif bmi <= 35:
  print(f"Your BMI is {bmi} and you are obese")
else:
  print(f"Your BMI is {bmi} and you are clinically obese")