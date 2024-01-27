# Create a program that uses a loop to print the multiplication table of a given number. 

number = int(input("Enter a number:"))


print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
