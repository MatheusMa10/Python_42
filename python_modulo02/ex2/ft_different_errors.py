def garden_operations(operation_number):
    match operation_number:
        case 0:
            print("Testing operation 0...")
            int("abc")
        case 1:
            print("Testing operation 1...")
            10 / 0
        case 2:
            print("Testing operation 2...")
            open("/non/existent/file")
        case 3:
            print("Testing operation 3...")
            "hello" + 5
        case _:
            print(f"Testing operation {operation_number}...")
            print("Operation completed successfully")

def test_error_types():
    i: int = 0
    while i < 5:
        try:
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: invalid literal for int() with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'")
        except TypeError:
            print("Caught TypeError: can only concatenate str (not int') to str")
        i += 1

    print()
    print("All error types tested sucessfully")
        

if __name__ == "__main__":
    test_error_types()