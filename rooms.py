import main


class Cockpit:

    def __init__(self):
        self.name = 'Cockpit'
        self.room_details = "You can see a sealed door to the Cargo Hold, next to the door is the door release lever."
        self.inventory = []
        self.door_locked = True

    def room_action(self,action):
        if action is "Pull Lever":
            self.door_locked = False
            self.room_details = "You can see an open door to the Cargo Hold, next to the door is the door release " \
                                "lever."
            print("You unlocked the door.")
        elif action is "North" and self.door_locked is False:
            '''load new room functionality?'''
            return 'CargoHold()'
        elif action is "North" and self.door_locked is True:
            print("You might need to pull a lever first?")
        elif action is "East" or action is "South" or action is "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        self.navigation = {'North': 'ShipsStore', 'East': 'AirLock'}
        self.room_details = "It looks like this are sustained some damage in the crash, the rover vehicle appears " \
                            "damaged. On the floor is a %a" % self.inventory[0]
        self.inventory = ['Box Cutter Knife']

    def room_action(self,action):
        if action is "Take Knife" or action is "Take Box Cutter Knife":
            main.Player.inventory.append('Box Cutter Knife')
        elif action is "North":
            print("This would go north")
        elif action is "East":
            print("This would go east")
        elif action is "South":
            print("This would go south")
        elif action is "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")
