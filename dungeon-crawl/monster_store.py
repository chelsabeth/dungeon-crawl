from monster import Monster
# Where monsters will be stored

# Declare monsters
monsters = {
    'undead': Monster("Undead", "The spooky corpse stands before you, sword in hand. Defeat this hideous monster!", 3, 3, "medium"),

    'ooze': Monster("Ooze", "A green ooze squishes through the cracks of the wall. Defeat this sloppy monster before it consumes you.", 3, 2, "small"),

    'livingspirit': Monster("Living Spirit", "At first you see a haze in the distance, but then it starts to form in the shape of a person. This isn't the traditional ghosts you've fought before.", 3, 4, "medium"),

    'pumpkinhead': Monster("Pumpkin Head", "You see a man approaching you, but as he gets closer you realize he has a pumpkin for a head. It's time to make a jack-o-lantern out of him!", 5, 5, "large", ["5 gold", "pumpkin muffin recipe", "great sword"], ["pumpkin muffin recipe", "5 gold"])
}