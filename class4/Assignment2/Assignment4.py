# Write a program to print a pattern of stars in the shape of a right-angled triangle

# a = int(input("enter the rows:"))
# b = int(input("enter the Columns:"))



# Get the number of rows and columns from the user

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Generate and display the multiplication table matrix
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print(f"{i * j}\t", end="")
    print(4)
