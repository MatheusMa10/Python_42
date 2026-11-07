from .creature_factory import CreatureFactory
from .shiftling import Shiftling
from .morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()