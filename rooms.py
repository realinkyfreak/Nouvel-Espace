import inventory


class RoomTemplate:
    def __init__(self):
        self.name = "Room Template"
        self.save_name = "RoomTemplate"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "Cockpit"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CargoHold"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "AirLock"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "ShipsStore"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CrashSite"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "JungleOne"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "JungleTwo"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "JungleThree"
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
        elif action == "Take Ladder" or action == "Take Rope Ladder":
            inventory.add_item('Rope Ladder')
            self.inventory.remove('Rope Ladder')
            print("You took the Rope Ladder.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "JungleFour"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CanyonEdgeNorth"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "Causeway"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CrashTrench"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CanyonEdgeEast"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "LookoutPost"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "CanyonPass"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "Clearing"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "RopeBridge"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "BridgeCrossing"
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
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "BeachOne"
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
            return 'BeachTwo()'
        elif action == "Up":
            return 'BridgeCrossing()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachTwo:
    def __init__(self):
        self.name = "Beach"
        self.save_name = "BeachTwo"
        self.inventory = []
        self.room_details = "The beach continues to the east. You can see the gentle waves lapping at the shore edge."


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
            return 'BeachThree()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachOne()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachThree:
    def __init__(self):
        self.name = "Beach"
        self.save_name = "BeachThree"
        self.inventory = []
        self.room_details = "The beach continues to the east. Your shoes are covered in sand."


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
            return 'BeachFour()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachFour:
    def __init__(self):
        self.name = "Beach"
        self.save_name = "BeachFour"
        self.inventory = []
        self.room_details = "The beach continues to the east. You can also see a ladder to the north that leads up " \
                            "off of the beach."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North" or action == "Up":
            return 'BeachPassFour()'
        elif action == "East":
            return 'BeachFive()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachThree()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachFive:
    def __init__(self):
        self.name = "Beach"
        self.save_name = "BeachFive"
        self.inventory = ['Polished Shell']
        self.room_details = "You can see a cliff face to the East where the sand stops and a more rocky path starts, " \
                            "the path appears to then go North from the cliff face."


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
            return 'CliffFaceOne()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachFour()'
        elif action == "Take Polished Shell" or action == "Take Shell":
            inventory.add_item('Polished Shell')
            self.inventory.remove('Polished Shell')
            print("You took the polished shell")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class CliffFaceOne:
    def __init__(self):
        self.name = "Cliff Face"
        self.save_name = "CliffFaceOne"
        self.inventory = []
        self.room_details = "The cliff face runs to the North. South the cliff face extends into the water a short " \
                            "distance."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'CliffFaceTwo()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachFive()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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
        self.save_name = "TrackOne"
        self.inventory = []
        self.room_details = "The track continues to the North. To the East you can walk along the top of the beach."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'TrackTwo()'
        elif action == "East":
            return 'BeachPassOne()'
        elif action == "South":
            return 'BridgeCrossing()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachPassOne:
    def __init__(self):
        self.name = "Pass above the beach"
        self.save_name = "BeachPassOne"
        self.inventory = []
        self.room_details = "The pass continues to the east."


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
            return 'BeachPassTwo()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'TrackOne()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachPassTwo:
    def __init__(self):
        self.name = "Pass above the beach"
        self.save_name = "BeachPassTwo"
        self.inventory = []
        self.room_details = "The pass continues to the east."


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
            return 'BeachPassThree()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachPassOne()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachPassThree:
    def __init__(self):
        self.name = "Pass above the beach"
        self.save_name = "BeachPassThree"
        self.inventory = []
        self.room_details = "The pass continues to the east."


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
            return 'BeachPassFour()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachPassTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachPassFour:
    def __init__(self):
        self.name = "Pass above the beach"
        self.save_name = "BeachPassFour"
        self.inventory = []
        self.room_details = "The pass continues to the East. To the North you look out over a large swamp."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            print("The swamp is too big, you would probably not survive. Let's not go that way.")
        elif action == "East":
            return 'BeachPassFive()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachPassThree()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BeachPassFive:
    def __init__(self):
        self.name = "Pass above the beach"
        self.save_name = "BeachPassFive"
        self.inventory = []
        self.room_details = "You've reached the end of the pass. There is a small path leading North."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'SwampEdgeEast()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'BeachPassFour()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class CliffFaceTwo:
    def __init__(self):
        self.name = "Cliff Face"
        self.save_name = "CliffFaceTwo"
        self.inventory = ['Climbing Rope']
        self.room_details = "Looks like someone tried to climb the cliffs. Judging by the flat red splodge at the " \
                            "bottom of the cliff face, they didn't have much luck!"


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'CliffFaceThree()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'CliffFaceOne()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Take Climbing Rope" or action == "Take Rope":
            inventory.add_item('Climbing Rope')
            self.inventory.remove('Climbing Rope')
            print("You took the Climbing Rope")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class CliffFaceThree:
    def __init__(self):
        self.name = "Cliff Face"
        self.save_name = "CliffFaceThree"
        self.inventory = []
        self.room_details = "To the West in the distance you can see some trees. To the North is what looks like an " \
                            "altar, maybe an ancient religious temple stood here."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'Altar()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'CliffFaceTwo()'
        elif action == "West":
            return 'SwampEdgeEast()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class SwampEdgeEast:
    def __init__(self):
        self.name = "Swamp Edge"
        self.save_name = "SwampEdgeEast"
        self.inventory = []
        self.room_details = "Your toes are getting wet! The swamp extends to the west, but there is no way of " \
                            "crossing it."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'LakeSide()'
        elif action == "East":
            return 'CliffFaceThree()'
        elif action == "South":
            return 'BeachPassFive()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class Altar:
    def __init__(self):
        self.name = "Creepy Altar"
        self.save_name = "Altar"
        self.inventory = []
        self.room_details = "A large stone altar is in front of you, it looks like it could have been use for " \
                            "sacrificial ceremonies...let's hope the priests aren't still here!"


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
            return 'CliffFaceThree()'
        elif action == "West":
            return 'LakeSide()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class LakeSide:
    def __init__(self):
        self.name = "Lake"
        self.save_name = "LakeSide"
        self.inventory = []
        self.room_details = "You are standing at the edge of a large lake, there is a small boat here that looks " \
                            "like it could carry you across the lake to the West."


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
            return 'Altar()'
        elif action == "South":
            return 'SwampEdgeEast()'
        elif action == "West":
            return 'Boat()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class Boat:
    def __init__(self):
        self.name = "Boat"
        self.save_name = "Boat"
        self.inventory = ['Rebreather']
        self.room_details = "You're in a small wooden boat. There are no sails and no oars, but despite the old " \
                            "looking boat there is a control panel with a red button marked with a strange symbol."


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
            return 'LakeSide()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("It's a bit wet in the lake, is there something else you could do?")
        elif action == "Push Button":
            print("The boat starts to move...it's taking you Westwards. It's reached land! You get out and the boat "
                  "goes back the way it came.")
            return 'TrackFour()'
        elif action == "Take Rebreather":
            inventory.add_item('Rebreather')
            self.inventory.remove('Rebreather')
            print("You took the Rebreather.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class TrackFour:
    def __init__(self):
        self.name = "Worn Track"
        self.save_name = "TrackFour"
        self.inventory = []
        self.room_details = "The track goes North where it's being guarded by strange looking soldiers. To the east" \
                            "the track goes into a tunnel."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'BlockedTrack()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            return 'OrnateArch()'
        elif action == "West":
            return 'Tunnel()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class BlockedTrack:
    def __init__(self):
        self.name = "Worn Track"
        self.save_name = "BlockedTrack"
        self.inventory = []
        self.room_details = "The track is blocked by an armed guard. You don't speak their language and you " \
                            "certainly don't look like him! Maybe a conversation is a bad idea at this time " \
                            "maybe you should go back the way you came?"


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
            return 'TrackFour()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class TrackTwo:
    def __init__(self):
        self.name = "Worn Track"
        self.save_name = "TrackTwo"
        self.inventory = []
        self.room_details = "The track continues to the East."


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
            return 'TrackThree()'
        elif action == "South":
            return 'TrackOne()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class TrackThree:
    def __init__(self):
        self.name = "Worn Track"
        self.save_name = "TrackThree"
        self.inventory = []
        self.room_details = "The track continues to the East."


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
            return 'OrnateArch()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'TrackTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class OrnateArch:
    def __init__(self):
        self.name = "Ornate Arch"
        self.save_name = "OrnateArch"
        self.inventory = ['Altar Key']
        self.room_details = "You are standing under an ornate arch, it looks very old although it seems to be in " \
                            "good condition."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'TrackFour()'
        elif action == "East":
            return 'SwampEdgeWest()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'TrackThree()'
        elif action == "Take Key" or action == "Take Altar key":
            inventory.add_item('Altar Key')
            self.inventory.remove('Altar Key')
            print("You took the Altar Key")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class SwampEdgeWest:
    def __init__(self):
        self.name = "Swamp Edge"
        self.save_name = "SwampEdgeWest"
        self.inventory = []
        self.room_details = "You are standing at the western edge of a large swamp."


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
            return 'OrnateArch()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class Tunnel:
    def __init__(self):
        self.name = "Tunnel"
        self.save_name = "Tunnel"
        self.inventory = []
        self.room_details = "The tunnel is dark, but you can see the light at the other end."


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
            return 'TrackFour()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'CanyonEdgeWest()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class CanyonEdgeWest:
    def __init__(self):
        self.name = "Canyon Edge"
        self.save_name = "CanyonEdgeWest"
        self.inventory = []
        self.room_details = "You are standing on the edge of this large canyon. It's a long way down to the bottom!"


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'JungleFive()'
        elif action == "East":
            return 'Tunnel()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("Let's not be foolish, it's a long way down to the bottom...and you don't have a parachute!")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleFive:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleFive"
        self.inventory = []
        self.room_details = "Looks like you're back in the jungle! There is a wooden hut to the west."


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
            return 'JungleSix()'
        elif action == "South":
            return 'CanyonEdgeWest()'
        elif action == "West":
            return 'WoodenHut()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class WoodenHut:
    def __init__(self):
        self.name = "Wooden Hut"
        self.save_name = "WoodenHut"
        self.inventory = []
        self.room_details = "You are in small wooden hut, which smells damp. In the corner of the hut is a body. " \
                            "Looking closer you see it's a dead alien wearing some kind of uniform. Maybe it was" \
                            " carrying something useful?"


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
            return 'JungleFive()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Search Body" or action == "Search Alien":
            print("You found some sort of Access Key, it looks useful so you take it.")
            inventory.add_item('Access Key')
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleSix:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleSix"
        self.inventory = []
        self.room_details = "The jungle is a little thicker here, but still passable without a machete."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'JungleSeven()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'JungleFive()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleSeven:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleSeven"
        self.inventory = []
        self.room_details = "Yet more Jungle.....The jungle goes on to the West, to the East is a very tall wall."


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
            return 'WestWallThree()'
        elif action == "South":
            return 'JungleSix()'
        elif action == "West":
            return 'JungleEight()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleEight:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleEight"
        self.inventory = []
        self.room_details = "You can see some tracks heading West."


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
            return 'JungleSeven()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'JungleNine()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleNine:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleNine"
        self.inventory = []
        self.room_details = "There are tracks here. They appear to be humanoid and appear to run East to West."


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
            return 'JungleEight()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'AlienCamp()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class AlienCamp:
    def __init__(self):
        self.name = "Alien Camp"
        self.save_name = "AlienCamp"
        self.inventory = []
        self.room_details = "There are several alien humanoids here, they all appear friendly. Once of them " \
                            "approaches you, looks like it wants to trade with you. Have you got anything shiny?"


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'LakeEdgeThree()'
        elif action == "East":
            return 'JungleNine()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
        elif action == "Exit":
            print("Are you sure you want to quit?")
            quitter = input("Y or N: ")
            if quitter.title() == "Y":
                print("Goodbye....")
                exit(0)
            else:
                print("Glad to hear it!")
        else:
            if 'Trade' in action:
                if action == "Trade Polished Shell" or action == "Trade Shell":
                    if 'Polished Shell' in inventory.inventory:
                        print("You traded the Polished Shell with the alien. He shows you a map which marks what "
                              "appears to be a power plant to the West, and a large citadel to the East of your "
                              "current location.")
                else:
                    print("No trade! You don't have anything else the alien wants.")
            else:
                print("Sorry, I don't understand.")


class LakeEdgeThree:
    def __init__(self):
        self.name = "Lake Edge"
        self.save_name = "LakeEdgeThree"
        self.inventory = []
        self.room_details = "You are standing on the shore of a giant lake, which runs East to West."


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
            return 'LakeEdgeFour()'
        elif action == "South":
            return 'AlienCamp()'
        elif action == "West":
            return 'LakeEdgeTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class LakeEdgeTwo:
    def __init__(self):
        self.name = "Lake Edge"
        self.save_name = "LakeEdgeTwo"
        self.inventory = []
        self.room_details = "The lake is clear and cool, it's nice to be out of the jungle heat."


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
            return 'LakeEdgeThree()'
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            return 'LakeEdgeOne()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class LakeEdgeOne:
    def __init__(self):
        self.name = "Lake Edge"
        self.save_name = "LakeEdgeOne"
        self.inventory = []
        self.room_details = "The lake edge is shallow here. If you could breathe under water you could get in to " \
                            "the North."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            if 'Rebreather' in inventory.inventory:
                return 'LakeOne()'
            else:
                print("You can't breathe under water...one is not a fish, is one.")
        elif action == "East":
            return 'LakeEdgeTwo()'
        elif action == "South":
            return 'JungleTen()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class JungleTen:
    def __init__(self):
        self.name = "Jungle"
        self.save_name = "JungleTen"
        self.inventory = []
        self.room_details = "You are back in the jungle, above you is a narrow pass. If you had a rope you could" \
                            " climb Up there."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            return 'LakeEdgeOne()'
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Up" or action == "Climb" or action == "Use Rope" or action == "Use Climbing Rope":
            if 'Climbing Rope' in inventory.inventory:
                return 'NarrowPass()'
            else:
                print("You don't have a rope.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class NarrowPass:
    def __init__(self):
        self.name = "Narrow Pass"
        self.save_name = "NarrowPass"
        self.inventory = []
        self.room_details = "You are on a narrow pass. To the North is a door with an Access Key slot. Below you " \
                            "is the jungle, if you had a rope you could climb Down."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            if 'Access Key' in inventory.inventory:
                return 'AlienPowerPlant()'
            else:
                print("The door is locked, it looks like you need an Access Key.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            print("You can't go that way.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Down" or action == "Climb Down" or action == "Use Rope" or action == "Use Climbing Rope":
            if 'Climbing Rope' in inventory.inventory:
                return 'JungleTen()'
            else:
                print("You don't have a rope.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class AlienPowerPlant:
    def __init__(self):
        self.name = "Alien Power Plant"
        self.save_name = "AlienPowerPlant"
        self.inventory = []
        if inventory.gas_vent_on:
            self.room_details = "The humming of the power plant is quite loud. You can see the exit to the South, to " \
                                "the North is a flooded tunnel. There is also a large button to turn off the power " \
                                "plant."
        else:
            self.room_details = "The power plant is silent. You can see the exit to the South, to the North is a " \
                                "flooded tunnel. The button to turn on the power plant appears to be broken."


    def show_inventory(self):
        if self.inventory:
            print("Looking around you also see:")
            print(self.inventory)
        else:
            print("Looking around you don't see anything significant.")


    def room_action(self, action):
        if action == "North":
            if 'Rebreather' in inventory.inventory:
                return 'LakeTwo()'
            else:
                print("You can't breathe under water. Maybe if you had a Rebreather.")
        elif action == "East":
            print("You can't go that way.")
        elif action == "South":
            if 'Access Key' in inventory.inventory:
                return 'NarrowPass()'
            else:
                print("The door is locked, it looks like you need an Access Key.")
        elif action == "West":
            print("You can't go that way.")
        elif action == "Push Button" or action == "Press Button":
            inventory.gas_vent_on = False
            print("The power plant is off.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class LakeOne:
    def __init__(self):
        self.name = "Lake"
        self.save_name = "LakeOne"
        self.inventory = []
        self.room_details = "The lake is wet. You can get out to the South, to the West is more wet lake."


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
            return 'LakeEdgeOne()'
        elif action == "West":
            return 'LakeTwo()'
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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


class LakeTwo:
    def __init__(self):
        self.name = "Lake"
        self.save_name = "LakeTwo"
        self.inventory = []
        self.room_details = "The lake is wet. To the East is more wet lake. There is also a tunnel to the South."


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
            return 'LakeOne()'
        elif action == "South":
            return 'AlienPowerPlant()'
        elif action == "West":
            print("You can't go that way.")
        elif action == "Inventory":
            inventory.show_inventory()
        elif action == "Save":
            inventory.save_game(self.save_name)
        elif action == "Load":
            return inventory.load_game()
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