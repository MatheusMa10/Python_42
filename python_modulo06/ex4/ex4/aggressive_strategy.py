from ex3.ex3.creature import Creature
from ex3.ex3.transform_capability import TransformCapability

from ex4.battle_strategy import (
    BattleStrategy,
    InvalidStrategyError
)


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:

        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' "
                "for this aggressive strategy"
            )

        if isinstance(entity, TransformCapability):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())