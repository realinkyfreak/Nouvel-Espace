import inventory

class Cockpit:

    def __init__(self):
        self.name = "Cockpit"
        self.room_details = "You can see a sealed door to the Cargo Hold, next to the door is the door release lever."
        self.inventory = []
        self.door_locked = True


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self,action):
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
        elif action == "Inventory":
            inventory.show_inventory()
        else:
            print("Sorry, I don't understand.")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        self.inventory = ['Box Cutter Knife']
        self.room_details = "It looks like this are sustained some damage in the crash, the rover vehicle appears " \
                            "damaged."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self,action):
        if action == "Take Knife" or action == "Take Box Cutter Knife":
            inventory.add_item('Box Cutter Knife')
            self.inventory.remove('Box Cutter Knife')
            print("You took the Box Cutter Knife.")
        elif action == "North":
            return 'ShipsStore()'
        elif action == "East":
            return 'AirLock()'
        elif action == "South":
            return 'Cockpit()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        else:
            print("Sorry, I don't understand.")


class AirLock:

    def __init__(self):
        self.name = "Air Lock"
        self.inventory = []
        self.room_details = "You're in the airlock. To the east, the outer door has been torn off in the crash and " \
                            "you can see crash debris outside."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self,action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            return 'CrashSite()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'CargoHold()'
        elif action == "Inventory":
            inventory.show_inventory()
        else:
            print("Sorry, I don't understand.")


class ShipsStore:

    def __init__(self):
        self.name = "Ships Store"
        self.inventory = []
        self.room_details = "The ships store is too dark to see anything."

    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self,action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'CargoHold()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        else:
            print("Sorry, I don't understand.")


class CrashSite:
    def __init__(self):
        self.name = "Crash Site"
        self.inventory = []
        self.room_details = "You step outside into the crash site, there is debris everywhere. You are standing in a " \
                            "small clearing made by the crash, you are surrounded by jungle."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'AirLock()'
        elif action == "Inventory":
            inventory.show_inventory()
        else:
            print("Sorry, I don't understand.")
