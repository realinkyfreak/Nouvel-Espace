class Player:

    player_alive = True
    victory = False
    inventory = []
    current_room = ''

    def __init__(self):
        self.player_alive = True
        self.vistory = False
        self.inventory = []

    def is_alive(self):
        if self.player_alive == False:
            return False
        else:
            return True

    def is_victorious(self):
        if self.victory == False:
            return False
        else:
            return True

    def player_died(self):
        self.player_alive = False

    def player_victory(self):
        self.victory = True
