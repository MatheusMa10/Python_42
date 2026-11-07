from .creature import Creature
from .transform_capability import TransformCapability


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Evolved Shapeshifter")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"

        return "Morphagon attacks normally."


    def transform(self) -> None:
        self.is_transformed = True
        print("Morphagon morphs into a dragonic battle form!")


    def revert(self) -> None:
        self.is_transformed = False
        print("Morphagon stabilizes its form.")