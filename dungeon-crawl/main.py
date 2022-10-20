from welcome import *
from room import Room

# Declare rooms
room = {
    'entrance': Room("Cave Entrance", 
    "North of you, the opening of the cave. It has an eerie glow about it, but still you feel it's pull."),

    'cavern': Room("Cavern", 
    "South of you, you can see the dim light from the cave entrance. Mysterious passages run north and east. It's a bit...too quiet."),

    'sleepquaters': Room("Sleeping Quarters", 
    "You push hard to open the squeaky door. Inside you find a dusty bed and a few empty chests. Looks like you've reached a dead end. You just hope that door didn't alert anyone or anything."),

    'kitchen': Room("Kitchen", 
    "You can smell something sweet in the air. You approach and see a stocked kitchen with warm muffins. You're favorite, pumpkin muffins! You shove a muffin in your mouth before whoever made them comes back, then notice a glowing door to the north, you feel it's pull again."),

    'treasure': Room("Treasure Chamber", 
    "You have found the treasure chamber, although there is no treasure...at least not anymore. Sadly, the place has already been looted. At least you got a delicous muffin out of this adventure...")
}

# Link rooms 
room['entrance'].n_to = room['cavern']
room['cavern'].s_to = room['entrance']
room['cavern'].n_to = room['sleepquarters']
room['cavern'].e_to = room['kitchen']
room['sleepquarters'].s_to = room['cavern']
room['kitchen'].w_to = room['cavern']
room['kitchen'].n_to = room['treasure']
room['treasure'].s_to = room['kitchen']


# Main REPL loop for dungeon crawl
print(info_welcome())
ask_name()

# while True: