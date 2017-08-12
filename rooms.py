class Cockpit:

    def __init__(self):
        self.name = "Cockpit"
        self.room_details = "You can see a sealed door to the Cargo Hold, next to the door is the door release lever."
        self.inventory = []
        self.door_locked = True

    def room_action(self,action):
        print(action)
        if action == "Pull Lever":
            self.door_locked = False
            self.room_details = "You can see an open door to the Cargo Hold, next to the door is the door release " \
                                "lever."
            print("You unlocked the door.")
        elif action == "North" and self.door_locked == False:
            return 'CargoHold()'
        elif action == "North" and self.door_locked == True:
            print("You might need to pull a lever first?")
        elif action == "East" or action == "South" or action == "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        self.inventory = ['Box Cutter Knife']
        self.room_details = "It looks like this are sustained some damage in the crash, the rover vehicle appears " \
                            "damaged. On the floor is a %a" % self.inventory[0]

    def room_action(self,action):
        if action == "Take Knife" or action == "Take Box Cutter Knife":
            print("Need to implement taking items")
        elif action == "North":
            print("This would go north")
        elif action == "East":
            print("This would go east")
        elif action == "South":
            print("This would go south")
        elif action == "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")
