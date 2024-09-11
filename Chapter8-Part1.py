### Chapter 8: Functions Part I

print()
print("Chapter 8: Functions Part I")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")


# Functions: 字面上的意思，它就是一个功能。你可以创造一些功能让你以后可以更有效率的使用重复性的代码。
# 你可以通过呼叫function 的名字来执行特定的任务。

# 比如我写了一个简单的功能, 命名为greetings。它的功能就是使用print functions打个招呼。
# 但这个functions 不会立即执行任务，而是要呼叫functions name, 也就是 greetings() 才会执行打招呼的任务。

# Keyword 'def' as define a functions named 'greetings'。那个括号可以用来储存数据。
# This function will not execute, unless below have called its name.
def greetings():
    # Task this function need to do when his name has called.
    print("Hi, nice to meet you! I am greetings function.")


# call function name three times, it will execute functions three time.
greetings()
greetings()
greetings()

print("\n=========================================================\n")

# 我们写一个print()，就是呼叫了这个功能, print是它的function name，它的任务是打印出括号里面的文字。
print("我就是functions, 我的名叫print, 我的任务是打印出括号里的数据。")

# 为什么要使用 functions? 如果你想要执行一个任务很多次，一直重复写它的任务很麻烦。
# 把它写成一个功能后，每一次要用只需要呼叫 function names 就会执行functions 里的代码。 这样把功能一个一个分开能让你的代码更容易阅读, 写, 测试和修改。

# 数字相加的功能, 我就不用一直写num1 + num2
# 而是直接 call functions name，给两个数字就有结果了。

print("\nAdd number functions: ")


# 括号有两个变量储存两个数字的数据类型，它的任务是让括号的两个数字相加
def add_number(num1, num2=2):  # num1 and num2 is 'parameter' that will receive value when function called.
    print(num1 + num2)         # parameter num2 default value is 2.


# 呼叫functions后，括号里的数字传到num1, num2
add_number(1, 1)  # 把两个数字1分别存在num1 & num2里           # 1 is 'arguments' that the value will pass to function
add_number(2, 8)  # 把两个数字 2和8 分别存在num1 & num2里      # 2 and 8 is 'arguments' that the value will pass to function

print("\n=========================================================\n")

# Arguments & parameters
print("Arguments & parameters")
print("Parameters 参数，refers to variable inside the functions parentheses. Used to receive the value passed in when function is called.")
print("Arguments 实参，refers to the value passed to the function when it is called.")

# Functions doesn't always have to display output. Instead, it can process some data and return the value. It's called 'return value'.

# Return statement
print("\nReturn Statements: ")


def get_fullname(first_name, middle_name, last_name=""):
    full_name = first_name + middle_name + last_name
    return full_name


name = get_fullname("Michael ", "Jackson")
print(name)
name = get_fullname("Wong ", "Yong ", "Qin")
print(name)

print("\n=========================================================\n")

# To Be Continued at page 180
print("Summary: In this Chapter 8 - Part 1, we have learned functions.")
print(" - Simply define and called functions.")
print(" - Know about parameters and arguments and use it to pass value when functions called.")
print(" - Learn some arguments optional, Keyword Arguments, Positional Arguments, Default Values, etc.")
print(" - Learn to use return statement to return values from functions.")
