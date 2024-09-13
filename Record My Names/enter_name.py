import json
filename = 'name.json'


def store_name():
    name = input("Hi, please enter your name: ")

    with open(filename, 'a') as file_obj:
        json.dump(name, file_obj)
        print("We'll remember your name when you come back, " + name + "!")


def load_name():
    with open(filename) as file_obj:
        content = json.load(file_obj)
        print("\nLoading data is successfully: \n" + "Welcome back, " + content + "!")


print("Hi, welcome ! You want to 'store name' or 'load name' ? ")
task = input(": ")

if task == "store name":
    store_name()
elif task == "load name":
    load_name()
else:
    print("No specific task, see you again !")
