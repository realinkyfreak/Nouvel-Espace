class Cockpit:

    def __init__(self):
        self.name = "Cockpit"
        self.navigation = {'North': 'Cargo Hold'}
        self.room_details = 'You can see a sealed door to the Cargo Hold, next to the door is the door release lever.'
        self.inventory = []
        self.door_locked = True

    def room_action(self,action):
        if action == "":
            print(action)
        elif action == "":
            print(action)
        elif action == "":
            print(action)
        else:
            print("You cant do that here!")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        self.navigation = {'North':'Ships Store','East': 'Airlock','South': 'Cockpit'}
        self.room_details = 'You are in the cargo hold, there has been a small fire here.'
        self.inventory = ['broken shuttle arm','Box Cutter Knife']

    def room_action(self,action):
        if action == "":
            print(action)
        elif action == "":
            print(action)
        elif action == "":
            print(action)
        else:
            print("You cant do that here!")
