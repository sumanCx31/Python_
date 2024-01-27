# Reverse a given string without using the reverse function or slicing.

string = "helloworld"
length = int(len(string))
# print(length)

length=length-1

for i in string:
    print(string[length],end="")
    length=length-1
