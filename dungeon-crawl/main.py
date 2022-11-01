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
    global location
    global player
    if direction == 'n' and location.n_to != None:
        location = location.n_to
    elif direction == 's' and location.s_to != None:
        location = location.s_to
    elif direction == 'e' and location.e_to != None:
        location = location.e_to
    elif direction == 'w' and location.w_to != None:
        location = location.w_to
    else:
        print(f'You cannot go that way {player.name}')
        return
    location.describe_room()
    location.monsters_in_room()


def get_user_direction():
    global player
    direction = input(f'Choose your direction, {player.name}: n, s, e, w\n')
    return direction


def parse_input(entry):
    internal_entry = entry.lower()
    if internal_entry == 'n' or internal_entry == 'north':
        return 'n'
    elif internal_entry == 's' or internal_entry == 'south':
        return 's'
    elif internal_entry == 'e' or internal_entry == 'east':
        return 'e'
    elif internal_entry == 'w' or internal_entry == 'west':
        return 'w'
    elif internal_entry == 'e' or internal_entry == 'exit' or internal_entry == 'leave' or internal_entry == 'quit':
        exit_game()
    elif internal_entry == 'r' or internal_entry == 'restart':
        restart_game()
    else:
        print('This was not a valid command, please try again')
        return

    # Still need to add inventory system pickup / drop commands, restart, and instructions page

def exit_game():
    exit()

def restart_game():

    # To Restart, Location has to be reset
    location = rooms['entrance']    
    print("\nThe Game Has restarted\n")
    location.describe_room()

def start_game():

    # Start of game
    info_welcome()

    # Get name information
    name = ask_name()
    player.__set_name__(name)

    # Explain first room
    location.describe_room()

start_game()

# Main game loop
while player_is_active:

    # Ask for a direction
    direction_input = get_user_direction()

    direction = parse_input(direction_input)

    if direction != None:
        move_player(direction)



