#!/usr/bin/env python3

import random


def data_comprehensions() -> None:
    print("=== Game Data Alchemist ===\n")
    list_of_players: list[str] = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                                  'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {list_of_players}")
    capitalize_players: list[str] = [player.capitalize()
                                     for player in list_of_players]
    print(f"New list with all names capitalized: {capitalize_players}")
    only_capitalize: list[str] = [player for player in list_of_players
                                  if player.istitle()]
    print(f"New list of capitalized names only: {only_capitalize}")
    dict_players: dict[str, int] = {player: random.randint(0, 1000)
                                    for player in capitalize_players}
    print(f"Score dict: {dict_players}")
    average: float = sum(dict_players.values()) / len(dict_players.values())
    print(f"Score average is {average:.2f}")
    high_scores: dict[str, int] = {
        player: score
        for player, score in dict_players.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_comprehensions()