from welcome import *

# step 2 - prompt user to make a choice
def get_user_direction():
    direction = input("Choose your direction adventurer - n, s, e, w\n")
    return direction

# step 3 - if user quits game, show message

# step 4 - compare users input and take them to location, if location is invalid, throw error

# step 1 - display welcome message & describe game
info_welcome()
ask_name()

# while True: