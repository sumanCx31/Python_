# Implement a program that counts the number of vowels in a given string using a loop.

String = "Hello world"
vowels = 0
n = len(String)

print(f"Length of the string: {n}")

for i in range(n):
    if String[i] in 'aeiouAEIOU':
        vowels += 1

print(f"Number of vowels in the string: {vowels}")


