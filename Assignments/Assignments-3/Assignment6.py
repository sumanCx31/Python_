# Write a function remove_duplicates(input_list) that takes a list as an argument and returns a new list with duplicates removed using a set.

def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print("Original List:", my_list)
print("List with Duplicates Removed:", result)

