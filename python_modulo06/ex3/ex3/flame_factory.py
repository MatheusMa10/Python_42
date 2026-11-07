from .creature_factory import CreatureFactory
from .flameling import Flameling
from .pyrodon import Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling()

    def create_evolved(self) -> Pyrodon:
        return Pyrodon()