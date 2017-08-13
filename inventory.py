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