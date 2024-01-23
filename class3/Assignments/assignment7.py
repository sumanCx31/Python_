# Write a Python program to print the Fibonacci sequence up to a certain number using a loop.

number = int(input("Enter the number: "))

a, b = 0, 1

while a <= number:
    print(a, end=" ")
    a, b = b, a + b
