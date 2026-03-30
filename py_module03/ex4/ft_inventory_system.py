import sys


def most_least_abundant(inventory: dict) -> str:
    most_item = None
    least_item = None

    for name, qty in inventory.items():

        if most_item is None or qty > inventory.get(most_item):
            most_item = name

        if least_item is None or qty < inventory.get(least_item):
            least_item = name

    return most_item, least_item


def inventory_system(argv: list) -> None:
    print("=== Inventory System Analysis ===")
    inventory = dict()
    for arg in argv:
        try:
            pair = arg.split(":")
            if len(pair) != 2:
                raise ValueError(f"Error - invalid parameter '{arg}'")
            if pair[0] in inventory:
                raise ValueError(f"Redundant item '{pair[0]}' - discarding")
            try:
                inventory[pair[0]] = int(pair[1])
            except ValueError as e:
                raise ValueError(f"Quantity error for '{pair[0]}': {e}")
        except ValueError as e:
            print(e)

    print(f"Got inventory: {inventory}")
    if inventory:
        keys = list(inventory.keys())
        values = list(inventory.values())
        total = sum(values)
        print(f"Item list: {keys}")
        print(f"Total quantity of the {len(keys)} items: {total}")
        for key, value in inventory.items():
            print(
                f"Item {key} represents "
                f"{round((value / total * 100), 1)}%"
                )
        most_item, least_item = most_least_abundant(inventory)
        print(
            f"Item most abundant: {most_item} "
            f"with quantity {max(inventory.values())}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {min(inventory.values())}"
        )
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":

    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
    else:
        inventory_system(args)
