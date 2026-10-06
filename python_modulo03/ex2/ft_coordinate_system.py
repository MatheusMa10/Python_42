import math

def get_player_pos():
    while True:
        try:
            coordinate = input("Enter new coordinates as floats in format 'x,y,z': ")
            x, y, z = coordinate.split(',')
            x = float(x)
            y = float(y)
            z = float(z)
            return (x, y, z)
        except (TypeError, ValueError) as error:
            print(f"Error on parameter '{error}': could not convert string to float: '{error}'")

if __name__ == "__main__":
    print("Get a first set of coordinates")
    first_coordinates = get_player_pos()
    print(f"Got a first tuple: {first_coordinates}")
    print(f"It includes: X={first_coordinates[0]}, Y={first_coordinates[1]}, Z={first_coordinates[2]}")
    print(f"Distance to center: {round(math.sqrt(first_coordinates[0] ** 2 + first_coordinates[1] ** 2 + first_coordinates[2] ** 2), 4)}")
    print()
    print("Get a second set of coordinates")
    second_coordinates = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {round(math.sqrt((second_coordinates[0] - first_coordinates[0])**2 +(second_coordinates[1] - first_coordinates[1])**2 +(second_coordinates[2] - first_coordinates[2])**2),4)}")