import sys
import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    
    if (sys.argv[1]):
        try:
            given_cordinates = list(sys.argv[1])
        except Exception as err:
            print(err)

        print(f"Position created: {sys.argv[1]}")
        current_cordinates = (0, 0, 0)
        x1, y1, z1 = current_cordinates
        x2, y2, z2 = given_cordinates
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        print(f"Distance between {current_cordinates} and {sys.argv[1]}:"
              f"{distance}")
