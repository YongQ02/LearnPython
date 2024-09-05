### Chapter 4: Working with Lists by Looping

print()
print("Chapter 4: Working with Lists")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Looping 是程序语言的特殊名词，中文叫循环。就如字面意思, 当条件成立便会重复循环执行任务。
# Python looping 有两种, 分别是 for loop 和 while loop。
# For looping 有两种用法, 分别是loop with list 和 loop in range。

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Just print a whole list\nLists without looping: ")
print(numbers_list)

print("\nprint every value in the list, if there is no more value inside the list, stop looping.\nLists with looping: ")
# Explanation: For every number value in the list of numbers, print all the number value.
for every_number_value in numbers_list:
    print(str(every_number_value) + " is a number.")
print("Looping is finished!")

print("\n=========================================================\n")

print("For number in range from 1 ~ 5, print all the number in range: ")
for number in range(1,5):
    print(number)

print("\nExplanation:")
print("There are two parameter value for range function.")
print("First value is to start counting, which is '1' and stop looping when it reaches second value, which is 5.")
print("The output never contains the end value, so 5 will not printed.")

print("\n=========================================================\n")

# Tuple
# List 和 Tuple 类似, 它们的分别是 List 的值可以更改，而 Tuple 也是列表的一种, 但是里面的值不能够更改 / immutable 不可变的。
# Tuple 用 () 括号 来定义，而不是 [] 正方括号
print("Normal List: List")
print("Immutable List : Tuple\n")


print("\nSummary: Looping can help computer more efficient to complete automates repeatitive tasks.")