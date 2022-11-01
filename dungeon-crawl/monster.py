class Monster:
    def __init__(self, name, attack, health, loot = None, inventory = None, size):
        self.name = name
        self.attack = attack
        self.health = health
        self.size = size

        if loot is None:
            self.loot = []
        else: 
            self.loot = loot

        if inventory is None: 
            self.inventory = []
        else:
            self.inventory = inventory

    def monster_loot(self):
        if self.loot == []:
            print('Sorry, this monster has no loot table')
        else: 
            print('This monster has the following loot:')
            for loot in self.loot:
                print(f'{loot.name}')
    
    def monster_inventory(self):
        if self.intventory == []:
            print('Sorry, nothing to collect from this monster')
        else: 
            print('You slayed the monster! You may collect these items:')
            for inventory in self.inventory:
                print(f'{inventory.name}')

