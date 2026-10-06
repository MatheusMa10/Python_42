class  GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

def water_plant(plant_name):
    try:
        if plant_name != plant_name.capitalize():
            raise PlantError()
        print(f"Watering {plant_name}: [OK]")
    except PlantError:
        print(f"Caught PlantError: Invalid plant name to water: '{plant_name}'")
        print(".. ending tests and returning to main")

if __name__ == "__main__":
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    finally:
        print("Closing watering system")
    print()
    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")