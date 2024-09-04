### List 列表
print()
print("Chapter 3: Introducing to Lists")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

# Python 用 [] 来代表 List
# List 里可以放很多个value
# List 里的每个 value 都用逗号来隔开

# Example 这列表命名为 "my_hobbies", 里有五个 value
my_hobbies= ['playing video game', 'playing electric guitar', 'watch anime', 'exersice', 'coding']
print("Hi! Today is going to learn Chapter 3: Lists. One of my hobbies is " + my_hobbies[1])

print("\n=========================================================\n")

# To check last information from list history
print("I have use lists to create a program, which can check last item i bought on Shopee.")
shopping_item = ['clothes', 'chair', 'mouse', 'huion-tablet', 'tissue', 'nose clear']
pop_item = shopping_item.pop()
print("The last item i bought on Shopee was " + pop_item)

print("\n=========================================================\n")

location_to_visit = ["Japan", "Taiwan", "Norway", "Australia", "HongKong"]
print("These is the country I wish to visit !")
print(location_to_visit)
