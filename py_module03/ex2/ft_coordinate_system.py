import math


def parse_coordinates(coord_str: str) -> tuple[int, int, int] | None:
    try:
        parts = coord_str.split(',')
        x, y, z = parts
        x = int(x)
        y = int(y)
        z = int(z)

        return (x, y, z)

    except ValueError as e:
        raise ValueError(e)


def distance_3d(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    origin = (0, 0, 0)
    tested_pos = (10, 20, 5)
    string_pos = "3,4,0"
    invalid_pos = "abc,def,ghi"

    print(f"Position created: {tested_pos}")
    print(f"Distance between {origin} and {tested_pos}:"
          f" {distance_3d(origin, tested_pos):.2f}\n")

    try:
        print(f'Parsing coordinates: "{string_pos}"')
        position = parse_coordinates(string_pos)
        print(f"Parsed position: {position}")
        dist = distance_3d(origin, position)
        print(f"Distance between {origin} and {position}: {dist}\n")
    except ValueError as err:
        print(f"Error parsing coordinates: {err}")
        print(f'Error details - Type: ValueError, Args: ("{err}",)')

    try:
        print(f'Parsing invalid coordinates: "{invalid_pos}"')
        position_2 = parse_coordinates(invalid_pos)
        dist = distance_3d(origin, position_2)
        print(f"Distance between {origin} and {position_2}: {dist}")
    except ValueError as err:
        print(f"Error parsing coordinates: {err}")
        print(f'Error details - Type: ValueError, Args: ("{err}",)\n')
    print("Unpacking demonstration:")
    x1, x2, x3 = position
    print(f"Player at x={x1}, y={x2}, z={x3}")
    print(f"Coordinates: X={x1}, Y={x2}, Z={x3}")
