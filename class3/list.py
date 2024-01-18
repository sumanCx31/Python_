# list in python
"""students  = ["suman","ritesh","sahil"]

roll = [1,2,3,4,5,6,7,8]

count_of_students = len(students)

roll_count=roll.__len__()

print(count_of_students,roll_count)"""

# list declaration with no elements in it

# Looping in python

roll = [1,2,3,4,5,6,7,8]

# for i in roll:
#   print(i)

# True, False, None
# i=0
# while( i<= 5):
#     print(i)
# i+=1

# students = []
# students.append("HCOE")
  
#   WAP in such a way that when user enters input "ram" as a name break loop and print the list ,otherwise 
#   keep on appending items to list and ask for next input from terminal..
name_list = ["suman"]
i=0
while(name_list[-1]!="hari"):
    i += 1
    name_list.append(input("enter your name:\n"))
    print(name_list)


