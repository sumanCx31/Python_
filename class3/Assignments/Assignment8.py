
# Write a Python program to check if a given string is a palindrome

a = input("Enter a string:")
b = a[-1::-1]

if(a==b):
    print("The given string is palindrome!")
else:
    print("The given string is not palindrome!")