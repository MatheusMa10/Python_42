from ex3.creature import Creature

from ex4.battle_strategy import (
    BattleStrategy,
    InvalidStrategyError
)


class NormalStrategy(BattleStrategy):

    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:

        if not self.is_valid(entity):
            raise InvalidStrategyError(
                f"Invalid Creature '{entity.name}' "
                "for this normal strategy"
            )

        print(entity.attack())
