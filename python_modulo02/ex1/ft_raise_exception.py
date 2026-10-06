def input_temperature(temp_str):
    print(f"Input data is '{temp_str}'")
    temp_int: int = int(temp_str)
    if temp_int >= 0 and temp_int <= 40:
        return (temp_int)
    elif temp_int < 0:
        raise ValueError(f"Caught input_temperature error: {temp_int}ºC is too cold for plants (min 0ºC)")
    else:
        raise ValueError(f"Caught input_temperature error: {temp_int}ºC is too hot for plants (max 40ºC)")

def test_temperature():
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{error}'")
    print()
    try:
        temperature = input_temperature ("abc")
        print(f"Temperature is now {temperature}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{error}'")
    print()
    try:
        temperature = input_temperature ("100")
        print(f"Temperature is now {temperature}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{error}'")
    print()
    try:
        temperature = input_temperature ("-50")
        print(f"Temperature is now {temperature}ºC")
    except ValueError as error:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{error}'")
    print()
    print(f"All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()