#!/usr/bin/env python3

import sys
import typing


def process_archive() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    file_name: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file_opening: typing.TextIO = open(file_name)
        print("---\n")

        read_content: str = file_opening.read()
        print(read_content, end="")
        print("\n---")

        file_opening.close()
        print(f"File '{file_name}' closed.\n")

        print("Transform data:")
        print("---\n")

        splited_line: list[str] = read_content.split('\n')
        processed_line: list[str] = [
            line + "#" if line else line for line in splited_line
        ]

        last_text: str = '\n'.join(processed_line)
        print(last_text, end="")
        print("\n---")

        new_file_name: str = input("Enter new file name (or empty): ")

        if not new_file_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            new_file: typing.TextIO = open(new_file_name, 'w')
            new_file.write(last_text)
            new_file.close()
            print(f"Data saved in file '{new_file_name}'.")

    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    process_archive()