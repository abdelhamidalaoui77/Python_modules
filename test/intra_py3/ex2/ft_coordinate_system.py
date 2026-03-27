import math


def parse_data(s: str) -> tuple:
    s = s.split(",")
    try:
        x, y, z = s
    except ValueError:
        raise ValueError("Invalid syntax")
    else:
        return (x, y, z)


def get_second_corr(tup: tuple) -> None:
    s = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x, y, z = parse_data(s)
    except ValueError as e:
        print(e)
        get_second_corr(tup)
        return
    try:
        x, y, z = float(x.strip()), float(y.strip()), float(z.strip())
        print(
            f"Distance between the 2 sets of "
            f"coordinates: {get_distance((x, y, z), tup)}"
        )
    except ValueError as e:
        print(f"Error on parameter {e.args[0][35:]}: {e}")
        get_second_corr(tup)
        return


def get_distance(tup1: tuple, tup2: tuple) -> float:
    x, y, z = tup1
    x2, y2, z2 = tup2
    return round(math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2 + (z2 - z) ** 2), 4)


def get_player_pos() -> None:
    """get pos tuple"""

    s = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x, y, z = parse_data(s)
    except ValueError as e:
        print(e)
        get_player_pos()
        return
    try:
        x, y, z = float(x.strip()), float(y.strip()), float(z.strip())
        print(f"Got a first tuple: {(x, y, z)}")
        print(f"It includes: X={x}, Y={y}, Z={z}")
        print(f"Distance to center: {get_distance((x, y, z), (0, 0, 0))}\n")
        print("Get a second set of coordinates")
        get_second_corr((x, y, z))
    except ValueError as e:
        print(f"Error on parameter {e.args[0][35:]}: {e}")
        get_player_pos()
        return


if __name__ == "__main__":
    try:
        print("=== Game Coordinate System ===\n")
        print("Get a first set of coordinates")
        get_player_pos()
    except KeyboardInterrupt:
        print()
