num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Can't divide by zero!")
else:
    print("Invalid operation !")

