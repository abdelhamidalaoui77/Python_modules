import math


def parse_coordinates(coord_str: str) -> tuple[float, float, float] | None:
    try:
        parts = coord_str.split(',')
        x, y, z = parts
        x = float(x)
        y = float(y)
        z = float(z)

        return (x, y, z)

    except Exception:
        raise Exception("Invalid syntax")


def distance_3d(p1: tuple[float, float, float],
                p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_player_pos() -> tuple | None:
    while True:
        given_pos = input("Enter new coordinates as floats in"
                          " format 'x,y,z': ")
        try:
            parse_pos = parse_coordinates(given_pos)
            return parse_pos
        except Exception as err:
            print(err)


def second_argumet_parsing(cordinates: str) -> tuple | None:
    cordinates_list = cordinates.split(",")
    for elem in cordinates_list:
        try:
            float(elem)
        except Exception as e:
            raise Exception(elem, e)


def get_second_argument() -> None:
    while True:
        given_pos = input("Enter new coordinates as floats in"
                          " format 'x,y,z': ")
        try:
            second_argumet_parsing(given_pos)
            parse_pos = parse_coordinates(given_pos)
            return parse_pos
        except Exception as err:
            bad_pos, error = err.args
            raise Exception(bad_pos, error)


if __name__ == "__main__":
    origin = (0, 0, 0)

    print("=== Game Coordinate System ===\n\n")
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    x, y, z = first_pos
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance = distance_3d(origin, first_pos)
    print(f"Distance to center: {round(distance, 4)}")
    print("\nGet a second set of coordinates")

    while True:
        try:
            second_pos = get_second_argument()
            distance2 = distance_3d(second_pos, first_pos)
            distance2 = round(distance2, 4)
            print(f"Distance between the 2 sets of coordinates: {distance2}")
            break
        except Exception as err:
            e1, e2 = err.args
            print(f"Error on parameter '{e1}': {e2}")
