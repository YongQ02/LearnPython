# Chapter 10: Files and Exceptions - Part II [Exceptions]

print()
print("Chapter 10: Files and Exceptions - Part II [Exceptions]")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Python can use special objects called exceptions to manage errors during program executing. We can write code to handle exceptions.
# Exceptions are handled with try-except-else blocks.
# 使用了这个try-except-else后，程序就算出错也会继续运行，而不是显示一些难看的 '红色错误文字'

# 让我们尝试一个错误的运算，这个运算会产生错误并提示 'ZeroDivisionError: division by zero'
# 这个 'ZeroDivisionError' 就是我们的异常对象, 可以指定这错误信息作为异常处理。
try:
    division = (5/0)
except ZeroDivisionError:
    print("You can't divide by Zero ! This will make programs error !")
else:
    print(division)
# 我们用 try-except-else 告诉 Python 先尝试运行这些代码，如果看到'ZeroDivisionError'这个错误，就给它运行另外一个任务。(发生这个事情的话，就进行plan b，类似这样。)

# ===================================================================================================================================================

# FileNotFoundError Exception (When the file in different location or doesn't exist)
print()
file = 'alice.txt'

try:
    with open(file) as testing_file:
        content = testing_file.read()
except FileNotFoundError:
    message = "Sorry, the file " + file + " doesn't exist."
    print(message)

print("\n=================================================================================\n")

# Storing Data with Json
# 目前我们程序的缺点就是获取用户的数据只能在程序运行时被储存。当程序停止再重新开始，之前从用户获取的数据会消失。
# 要让获取的数据永久保存到文件，每一次执行都能使用用户数据的话，我们需要使用json模块。json模块也能用来分享数据到其它程序。
print("JSON: JavaScript Object Notation, developed for JavaScript.")

# json.dump()  To store the set of numbers, takes two arguments (data to store, file object)。
import json   # import json module before used.

numbers = [2, 3, 5, 7, 11, 13]        # Create a list and store a set of numbers.
filename = 'numbers.json'             # store file name in this variable
with open(filename, 'w') as file_obj:  # Open 'numbers.json' file in 'write mode'.
    json.dump(numbers, file_obj)       # json.dump() function, 'store a list of numbers' in 'numbers.json' file.

# json.load()  To load and read the data back into memory.

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print("Data has successfully loads from " + filename + ": " + str(numbers))

print("\n=================================================================================\n")

print("Summary: Chapter 10 - Part 2 we learned: ")
print("- Put some exception to handle exceptions, avoid error hint.")
print("- Learned to store Python data structures, which allow to save and load information from users provide.")
