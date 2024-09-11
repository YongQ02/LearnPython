# Chapter 9: Classes Part I

print()
print("Chapter 9: Classes - Part I")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Object-Oriented Programming (OOP)，是开发软件最有效率的方法之一。
# Classes可以代表现实的事物。你将根据这些 class 创建 object。
keyword_1 = "instantiation"

print("Introduction: ")
print("Making an object from a class is called '" + keyword_1 + "', and you work with instances of a class.")

print("\n=========================================================\n")


# Create a 'dog' class.
# Capitalize names refer to classes in Python. Function name will use lower case.
# A function that inside part of class is call a method.
class Dog():
    def __init__(self, name, age):
        self.name = name     # attribute
        self.age = age       # attribute

    def sit(self):
        print(self.name.title() + " now is sitting. Good Boy !")

    def sleep(self):
        print(self.name.title() + " now is laying down and try to sleep. Good Boy !")

# initial method 的前面和后面都有两个underscore: '__init__'。
# 用处是为了让Python可以区分哪个是初始化method，哪个是普通method。避免产生冲突。

# Self parameters 在method definition是必须要有的。而且必须在全部 [参数parameters] 的最前方。
# 定义后不会有任何结果，与'Function'一样, 'class' 要 call CLASS_NAME 才会开始创建 class。

# 任何有 self 作为前缀的 variable 都可以在 class 内的任何 method 中使用。这些变量将称为 '属性-attributes'。


# ==============================================================================================================

# 注意，上面的部分只是定义一个 Dog Class而已。( 可以把Class define当成说明书，下面才是实际创建小狗。 )
# Class里有一个init method，它的工作是初始化信息，然后获取 实参-arguments 存在 'name' 和 'age' 的变量里。
# Class里还有另外两个 method 是这只狗所具备的动作，功能或特征。

# 接下来, 呼叫Class Name并提供实参，才会从这个Class 里面创建一个实体例子。
my_dog = Dog('Kopi', 3)   # 创建 class 的实列开始后，Dog Class里的 'init method' 会先自动运行。
print("My dog's name is " + my_dog.name.title() + '.')
print(my_dog.name.title() + " is " + str(my_dog.age) + " years old.")

print("\n=========================================================\n")

# 从 Dog Class 创建 [ 实列-instance ]后，我们可以用点符号来呼叫任何Class里面的 [方法-method]。
my_dog.sit()
my_dog.sleep()

print("\n=========================================================\n")

# To be continued at page 205, Inheritance.
print("Summary: In this Chapter 9 - Part 1, we have learned to simply define a classes and instance it.")
print(" - Define a class and initialize method on it.")
print(" - Define attribute inside class.")
print(" - Create other method inside the class and called it.")
print(" - Provides arguments to instance create a class")
print(" - Setting default value for an attribute and modify attribute values.")
