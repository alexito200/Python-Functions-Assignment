# Objective: The aim of this assignment is to build a basic calculator that can perform
# addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b


# Task 3: Ensure your code can handle division by zero and other potential errors.
# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator_app(a, b, operation):
    if operation == "addition":
        return addition(a, b)
    elif operation == "subtraction":
        return subtraction(a, b)
    elif operation == "multiplication":
        return multiplication(a, b)
    elif operation == "division":
        return division(a, b)
    else:
        return "Invalid Operation"

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

def main():
    operation = input("What operation would you like to perform: ")    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = calculator_app(a, b, operation)
    
    print(f"Here is your result = {result} ")
main()


