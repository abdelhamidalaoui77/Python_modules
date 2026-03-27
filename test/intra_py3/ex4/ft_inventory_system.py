import sys


def main(argv: list) -> dict:
    print("=== Inventory System Analysis ===")
    mon_dict = dict()
    for arg in argv:
        try:
            pair = arg.split(":")
            if len(pair) != 2:
                raise ValueError(f"Error - invalid parameter '{arg}'")
            if pair[0] in mon_dict:
                raise ValueError(f"Redundant item '{pair[0]}' - discarding")
            try:
                mon_dict[pair[0]] = int(pair[1])
            except ValueError as e:
                raise ValueError(f"Quantity error for '{pair[0]}': {e}")
        except ValueError as e:
            print(e)

    print(f"Got inventory: {mon_dict}")
    if mon_dict:
        keys = list(mon_dict.keys())
        values = list(mon_dict.values())
        print(f"Item list: {keys}")
        print(f"Total quantity of the {len(keys)} items: {sum(values)}")
        for key, value in mon_dict.items():
            print(
                f"Item {key} represents "
                f"{round((value/sum(values)*100), 1)}%"
                )
        print(
            f"Item most abundant: {max(mon_dict, key=mon_dict.get)} "
            f"with quantity {max(mon_dict.values())}"
        )
        print(
            f"Item least abundant: {min(mon_dict, key=mon_dict.get)} "
            f"with quantity {min(mon_dict.values())}"
        )
        mon_dict.update({"magic_item": 1})
        print(f"Updated inventory: {mon_dict}")


if __name__ == "__main__":

    args = sys.argv[1:]
    if len(args) != 0:

        main(args)
