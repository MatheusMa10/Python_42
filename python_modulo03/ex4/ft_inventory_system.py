#!/usr/bin/env python3
import sys


def add_item(inventory: dict[str, int]) -> dict[str, int]:
    args: list[str] = sys.argv[1:]
    for item in args:
        if ":" in item:
            key, value = item.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
                continue
            try:
                inventory[key] = int(value)
            except ValueError as ve:
                print(f"Quantity error for '{key}': {ve}")
        else:
            print(f"Error - invalid parameter '{item}'")

    return inventory





if __name__ == "__main__":
    inventory: dict[str, int] = add_item(dict())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    if inventory:
        total_itens: int = sum(inventory.values())
        print(f"Total quantity of the {len(inventory.values())}"
                f" items: {total_itens}")
        for key in inventory:
            value = inventory[key]
            percent: float = round((value / total_itens) * 100, 1)
            print(f"Item {key} represents {percent}%")
        more: str = list(inventory.keys())[0]
        less: str = list(inventory.keys())[0]
        for key in inventory:
            if inventory[key] > inventory[more]:
                more = key
            if inventory[key] < inventory[less]:
                less = key
        print(f"Item most abundant: {more} with quantity"
                f" {inventory[more]}")
        print(f"Item least abundant: {less} with quantity"
                f" {inventory[less]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")