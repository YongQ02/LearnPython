# Chapter 9: Classes Part II

print()
print("Chapter 9: Classes - Part II")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Inheritance 继承, 继承一个class后可以获取它的 attribute 和 methods进行使用。
# The original class called 'parent class', and the new class is 'child class'。
# Child class inherit all attribute and method from its parent class, and also can define new for his own。


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):     # Name of parent class inside parentheses.
    def __init__(self, make, model, year):
        super().__init__(make, model, year)   # Super function helps Python makes connection between parent and child class.
        self.battery_size = 80

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

# Parent class 必须和 child class 在同一个 file，而且必须出现在 child class 前面。先定义 parent class 才能有 child class。

# ===========================================================================================================================


print("Override: ")
print("class的 method 在child class不适用，你可以在child 使用'override'重写 parent class 的 method。")
print("你只需要在 child 定义你想重写的 method 名，然后修改method里的代码就可以了，只有child 会使用新的method，parent 不受影响。")

print("\nImport Class: ")

# Importing Classes
from CarClass import *

my_newcar = Car('Audi', 'a4', 2016)
print(my_newcar.get_descriptive_name())

my_newcar.odometer_reading = 23
my_newcar.read_odometer()

print()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n=========================================================\n")

print("The Python Standard Library: ")
print("It store a set of modules includes function and class.")
print("You can also download modules from external sources like 'Python Package Index [PyPi]'")

print("\nStyling Classes: ")
print("Class name should be capitalize in first letter of each word, and don't use underscore.")
print("Instance and module names should be written in lowercase with underscores between words.")
print("Every class should have a comment to describe what the class does.")

print("\n=========================================================\n")

print("Summary: In Chapter 9, we learned how to write our own classes.")
print("- Store information in a class using attributes and write methods for class behavior.")
print("- Write __init__() methods that create instances from classes with attributes.")
print("- How to modify attributes through methods.")
print("- Learned inheritance can simplify the creation of classes that are related to each other.")
print("- Learned how storing classes in modules and import it when needed.")
