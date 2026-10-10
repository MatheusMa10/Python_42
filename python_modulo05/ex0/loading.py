import importlib
def main():
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }

    missing = []

    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            missing.append(name)
            print(f"[MISSING] {name} - Not installed")

    print("\npip vs Poetry:")
    print(
        "requirements.txt declares what to install; "
        "pip resolves it at install time.\n"
        "pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved versions in poetry.lock."
        "so every install is identical."
    )

    if missing:
        print("\nSome reagents are missing.")
        print("Install with pip:")
        print("python3 -m pip install -r ex0/requirements.txt")
        print("Install with Poetry:")
        print("poetry install")
    else:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()