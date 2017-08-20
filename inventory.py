import savegame

inventory = []

def add_item(item):
    inventory.append(item)


def remove_item(item):
    inventory.remove(item)


def show_inventory():
    if inventory:
        print("You are currently carrying:")
        print(inventory)
    else:
        print("You are not carrying anything.")


def save_game(room):
    game_saved = savegame.save_game(inventory,room)
    if game_saved:
        print("Game Saved!")
    else:
        print("Game could not be saved.")


def load_game():
    game_loaded = savegame.load_game()
    if game_loaded:
        print(game_loaded)
        current_room = game_loaded[0]
        '''broken load...damn it!'''
        i=1
        while i < game_loaded.__len__()-1:
            inventory.append(i)
    else:
        print("No save game found, starting at the begining...")
