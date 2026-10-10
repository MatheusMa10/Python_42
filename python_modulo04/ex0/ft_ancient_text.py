#!/usr/bin/env python3

import sys
import typing


def checking_arg() -> None:
    argv: list[str] = sys.argv
    if len(argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    file_name: str = argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{argv[1]}'")
    try:
        file_opening: typing.TextIO = open(file_name)
        print("---\n")
        read_content: str = file_opening.read()
        print(read_content, end="")
        print("\n---")
        file_opening.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError as fe:
        print(f"Error opening file '{file_name}': {fe}")
    except PermissionError as pe:
        print(f"Error opening file '{file_name}': {pe}")


if __name__ == "__main__":
    checking_arg()