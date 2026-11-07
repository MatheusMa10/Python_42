
from .creature import Creature
from .transform_capability import TransformCapability


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Shapeshifter")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        
        return "Shiftling attacks normally."

    def transform(self) -> None:
        self.is_transformed = True
        print("Shiftling shifts into a sharper form!")

    def revert(self) -> None:
        self.is_transformed = False
        print("Shiftling returns to normal.")