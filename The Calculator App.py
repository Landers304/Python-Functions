#Task 1:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"
    return x / y




#Task 2: 


def what_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation! Please choose from '+', '-', '*', '/'.")

num1, num2 = what_numbers()

operation = get_operation()

print("Numbers:", num1, "and", num2)
print("Operation:", operation)




#Task 3: 


def what_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid! Please enter numeric values.")

def get_operation():
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation! Please choose from '+', '-', '*', '/'.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error! Unable to divide by 0."
        else:
            return num1 / num2

num1, num2 = what_numbers()

operation = get_operation()

result = calculate(num1, num2, operation)
print("Result:", result)
