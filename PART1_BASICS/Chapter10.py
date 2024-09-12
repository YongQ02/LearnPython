# Chapter 10: Files and Exceptions

print()
print("Chapter 10: Files and Exceptions")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# To do any work with a file, first need to open the file to access it.
# The open() function needs one argument: the name of the file you want to open.
# The open() function returns an object representing the file and store this object in 'file_object'.

# 从文件中获取数据
with open('pi_digits.txt') as file_object:
    contents = file_object.read()     # read all content in the file.
    print(contents.rstrip())

# The keyword 'with' closes the file once access is no longer needed. That means the file will close automatically once task is complete.
# The open() function automatically creates file if it doesn't exist.

print("\n=========================================================\n")

# This open function only open files in same directory. Provide 'file path' to open files from other directory.
digit_file_path = 'C:/LearnPython/Python-Crash-Course/PART1_BASICS/pi_digits.txt'   # We called this 'absolute file path'.

with open(digit_file_path) as test_file:
    #for line in test_file:
        #print(line.rstrip())
    lines = test_file.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print("\n=========================================================")

# Python 只能写入字符串, 如果要写数字必须使用 str() function。

# Writing to a file 写入文件
filepath = 'C:/LearnPython/Python-Crash-Course/learningpython.txt'

with open(filepath, 'w') as file_object2:      # First arguments: File path; Second arguments: 'w' (tells Python we open the file in "write mode")
    file_object2.write("I like to playing video games !\n")     # We have 'read mode - r', 'write mode - w', 'append mode - a' and 'read & write mode - r+'
    file_object2.write("I love watch anime too !")

print("Content have successfully write into 'learningpython.txt' file.")
# write mode 会清楚所有数据再重第一行开始写。如果要继续写数据, 最好用append mode。

with open(filepath, 'a') as file_object2:
    file_object2.write("\nThis is an extra appended sentences....")

print("A sentences has successfully append to the 'learningpython.txt' file.")

print("\n=========================================================")

print("Summary: ")
print("- Learned to open and reads the file.")
print("- Learned how to over write content or append content on the files.")
print("- The keyword 'with' will open and automatically close the file once the task is done.")
print("\nSee you on Chapter 10 - Part II: Exceptions [page233]")
