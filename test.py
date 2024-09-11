# Function to determine if number is even or odd.

#number_receieve = "Enter a number, I'll tell you if it's even or odd."
#number_receieve += "\nEnter number here: "

#number = int(input(number_receieve))

#if number % 2 == 0:
#    print("The number '" + str(number) + "' is even.")
#else:
#    print("The number '" + str(number) + "' is odd.")


# Favourite mountain for people survey

#responses = {}
#polling_active = True

#while polling_active:
#    name = input("\nWhat is your name: ")
#    response = input("Which mountain would you like to climb someday: ")
#
#    responses[name] = response

#    repeat = input("Would you like to let anohter person respond: ")
#    if repeat == 'no':
#        polling_active = False

#print("\n--- Poll Results ---")
#for name, response in responses.items():
#    print(name + " would like to climb " + response + ".")

print()


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, customer_number):
        if customer_number >= self.number_served:
            self.number_served = customer_number
        else:
            print("You don't have the ability to turn back time !")

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("mc donald", "french fries")
print("\nThe restaurant has served " + str(restaurant.number_served) + " customer today.")
restaurant.set_number_served(23)
print("\nAfter 1 hour, the restaurant has served " + str(restaurant.number_served) + " customers today.")
restaurant.increment_number_served(50)
print("After 3 hours, the restaurant now has served " + str(restaurant.number_served) + " customers.")
