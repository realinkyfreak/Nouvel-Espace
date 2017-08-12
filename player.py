class Player:

    player_alive = True
    victory = False
    inventory = []
    current_room = ''

    def __init__(self):
        self.player_alive = True
        self.victory = False
        self.inventory = []

    def is_alive(self):
        if self.player_alive is False:
            return False
        else:
            return True

    def is_victorious(self):
        if self.victory is False:
            return False
        else:
            return True

    def player_died(self):
        self.player_alive = False

    def player_victory(self):
        self.victory = True

    def add_inventory(self,item):
        self.inventory.append(item)

    def drop_inventory(self,item):
        self.inventory.remove(item)
