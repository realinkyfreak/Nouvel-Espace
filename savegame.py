def save_game(inventory):
    try:
        save_file = open("savegame.txt", 'w')
        save_file.flush()
        for item in inventory:
            save_file.write(item + "\n")
        return True
    except FileNotFoundError:
        return False


def load_game():
    temp_inventory = []

    try:
        save_file = open("savegame.txt")
        for line in save_file:
            temp_inventory.append(line)
        return temp_inventory
    except FileNotFoundError:
        return False
