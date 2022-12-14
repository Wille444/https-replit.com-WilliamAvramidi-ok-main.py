print("Welcome to retarded love score")
name1 = input("What is your name?")
name2 = input("What is their name?")
name_combined = name1 + name2
name_combined_lower = name_combined.lower()
print(name_combined_lower)
t = name_combined_lower.count("t")
r = name_combined_lower.count("r")
u = name_combined_lower.count("u")
e = name_combined_lower.count("e")
true = t + r + u + e
l = name_combined_lower.count("l")
o = name_combined_lower.count("o")
v = name_combined_lower.count("v")
e = name_combined_lower.count("e")
love = l + o + v + e
core = int(str(true) + str(love))
if score < 10 or score > 90:
  print(f"Your score is {score} and you are made for each other")
elif score > 40 and score < 50:
  print(f"Your score is {score} and you guys will do just fine")
else:
  print(f"Your score is {score} and you are okey")