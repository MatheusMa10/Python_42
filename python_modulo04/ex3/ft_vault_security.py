#!/usr/bin/env python3


def secure_archive(
        file_name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"
        else:
            with open(file_name, "r") as file:
                read_content: str = file.read()
            return True, read_content

    except Exception as e:
        return False, str(e)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    with open("ancient_fragment.txt", "w") as f:
        f.write("[FRAGMENT 001] Digital preservation"
                " protocols established 2087\n"
                "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
                "[FRAGMENT 003] Every byte saved is a victory"
                " against oblivion\n")
    print(secure_archive("ancient_fragment.txt", "read"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", "Some content"))