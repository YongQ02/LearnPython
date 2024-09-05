### Chapter 6: Dictionaries

print()
print("Chapter 6: Dictionaries")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Dictionary in python is collection of key value pair.
# Key is connected to value.
# Key value can be a string, a number, a list or even another dictionary. 
# 字典用 大括号{} 来定义, 大括号里储存 {Key:Value} ，并用逗号间隔。

my_guitar = {'guitar type':'acoustic guitar', 'brand':'Cort', 'price':500}
print("My " + my_guitar['guitar type'] + " costs " + str(my_guitar['price']) + " ringgit.")

print("\n=========================================================\n")

character_hair_color = {'Alice': 'red', 'Roxy': 'blue', 'sylphy': 'green', 'elinalise': 'gold', 'zenith': 'gold'}

# 如果要用 for 循环字典，需要使用 items() to returns a list of key-value pairs.
for name, hair_color in character_hair_color.items():
    print(name + " hair color is: " + hair_color)

print("\n=========================================================\n")

users = {
    'Ben': {
        'name':'Yong',
        'age': 21,
        'gender':'male',
    },
    'Henry':{
        'name':'Min',
        'age': 22,
        'gender':'male',
    }
}

for username, information in users.items():
    name = information['name']
    age = str(information['age'])

    print("\nUsername: " + username)
    print("\tFullname: " + name)    
    print("\tAge: " + age) 
    print("\tGender: " + information['gender'])

print("\n=========================================================\n")

print("Summary: This chapter learn to define a dictionary and work with the information.")
print("Moreover, learn to access, modify and loop on the dictionary. ")
print("I also learned how to nest multiple dictionary in list, list in dictionary or dictionary in dictionary.")