import math


def parse_coordinates(coord_str: str) -> tuple[float, float, float]:
    parts = coord_str.split(",")

    if len(parts) != 3:
        raise ValueError("Invalid syntax")

    coords = []
    for part in parts:
        part = part.strip()
        try:
            coords.append(float(part))
        except ValueError as e:
            raise ValueError(f"Error on parameter '{part}': {e}")

    return (coords[0], coords[1], coords[2])


def distance_3d(p1: tuple[float, float, float],
                p2: tuple[float, float, float]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def get_player_pos() -> tuple[float, float, float]:
    while True:
        given = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            return parse_coordinates(given)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    origin = (0.0, 0.0, 0.0)

    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")

    x, y, z = first_pos
    print(f"It includes: X={x}, Y={y}, Z={z}")

    dist = distance_3d(origin, first_pos)
    print(f"Distance to center: {round(dist, 4)}")

    print("\nGet a second set of coordinates")
    second_pos = get_player_pos()

    dist2 = distance_3d(first_pos, second_pos)
    print(f"Distance between the 2 sets of coordinates: {round(dist2, 4)}")
