import os
import sys
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR: Path = Path(__file__).resolve().parent
ENV_FILE: Path = BASE_DIR / ".env"

load_dotenv(ENV_FILE, override=False)


def get_config() -> tuple[dict[str, str], list[str]]:
    defaults: dict[str, str] = {
        "MATRIX_MODE": "development",
        "DATABASE_URL": "",
        "API_KEY": "",
        "LOG_LEVEL": "DEBUG",
        "ZION_ENDPOINT": "",
    }

    config: dict[str, str] = {}
    missing: list[str] = []

    for name, default in defaults.items():
        value: str | None = os.getenv(name)

        if value is None or not value.strip():
            config[name] = default
            missing.append(name)
        else:
            config[name] = value.strip()

    if config["MATRIX_MODE"] not in ("development", "production"):
        print(
            "Warning: Invalid MATRIX_MODE. Using development mode."
        )
        config["MATRIX_MODE"] = "development"

    valid_levels: set[str] = {
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
    }

    if config["LOG_LEVEL"].upper() not in valid_levels:
        print("Warning: Invalid LOG_LEVEL. Using DEBUG.")
        config["LOG_LEVEL"] = "DEBUG"
    else:
        config["LOG_LEVEL"] = config["LOG_LEVEL"].upper()

    return config, missing


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")

    config: dict[str, str]
    missing: list[str]
    config, missing = get_config()

    if missing:
        print("Warning: Missing configuration values:")
        for name in missing:
            print(f"  - {name}")
        print("Safe defaults will be used where available.")

    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["DATABASE_URL"]:
        print("Database: Configured")
    else:
        print("Database: Not configured (local development fallback)")

    if config["API_KEY"]:
        print("API Access: Key configured")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Remote Network: Endpoint configured")
    else:
        print("Remote Network: Not configured")

    print("\nConfiguration security check:")
    print("[OK] Secrets are not printed in the output")

    if ENV_FILE.exists():
        print("[INFO] .env exists; verify that Git ignores it")
    else:
        print("[INFO] No .env file found")

    print("[OK] Environment variables can override .env values")

    if config["MATRIX_MODE"] == "development":
        print("\nDevelopment mode: Verbose diagnostics enabled.")
        print("External services are not contacted by this example.")
    else:
        print("\nProduction mode: Minimal diagnostics enabled.")
        print("Secret values remain hidden.")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()