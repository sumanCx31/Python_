# Python Condition 

user_detail_first = {
    "name":"suman",
    "age":"19",

}

user_detail_second = {
    "country":"Nepal",
    "Hobby":"cricket",

}
# Merging two dict
user_detail = {
    **user_detail_first,
    **user_detail_second,
    "ph_number":"98*********"
}

print(user_detail)

# Merging two or more list

student1 = ["Ms.Dhoni","virat","Rohit"]
student2 = ["Ishan","Surya","Deepak"]

student = [*student1,*student2,"David"]

print(student)
