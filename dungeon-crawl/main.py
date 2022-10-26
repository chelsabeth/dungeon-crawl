from welcome import *

# step 3 - if user quits game, show message

# step 4 - compare users input and take them to location, if location is invalid, throw error

# step 1 - display welcome message & describe game
info_welcome()
ask_name()

# while True:




# Helpers
def get_user_direction():
    direction = input("Choose your direction adventurer - n, s, e, w\n")
    return direction


def parse_input(entry):
    internal_entry = entry.lower()
    if internal_entry == 'n' | internal_entry == 'north':
        print('North Works')
        return 'n' # What should I be returning here? This functions purpose it to parse a input and give back a useful result. Should it be calling a move function or something along those lines?
    else if internal_entry == 's' | internal_entry == 'south':
        print('South Works')
        return 's'
    else if internal_entry == 'e' | internal_entry == 'east':
        print('East Works')
        return 'e'
    else if internal_entry == 'w' | internal_entry == 'west':
        print('West Works')
        return 'w'
    else if internal_entry == 'e' | internal_entry == 'exit' | internal_entry == 'leave' | internal_entry == 'quit': 
        print('exit Works')
        return 'e'
    else:
        print('This was not a valid command, please try again')
        return 'invalid'

    # Still need to add inventory system pickup / drop commands