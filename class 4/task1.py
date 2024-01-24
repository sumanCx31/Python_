'''user = {
    "name":"suman",
    "age":"19",
    "address":"NAPAL",
}

print(user.get("name"))
print("Full Name Is",user.get("full_name","No Name"))
breakpoint()


# getting keys of Dict
print(user.keys())

# getting Values of Dict
print(user.values())

# setting new keys of Dict
user.setdefault("Hobby","Cricket")
user["Goat"]="Greatest of all time"

print(user.keys())
'''

"""WAP to get name ,age religion,father_name,mother_name,college_name, as inputs from terminal. Declare an empty dict Add these key 
value pairs to a dictionary and print result"""


key_list = ["name","age","religion","college_name"]

user_detail = {}

for i in key_list:
    # user_detail.setdefault(i,input(f"Enter your {i}\n"))
    user_detail.__setitem__(i,input(f"Enter your {i}\n"))

print(user_detail)


# Magic Methods

for i in user_detail:
    print(i)
breakpoint()