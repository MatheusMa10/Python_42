from .creature import Creature


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire Dragon")

    def attack(self) -> str:
        return "Pyrodon unleashes a powerful fire blast!"