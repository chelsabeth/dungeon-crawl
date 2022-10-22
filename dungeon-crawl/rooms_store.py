from room import Room
# Where rooms will be stored
# Room connections will be created here

# Declare rooms
rooms = {
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
rooms['entrance'].n_to = rooms['cavern']
rooms['cavern'].s_to = rooms['entrance']
rooms['cavern'].n_to = rooms['sleepquarters']
rooms['cavern'].e_to = rooms['kitchen']
rooms['sleepquarters'].s_to = rooms['cavern']
rooms['kitchen'].w_to = rooms['cavern']
rooms['kitchen'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['kitchen']