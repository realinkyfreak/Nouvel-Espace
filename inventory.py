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


def save_game():
    game_saved = savegame.save_game(inventory)
    if game_saved:
        print("Game Saved!")
    else:
        print("Game could not be saved")


def load_game():
    '''Load save file and set inventory, but what about room inventories'''
    game_loaded = savegame.load_game()
    if game_loaded:
        print("Save Data Loaded!")
    else:
        print("No save game found, starting at the begining")