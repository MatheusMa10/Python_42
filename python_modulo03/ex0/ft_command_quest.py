import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) > 1:
        print(f"Total arguments: {len(sys.argv) - 1}")
    i = 1
    if len(sys.argv) > 1:
        while i < len(sys.argv):
            print(f"Argument {i}: {sys.argv[i]}")
            i +=1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}\n")