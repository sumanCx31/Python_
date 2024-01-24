# Implement a program that calculates and prints the sum of digits of a given number using a while loop.


number = int(input("Enter a number: "))

digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum = digit + digit_sum
    number //= 10

print(f"The sum of digits is: {digit_sum}")
