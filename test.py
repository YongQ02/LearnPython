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


def make_album(album_artist, album_title):
    music_album = {album_artist: album_title}

    return music_album


print("\nEnter 'q' to Quit program.")
decision = True

while decision:
    artist = input("\nEnter a album artist: ")

    if artist == 'q':
        decision = False
        break

    title = input("Enter a album title: ")

    if title == 'q':
        decision = False
        break

    musician = make_album(artist, title)
    print(musician)
