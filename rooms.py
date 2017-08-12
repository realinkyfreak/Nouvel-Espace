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
            return 'ShipsStore()'
        elif action == "East":
            return 'AirLock()'
        elif action == "South":
            return 'Cockpit()'
        elif action == "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")


class AirLock:

    def __init__(self):
        self.name = "Air Lock"
        self.inventory = []
        self.room_details = "You're in the airlock. To the east, the outer door has been torn off in the crash and " \
                            "you can see crash debris outside."

    def room_action(self,action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            return 'CrashSite()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'CargoHold()'
        else:
            print("Sorry, I don't understand.")


class ShipsStore:

    def __init__(self):
        self.name = "Ships Store"
        self.inventory = []
        self.room_details = "The ships store is too dark to see anything."

    def room_action(self,action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'CargoHold()'
        elif action == "West":
            print("You can't go that way.")
        else:
            print("Sorry, I don't understand.")


class CrashSite:
    def __init__(self):
        self.name = "Crash Site"
        self.inventory = []
        self.room_details = "You step outside into the crash site, there is debris everywhere. You are standing in a " \
                            "small clearing made by the crash, you are surrounded by jungle."

    def room_action(self, action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'AirLock()'
        else:
            print("Sorry, I don't understand.")
