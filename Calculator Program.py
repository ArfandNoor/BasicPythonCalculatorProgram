#Calculator Program

operator = input("Choose your operator (+, -, *, /): ")
number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))

if operator == "+":
    result = (number1 + number2)
    print(f"your answer is {result}")
elif operator == "-":
    result = number1 - number2
    print(f"your answer is {result}")
elif operator  == "*":
    result = number1 * number2
    print(f"your answer is {result}")
elif operator == "/":
    result = number1 / number2
    print(f"your answer is {result}")
else:
    print(f"{operator} is not a valid operator")