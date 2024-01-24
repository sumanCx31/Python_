# Write a program that takes a number as input and prints its factorial using a while loop.

number = int(input("Enter a number:"))
i=1
fact=1
num = number
while(i<=number):
    fact=fact*num
    i=i+1
    num = num-1

print(f"The factorial of given number is {fact}.")