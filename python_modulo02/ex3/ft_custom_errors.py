class  GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def testing_garden_errors():
    wilting = True
    water = None
    try:
        print("Testing PlantError...")
        if wilting:
            raise PlantError()
    except PlantError:
        print("Caught PlantError: The tomato plant is wilting!")
    print()
    try:
        print("Testing WaterError...")
        if not water:
            raise WaterError()
    except WaterError:
        print("Caught WaterError: Not enough water in the tank!")
    print()
    print("Testing catching all garden errors...")
    try:
        if wilting:
            raise PlantError()
    except GardenError:
        print("Caught GardenError: The tomato plant is wilting!")
    try:
        if not water:
            raise WaterError()
    except GardenError:
        print("Caught GardenError: Not enough water in the tank!")
    print()
    print("All custom error types work correctly!")

if __name__ == "__main__":
    testing_garden_errors()