### Chapter 7: User Input and While Loops

print()
print("Chapter 7: User Input and While Loops")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# 在这个章节我们将学会用 input () 获取用户提供的信息来实现更有互动性的程序。
# 此外，还会用新的循环方式 while loop，只要条件成立，就可以一直保持运行程序。
# 获取的信息会被视为字符串，所以比较数字前要转换成 int 数据类型。

print("Notes: ")
print("The input function will pauses your program and waits for user to enter some text.")
print("Once Python receive the user's input, it can stores it into a variable to make convenient work.")

# Example
input_example = "\nEnter something, I will repeat it. Enter 'quit' to end this input."
# The operator '+=' take the first part string and adds the new string onto the end。 String also can use += operator。
input_example += "\nEnter here: "
message = ""

while message.lower() != 'quit':
    message = input(input_example)
    if message.lower() == 'quit':
        print("You choose to QUIT this input section.")
    else:
        print("Repeat message: " + message)

print("\n=========================================================\n")

# For Loops 用来循环一个列表里的数据和一个范围，而 While Loops 只要在条件成立的情况，甚至可以进入死循环。
# 如果真的进入了死循环停不下, 你可以使用ctrl + c 强行让程序终止。

print("While Looping")

current_number = 1                    # 当前号码等于1
while current_number < 5:             # 设定条件(1小于5), 如果结果是True就会一直循环，直到1大于5，或者...你电脑爆炸。
    print(current_number)             # 如果条件结果是True就一直print 号码1。
    current_number += 1               # 每一次print 了号码后，把当前的数字加1，循环一次加一次1。循环5次后current number就会大于5。

print("\n=========================================================\n")

print("While loops with break")

num = 1
while True:   # active flag variable
    print(num)
    num += 1

    if num == 10:
        print("Number = 10, break the program now.")
        break

print("\n=========================================================\n")

print("Summary: \n - This chapter learn how to use input to receive user information.")
print(" - Learn to use several ways to control while loop, by setting an active flag.")
print(" - Learned to use break and continue statement in looping.")
print(" - Learned how to use while loop to move items from one list to another list, and dictionary.")
