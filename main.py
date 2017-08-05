from rooms import *
from player import Player
from world import World

room_list = ['Room1','Room2','Room3']

'''Just doing a quick sanity check on rooms'''
for room in room_list:
    print(room)

def play():
    world = World()
    world.load_titles()
    current_room = Cockpit()
    player = Player()

    while player.is_alive() and not player.is_victorious():
        if player.is_alive() and not player.is_victorious():
            print("You are in the %a." %current_room.name)
            print(current_room.room_details)
            break


play()