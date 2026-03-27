import sys


def parse_inventory(args: list[str]) -> dict | None:
    inventory = {}

    for arg in args:
        if ":" not in arg:
            raise ValueError(
                "Invalid format; expected format : item1:quantity1 item2:"
                "quantity2 ..."
            )

        name, qty = arg.split(":")
        if not name:
            raise ValueError(
                "Invalid format; expected format : item1:quantity1 item2:"
                "quantity2 ..."
            )
        try:
            qty = int(qty)
        except Exception:
            raise Exception("Invalid number or Argument; All values"
                            " should be an int")

        inventory.update({name: qty})

    return inventory


def total_items(inventory: dict) -> int:
    total = 0
    for qty in inventory.values():
        total += qty
    return total


def most_least_abundant(inventory: dict) -> str:
    most_item = None
    least_item = None

    for name, qty in inventory.items():

        if most_item is None or qty > inventory.get(most_item):
            most_item = name

        if least_item is None or qty < inventory.get(least_item):
            least_item = name

    return most_item, least_item


def items_categories(inventory: dict) -> dict:
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


def sort_items(items: list, total: int):
    while len(items) > 0:
        max_pair = None

        for pair in items:
            if max_pair is None or pair[1] > max_pair[1]:
                max_pair = pair

        name, qty = max_pair
        percent = (qty / total) * 100

        if qty == 1:
            unit_word = "unit"
        else:
            unit_word = "units"

        print(f"{name}: {qty} {unit_word} ({percent:.1f}%)")

        items.remove(max_pair)


def management_suggestions(categories: dict) -> None:

    scarce = categories.get("Scarce")

    restock = []
    for item, qty in scarce.items():
        if qty == 1:
            restock = restock + [item]

    restock_lenght = len(restock)

    if restock_lenght > 0:
        print("Restock needed:", end=" ")
        i = 0
        while i < len(restock):
            print(restock[i], end="")
            if restock_lenght - 1 != i:
                print(", ", end="")
            i += 1
        print()
    else:
        print("No restock needed")


def dictionary_demo(inventory: dict) -> None:

    print("Dictionary keys:", end="")
    keys = inventory.keys()

    lenght = 0
    i = 0

    for elm in keys:
        lenght += 1

    for elm in keys:
        print(elm, end="")
        if i < lenght - 1:
            print(", ", end="")
        i += 1

    values = inventory.values()
    print()
    print("Dictionary values: ", end="")

    i = 0

    for elm in values:
        print(elm, end="")
        if i < lenght - 1:
            print(", ", end="")
        i += 1
    print()
    print(
        "Sample lookup - 'sword' in inventory:",
        inventory.get("sword") is not None
    )


def main() -> None:

    if len(sys.argv) == 1:
        print("No data provided.Usage: python3 ft_inventory_system.py"
              " item:quantity ...")
        return

    try:
        inventory = parse_inventory(sys.argv[1:])
    except ValueError as err:
        print(err)
        return

    total = total_items(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")

    items = list(inventory.items())

    sort_items(items, total)

    print()
    print("=== Inventory Statistics ===")

    most, least = most_least_abundant(inventory)

    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} units)")

    print()
    print("=== Item Categories ===")

    categories = items_categories(inventory)

    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}\n")

    print("=== Management Suggestions ===")
    management_suggestions(categories)

    print()
    print("=== Dictionary Properties Demo ===")

    dictionary_demo(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
