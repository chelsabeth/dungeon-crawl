from welcome import *
from player import *
from room import *
from rooms_store import *

# Properties

player_is_active = True
player = Player("No Name Given", 10) # This is generating a default player for now, update this later.
location = rooms['entrance']

# Helpers

def move_player(direction):
    if direction == 'n' and location.n_to != None:
        location = location.n_to
    elif direction == 's' and location.s_to != None:
        location = location.s_to
    elif direction == 'e' and location.e_to != None:
        location = location.e_to
    elif direction == 'w' and location.w_to != None:
        location = location.w_to
    else:
        print("That was not a valid location")
        return
    location.describe_room()


def get_user_direction():
    direction = input("Choose your direction adventurer: n, s, e, w\n")
    return direction


def parse_input(entry):
    internal_entry = entry.lower()
    if internal_entry == 'n' or internal_entry == 'north':
        print('North Works')
        return 'n' # What should I be returning here? This functions purpose it to parse a input and give back a useful result. Should it be calling a move function or something along those lines?
    elif internal_entry == 's' or internal_entry == 'south':
        print('South Works')
        return 's'
    elif internal_entry == 'e' or internal_entry == 'east':
        print('East Works')
        return 'e'
    elif internal_entry == 'w' or internal_entry == 'west':
        print('West Works')
        return 'w'
    elif internal_entry == 'e' or internal_entry == 'exit' or internal_entry == 'leave' or internal_entry == 'quit':
        exit_game()
    else:
        print('This was not a valid command, please try again')
        return 'invalid'

    # Still need to add inventory system pickup / drop commands, restart, and instructions page

def exit_game():
    exit()

# step 3 - if user quits game, show message

# step 4 - compare users input and take them to location, if location is invalid, throw error

# Start of game
info_welcome()

# Get name information
name = ask_name()
player.__set_name__(name)

# Explain first room
location.describe_room()

# Main game loop
while player_is_active:

    # Ask for a direction, parse it and perform that action
    parse_input(get_user_direction())
