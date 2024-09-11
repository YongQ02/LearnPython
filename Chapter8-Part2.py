# Chapter 8: Functions Part II
# Start from page 180

print()
print("Chapter 8: Functions Part II")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")


# Pass a list to the function
def greeting_names(names):
    for name in names:
        print("Hi, my name is " + name)


namelist = ['Qin', 'Jun', 'Sheng']
greeting_names(namelist)

print("\n=========================================================")


# 传递任意数量的参数 Passing an Arbitrary Number of Arguments (*parameters)
# The systax works no matter how many arguments the functions receive.
def favourite_fruits(*fruits):
    print("\nYour favourite food is: ")

    for fruit in fruits:
        print("- " + fruit)


favourite_fruits('apple')
favourite_fruits('apple', 'orange', 'banana', 'grapes')

print("\n=========================================================\n")

# Store your functions as a Module
print("Store your functions in a separate file called a module.")
print("Use import statement tells Python to make the module available in the currently running program file.")
print("It allows developer to reuse functions in many different programs.")

# Let's get start ! Import the file as module
import Function_Example as file

file.greeting()  # to use the function, write the 'FILE_NAME.FUNCTION_NAME'

print("\n=========================================================\n")

# End with page 193
print("Summary: In this Chapter 8 - Part 2, we continue to learn functions.")
print(" - Passing list to function")
print(" - Passing an Arbitrary Number of Arguments to function.")
print(" - Learn to write functions in other files.")
print(" - Use import statement to import functions from other program files.")
print(" - Learned different ways to import modules and call functions name.")   
