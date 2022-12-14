print("Welcome to Fast Fried Chicken!")
chicken = input("How many fried chickens do you want? 4, 6, or 8 ")
dipping = input("Do you want dip sauce? Y or N ")
drink = input("Do you want a drink? Y or N ")

bill = 0


if chicken == "4":
  bill += 50
elif chicken == "6":
  bill += 70
elif chicken == "8":
  bill += 90

if dipping == "Y":
  if chicken == "4":
    bill += 5
  else:
    bill += 7

if drink == "Y":
  bill += 10

print(f"Your total bill is {bill}")