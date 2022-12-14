def operation():
  question = input("Would you like to convert celcius or fahrenheit?")
  if question == "celcius":
      celcius_degree = float(input("What is the celcius degrees?"))
      farenheit_degree = celcius_degree * 1.8 + 32
      conversion = round(farenheit_degree, 1)
      print(f"It is {conversion} fahrenheit degrees outside!")
  elif question == "fahrenheit":
    fahrenheit_degree = float(input("What is the fahrenheit degrees?"))
    celcius_degree = fahrenheit_degree * 0.55 - 32
    conversion = round(celcius_degree, 1)
    print(f"It is {conversion} celcius degrees outside!")
  else:
      print("Please enter a valid answer :(")
running = True

while running:
    operation()
    close = input("Would you like to do another operation (yes/no)")
    if close == "no":
        running = False      
