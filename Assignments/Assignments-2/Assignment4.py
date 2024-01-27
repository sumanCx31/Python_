# Define a list of numbers
numbers = [5, 8, -3, 12, 7, -1, 10]

# Iterate over the list
for num in numbers:
    if num < 0:
        print(f"Negative number encountered: {num}")
        break

    print(f"Processing number: {num}")
