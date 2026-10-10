import os
import sys
import site

def main():
    if sys.prefix == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole" \
              " system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting\n"
              "the global system.\n")
        if site.getsitepackages():
            print(f"Reagent installation path:\n{site.getsitepackages()[0]}")

if __name__ == "__main__":
    main()
