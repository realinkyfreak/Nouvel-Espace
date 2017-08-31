import savegame

inventory = []
gas_vent_on = True

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
        print(game_loaded[0])
        counter = 1
        while counter < len(game_loaded):
            inventory.append(game_loaded[counter].strip())
            counter += 1
        print("Game Loaded!")
        return game_loaded[0]
    else:
        print("No save game found, starting at the begining...")


def end_game(room):
    save_game(room)
    print("CONGRATULATIONS !!! You escaped the planet and are on your way home...if the coordinates were correct...")
    print("********************************************")
    print("Thanks for playing Nouvel Espace.")
    print("All game development and design are by Andrew Carrington-Chappell.")
    print("Wan't a copy of the original draft game map...download it from:")
    print("https://www.carrington-chappell.co.uk/downloads/Nouvel-Espace_Design_Map.jpg")
    print("Goodbye for now!")
    exit()
