class Cockpit:

    def __init__(self):
        self.name = "Cockpit"
        self.navigation = {'North': 'CargoHold'}
        self.room_details = "You can see a sealed door to the Cargo Hold, next to the door is the door release lever."
        self.inventory = []
        self.door_locked = True

    def room_action(self,action):
        if action == "Pull Lever":
            self.door_locked = False
            self.room_details = "You can see an open door to the Cargo Hold, next to the door is the door release " \
                                "lever."
            print("You unlocked the door.")
        elif action == "North" and self.door_locked == False:
            '''load new room functionality?'''
            return self.navigation['North']
        elif action == "North" and self.door_locked == True:
            print("You might need to pull a lever first?")
        elif action == "East" or action == "South" or action == "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        self.navigation = {'North': 'ShipsStore', 'East': 'AirLock'}
        self.room_details = ""
        self.inventory = ['Box Cutter Knife']

    def room_action(self,action):
        if action:
            print(action)
