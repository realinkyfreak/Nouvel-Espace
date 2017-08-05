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
        game_action = current_room.room_action(player_action.title())
        if game_action == "NewRoom":
            load_next_room()


def load_next_room():
    current_room = "New Room"
    print(current_room)


play()