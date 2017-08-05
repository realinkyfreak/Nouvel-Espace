from rooms import *
from player import Player
from world import World

def play():
    world = World()
    world.load_titles()
    current_room = Cockpit()
    player = Player()

    while player.is_alive() and not player.is_victorious():
        print("You are in the %a." %current_room.name)
        print(current_room.room_details)
        player_action = input("What next? : ")
        next_room = current_room.room_action(player_action.title())
        if next_room:
            print(next_room)
            '''How do I eval the string returned to create a new room from it?'''
            


play()