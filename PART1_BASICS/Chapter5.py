### Chapter 5: If statement

print()
print("Chapter 5: If statement")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# If statement is an expression that can be evaluated the condition is TRUE of FALSE.
# It's use a conditional test to decide whether the code should be executed.

# MATHEMATICAL COMPARISON & LOGICAL COMPARISON can be used for if statement to make specific decision.

cars = ['audi', 'bmw', 'mitsubishi', 'toyata']
for car in cars:
    if (car == 'bmw'):
        print(car.upper())
    else:
        print(car.title())

print("\n=========================================================\n")

print("Times to go school. Argh, is rainning...")
print("Do I have an umbrella?\n")

have_umbrella = True

if have_umbrella == True:
    print("Alright.. I have umbrella. Let's go school.")
else:
    print("I don't have any umbrella in house, just stay in house today. GAME TIME !!")

print("\n=========================================================\n")

favourite_fruits = ["Apple", "Orange", "Grapes", "Watermelon", "Banana"]

for fruit in favourite_fruits:
    if fruit in favourite_fruits:
        print("You really likes " + fruit + " !")

print("\n=========================================================\n")

# 如果一个 List 里是空的, 没有值。Python 会视它为 False 值。
listitem = ['one', 'two']
empty_list = []

if listitem:
    print(True)
else:
    print(False)

if empty_list:
    print(True)
else:
    print(False)

print("\n=========================================================\n")

current_users = ['Jean', 'Lisa', 'Diluc', 'Kaiya', 'Wendy']
new_uesrs = ['Amber', 'Rosaria', 'Wendy', 'Eula', 'Kaiya']

for user in new_uesrs:
    if user in current_users:
        print(user + ": Username already exists. Please try other.")
    else:
        print(user + ": The username is available.")

print("\n=========================================================\n")
print("Summary: If statement helps computer make decision to enhance program.")