class Room:
    def __init__(self, name, description, light = 'default', items = None, monsters = None, n_to = None, s_to = None, e_to = None, w_to = None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

        self.light = light # This will give the room any lighting effects I.E. Dark, light, raining, etc

        if items is None:
            self.items = []
        else:
            self.items = items

        if monsters is None:
            self.monsters = []
        else:
            self.monsters = monsters


    def items_in_room(self):
        if self.items == []:
            print('Sorry, this room has no items')
        else: 
            print('This room contains these items:')
            for item in self.items:
                print(f'{item.name}, {item.description}')

    def monsters_in_room(self):
        if self.monsters == []:
            print('This room appears to have no monsters in it')
        else: 
            print('This room contains these monsters:')
            for monster in self.monsters:
                print(f'{monster.name}')

    def describe_room(self):
        print(self.description)


