def input_temperature(temp_str):
    print(f"Input data is {temp_str}")
    temp_int: int = int(temp_str)
    return (temp_int)

def test_temperature():
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}ºC")

        temperature = input_temperature ("abc")
        print(f"Temperature is now {temperature}ºC")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temperature}'")
    print(f"All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()