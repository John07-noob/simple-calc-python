# This SimpleCalc created by John07-noob
from function import inputNumber

print("Welcome to SimpleCalc")
while True:
  ask = input("Please choose operation here (+,-,/,*) ")   # Ask user for the operation
  if ask == "+":                                           # if else statement
    x = inputNumber("Insert number here: ")                 # Ask user input
    y = inputNumber("Insert number here: ")                 # Ask user input
    print(x + y)
  elif ask == "-":                                         
    x = inputNumber("Insert number here: ")                 # Ask user input
    y = inputNumber("Insert number here: ")                 # Ask user input
    print(x - y)
  elif ask == "/":
    x = inputNumber("Insert number here: ")                 # Ask user input
    y = inputNumber("Insert number here: ")                 # Ask user input
    print(x / y)
  elif ask == "*":
    x = inputNumber("Insert number here: ")                 # Ask user input
    y = inputNumber("Insert number here: ")                 # Ask user input
    print(x * y)
  else:
    print("Enter the valid Operation Please!")
