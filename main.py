from rooms import *
from player import Player
from world import World


world = World()
world.load_titles()
player = Player()
current_room = Cockpit()

while player.is_alive() and not player.is_victorious():
    print("You are at the %a." % current_room.name.title())
    print(current_room.room_details)
    current_room.show_inventory()
    player_action = input("What next? : ")
    next_room = current_room.room_action(player_action.title())
    if next_room:
        try:
            current_room = eval(next_room)
            player.current_room = eval(next_room)
        except Exception:
            print("Room not yet developed!")
