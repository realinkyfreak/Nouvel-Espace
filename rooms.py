import inventory
'''Need to add save and load game to each room!'''

class RoomTemplate:
    def __init__(self):
        self.name = "Room Template"
        self.inventory = []
        self.room_details = "Describe the room to the player"


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
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


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
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class CargoHold:

    def __init__(self):
        self.name = "Cargo Hold"
        if 'Box Cutter Knife' in inventory.inventory:
            self.inventory = []
        else:
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
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class AirLock:

    def __init__(self):
        self.name = "Air Lock"
        self.inventory = []
        self.room_details = "To the east, the outer door has been torn off in the crash and " \
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
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class ShipsStore:

    def __init__(self):
        self.name = "Ships Store"
        if 'First Aid Kit' in inventory.inventory:
            self.inventory = []
        else:
            self.inventory = ['First Aid Kit']
        self.room_details = "The ships store is too dark to see anything."

    def show_inventory(self):
        if self.inventory and 'Torch' in inventory.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("It's too dark.")


    def room_action(self,action):
        if action == "North":
            print("You can't go that way.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'CargoHold()'
        elif action == "West":
            print("You can't go that way.")
        elif action == 'Take First Aid Kit':
            if 'Torch' in inventory.inventory:
                inventory.add_item('First Aid Kit')
                self.inventory.remove('First Aid Kit')
                print("You took the First Aid Kit.")
            else:
                print("I can't see that.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
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
            return 'JungleOne()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'AirLock()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class JungleOne:
    def __init__(self):
        self.name = "Jungle"
        self.inventory = []
        self.room_details = "You're surrounded by trees, vegetation and the strange calls of " \
                            "wild animals."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'JungleTwo()'
        elif action == "East":
            return 'JungleThree()'
        elif action == "South":
            return 'CrashSite()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class JungleTwo:
    def __init__(self):
        self.name = "Jungle"
        self.inventory = []
        self.room_details = "More trees, vegetation and the strange calls of " \
                            "wild animals."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'CanyonEdgeNorth()'
        elif action == "East":
            return 'JungleFour()'
        elif action == "South":
            return 'JungleOne()'
        elif action == "West":
            return 'Causeway()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class JungleThree:
    def __init__(self):
        self.name = "Jungle"
        self.inventory = ['Rope Ladder']
        self.room_details = "More trees, vegetation and the strange calls of " \
                            "wild animals."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'JungleFour()'
        elif action == "East":
            return 'CanyonEdgeEast()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'JungleOne()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class JungleFour:
    def __init__(self):
        self.name = "Jungle"
        self.inventory = []
        self.room_details = "More trees, vegetation and the strange calls of " \
                            "wild animals."


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
            return 'JungleThree()'
        elif action == "West":
            return 'JungleTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class CanyonEdgeNorth:
    def __init__(self):
        self.name = "Canyon Edge"
        self.inventory = []
        self.room_details = "You can see out over a large deep canyon. It runs in an arch from your West round you " \
                            "to the South. There are barriers in front of you, it appears to be a viewing area."


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
            return 'JungleTwo()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class Causeway:
    def __init__(self):
        self.name = "Causeway"
        self.inventory = []
        self.room_details = "You are walking along a narrow causeway. To the East is the crash trench clearly visible" \
                            " through the trees. To your south is a large lake, but your path is blocked by thick" \
                            " jungle."


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
            return 'JungleTwo()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'CrashTrench()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class CrashTrench:
    def __init__(self):
        self.name = "Crash Trench"
        if 'Torch' in inventory.inventory:
            self.inventory = []
        else:
            self.inventory = ['Torch']
        self.room_details = "You're standing in the bottom of a shallow trench that was dug as the ship crashed and " \
                            "skidded along the ground. To the south one of the ships engines is still running and " \
                            "hot gasses and flames are eminating from it."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            print("The canyon edge is unguarded, probably best not to go that way.")
        elif action == "East":
            return 'Causeway()'
        elif action == "South":
            print("The hot gasses from the engine start to choke you, at least until the jet flames ignite a small "
                  "patch of your hair like the wick of a candle. You rush back patting out your flaming hair!")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Take Torch":
            inventory.add_item('Torch')
            self.inventory.remove('Torch')
            print("You took the Torch.")
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class CanyonEdgeEast:
    def __init__(self):
        self.name = "Canyon Edge"
        self.inventory = []
        self.room_details = "You can see out over a narrower canyon. It runs from North to South."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'LookoutPost()'
        elif action == "East":
            print("Careful there, it's the canyon edge that way. I wouldn't go that way.")
        elif action == "South":
            return 'CanyonPass()'
        elif action == "West":
            return 'JungleThree()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class LookoutPost:
    def __init__(self):
        self.name = "Lookout Post"
        self.inventory = []
        self.room_details = "From the lookout post, you can see out over a narrower canyon, maybe the end of " \
                            "something longer? It runs from North to South. To the North West you can see a " \
                            "bright glow coming from a tall building. To the North East you can see a large " \
                            "city with high walls."


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
            return 'CanyonEdgeEast()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class CanyonPass:
    def __init__(self):
        self.name = "Canyon Pass"
        self.inventory = []
        self.room_details = "Just seems to be a narrow pass through the jungle, looks like a clearing to the South."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'CanyonEdgeEast()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'Clearing()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class Clearing:
    def __init__(self):
        self.name = "Clearing"
        self.inventory = []
        self.room_details = "You stand in a small clearing. It feels larger than it looks, maybe that's just the " \
                            "claustrophobia of the jungle talking! To your East is a rather worn rope bridge."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'CanyonPass()'
        elif action == "East":
            return 'RopeBridge()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class RopeBridge:
    def __init__(self):
        self.name = "Rope Bridge"
        self.inventory = []
        self.room_details = "This bridge seems a bit too worn and is swaying in the  wind that blows through the " \
                            "canyon. Maybe we should get moving?"


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
            return 'BridgeCrossing()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return('Clearing()')
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class BridgeCrossing:
    def __init__(self):
        self.name = "Bridge Crossing"
        self.inventory = []
        self.room_details = "There is a worn track leading North. There is also a set of narrow steps leading down" \
                            " to a beach that continues to the East?"


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'TrackOne()'
        elif action == "East":
            print("You can't go that way. But there are steps leading Down.")
        elif action == "Down":
            return 'BeachOne()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return('RopeBridge()')
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class BeachOne:
    def __init__(self):
        self.name = "Beach"
        self.inventory = []
        self.room_details = "The beach is sandy and the waves lap gently at the shore. The " \
                            "beach continues to the East, and steps lead up from the beach."


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
            print("*** TO DE DONE ***")
        elif action == "Up":
            return 'BridgeCrossing()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")


class TrackOne:
    def __init__(self):
        self.name = "Worn Track"
        self.inventory = []
        self.room_details = "The track continues to the North."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            print("*** TO BE DONE ***")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'BridgeCrossing()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            print("Sorry, I don't understand.")