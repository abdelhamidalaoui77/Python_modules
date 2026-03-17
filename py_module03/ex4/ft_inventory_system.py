import sys


def parse_inventory(args: list[str]) -> dict | None:
    inventory = {}

    for arg in args:
        if ":" not in arg:
            print("Invalid Format")
            return None

        name, qty = arg.split(":")
        try:
            qty = int(qty)
        except ValueError as err:
            raise ValueError(err)

        inventory.update({name: qty})

    return inventory


def total_items(inventory: dict) -> int:
    total = 0
    for qty in inventory.values():
        total += qty
    return total


def most_least_abundant(inventory: dict):
    most_item = None
    least_item = None

    for name, qty in inventory.items():

        if most_item is None or qty > inventory.get(most_item):
            most_item = name

        if least_item is None or qty < inventory.get(least_item):
            least_item = name

    return most_item, least_item


def categorize_items(inventory: dict):
    categories = {
        "Moderate": {},
        "Scarce": {}
    }

    for name, qty in inventory.items():

        if qty >= 4:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    return categories


def inventory_system():

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        return

    try:
        inventory = parse_inventory(sys.argv[1:])
    except ValueError as err:
        raise ValueError(err)

    if not inventory:
        return

    total = total_items(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")

    items = list(inventory.items())

    while len(items) > 0:
        max_pair = None

        for pair in items:
            if max_pair is None or pair[1] > max_pair[1]:
                max_pair = pair

        name, qty = max_pair
        percent = (qty / total) * 100

        unit_word = "unit" if qty == 1 else "units"

        print(f"{name}: {qty} {unit_word} ({percent:.1f}%)")

        items.remove(max_pair)

    print()
    print("=== Inventory Statistics ===")

    most, least = most_least_abundant(inventory)

    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} units)")

    print()
    print("=== Item Categories ===")

    categories = categorize_items(inventory)

    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}\n")

    print("=== Management Suggestions ===")

    scarce = categories.get("Scarce")

    restock = []
    for item, qty in scarce.items():
        if qty == 1:
            restock.append(item)

    if len(restock) > 0:
        print("Restock needed:", ", ".join(restock))
    else:
        print("No restock needed")

    print()
    print("=== Dictionary Properties Demo ===")

    print("Dictionary keys:", ", ".join(inventory.keys()))

    values = []
    for qty in inventory.values():
        values.append(str(qty))
    print("Dictionary values:", ", ".join(values))

    print(
        "Sample lookup - 'sword' in inventory:",
        inventory.get("sword") is not None
    )


if __name__ == "__main__":
    inventory_system()
