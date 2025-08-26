# Basic Calculator

# Ask the user for two numbers
number1 = float(input("Type the first number: "))
number2 = float(input("Type the second number: "))

# Ask the user what operation to do
operation = input("Type + for add, - for subtract, * for multiply, / for divide: ")

# Do the calculation
if operation == "+":
    print(number1, "+", number2, "=", number1 + number2)
elif operation == "-":
    print(number1, "-", number2, "=", number1 - number2)
elif operation == "*":
    print(number1, "*", number2, "=", number1 * number2)
elif operation == "/":
    if number2 != 0:
        print(number1, "/", number2, "=", number1 / number2)
    else:
        print("Oops! Cannot divide by zero.")
else:
    print("Sorry, that is not a correct operation.")
